from decimal import Decimal
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product
from app.repositories.customer_repository import CustomerRepository
from app.repositories.order_item_repository import OrderItemRepository
from app.repositories.order_repository import OrderRepository
from app.repositories.product_repository import ProductRepository
from app.schemas.order import (
    OrderCreateRequest,
    OrderDeleteResponse,
    OrderDetailResponse,
    OrderItemResponse,
    OrderListResponse,
    OrderResponse,
)


# ==========================================================
# Helper Methods
# ==========================================================

def _build_order_response(order: Order) -> OrderResponse:
    return OrderResponse.model_validate(order)


def _build_order_detail_response(
    order: Order,
    order_items: list[OrderItem],
) -> OrderDetailResponse:

    return OrderDetailResponse(
        order_id=order.order_id,
        customer_id=order.customer_id,
        order_date=order.order_date,
        order_status=order.order_status,
        payment_status=order.payment_status,
        total_amount=order.total_amount,
        shipping_address=order.shipping_address,
        items=[
            OrderItemResponse(
                product_id=item.product_id,
                quantity=item.quantity,
                unit_price=item.unit_price,
                line_total=item.line_total,
            )
            for item in order_items
        ],
    )


# ==========================================================
# Create Order
# ==========================================================

def create_order(
    db: Session,
    request: OrderCreateRequest,
) -> OrderResponse:

    customer = CustomerRepository.get_customer_by_id(
        db=db,
        customer_id=request.customer_id,
    )

    if customer is None:
        raise ValueError("Customer not found.")

    total_amount = Decimal("0.00")
    order_items: list[OrderItem] = []

    try:

        order = Order(
            customer_id=request.customer_id,
            shipping_address=request.shipping_address,
            order_status="CONFIRMED",
            payment_status="PAID",
            total_amount=Decimal("0.00"),
        )

        OrderRepository.create_order(
            db=db,
            order=order,
        )

        for item in request.items:

            product: Product | None = ProductRepository.get_product_by_id(
                db=db,
                product_id=item.product_id,
            )

            if product is None:
                raise ValueError(
                    f"Product {item.product_id} not found."
                )

            if not product.is_active:
                raise ValueError(
                    f"{product.product_name} is inactive."
                )

            if product.stock_quantity < item.quantity:
                raise ValueError(
                    f"Insufficient stock for {product.product_name}."
                )

            line_total = product.price * item.quantity
            total_amount += line_total

            order_items.append(
                OrderItem(
                    order_id=order.order_id,
                    product_id=product.product_id,
                    quantity=item.quantity,
                    unit_price=product.price,
                    line_total=line_total,
                )
            )

            product.stock_quantity -= item.quantity

        order.total_amount = total_amount

        OrderItemRepository.create_order_items(
            db=db,
            order_items=order_items,
        )

        db.commit()
        db.refresh(order)

        return _build_order_response(order)

    except Exception:
        db.rollback()
        raise


# ==========================================================
# Get Order By ID
# ==========================================================

def get_order_by_id(
    db: Session,
    order_id: UUID,
) -> OrderDetailResponse:

    order = OrderRepository.get_order_by_id(
        db=db,
        order_id=order_id,
    )

    if order is None:
        raise ValueError("Order not found.")

    order_items = OrderItemRepository.get_order_items_by_order_id(
        db=db,
        order_id=order_id,
    )

    return _build_order_detail_response(
        order,
        order_items,
    )


# ==========================================================
# Get Orders
# ==========================================================

def get_orders(
    db: Session,
    page: int,
    size: int,
) -> OrderListResponse:

    orders = OrderRepository.get_orders(
        db=db,
        limit=size,
        offset=(page - 1) * size,
    )

    total_records = OrderRepository.get_total_orders(db=db)

    return OrderListResponse(
        orders=[
            _build_order_response(order)
            for order in orders
        ],
        total_records=total_records,
        page=page,
        size=size,
    )


# ==========================================================
# Delete Order
# ==========================================================

def delete_order(
    db: Session,
    order_id: UUID,
) -> OrderDeleteResponse:

    order = OrderRepository.get_order_by_id(
        db=db,
        order_id=order_id,
    )

    if order is None:
        raise ValueError("Order not found.")

    try:
        OrderRepository.delete_order(
            db=db,
            order=order,
        )

        db.commit()

        return OrderDeleteResponse(
            message="Order deleted successfully."
        )

    except Exception:
        db.rollback()
        raise