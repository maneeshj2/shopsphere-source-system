from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


# ==========================================================
# Order Item Schemas
# ==========================================================

class OrderItemRequest(BaseModel):
    """
    Request model for a single order item.
    """

    product_id: UUID
    quantity: int = Field(gt=0)


class OrderItemResponse(BaseModel):
    """
    Response model for a single order item.
    """

    product_id: UUID
    quantity: int
    unit_price: Decimal
    line_total: Decimal

    model_config = ConfigDict(from_attributes=True)


# ==========================================================
# Create Order
# ==========================================================

class OrderCreateRequest(BaseModel):
    """
    Request model for creating an order.
    """

    customer_id: UUID

    shipping_address: str = Field(
        min_length=5,
        max_length=500,
    )

    items: list[OrderItemRequest] = Field(
        min_length=1,
    )


# ==========================================================
# Order Response
# ==========================================================

class OrderResponse(BaseModel):
    """
    Basic Order response.
    """

    order_id: UUID
    customer_id: UUID

    order_date: datetime

    order_status: str

    payment_status: str

    total_amount: Decimal

    shipping_address: str

    model_config = ConfigDict(from_attributes=True)


# ==========================================================
# Order Detail Response
# ==========================================================

class OrderDetailResponse(OrderResponse):
    """
    Detailed order response including items.
    """

    items: list[OrderItemResponse]


# ==========================================================
# Order List Response
# ==========================================================

class OrderListResponse(BaseModel):
    """
    Paginated order response.
    """

    orders: list[OrderResponse]

    total_records: int

    page: int

    size: int


# ==========================================================
# Delete Response
# ==========================================================

class OrderDeleteResponse(BaseModel):
    """
    Delete response.
    """

    message: str