from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.order import (
    OrderCreateRequest,
    OrderDeleteResponse,
    OrderDetailResponse,
    OrderListResponse,
    OrderResponse,
)
from app.services.order_service import (
    create_order,
    delete_order,
    get_order_by_id,
    get_orders,
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


# ==========================================================
# Create Order
# ==========================================================

@router.post(
    "",
    response_model=OrderResponse,
    status_code=201,
)
def create_new_order(
    request: OrderCreateRequest,
    db: Session = Depends(get_db),
) -> OrderResponse:
    """
    Create a new order.
    """

    return create_order(
        db=db,
        request=request,
    )


# ==========================================================
# Get Order By ID
# ==========================================================

@router.get(
    "/{order_id}",
    response_model=OrderDetailResponse,
)
def fetch_order_by_id(
    order_id: UUID,
    db: Session = Depends(get_db),
) -> OrderDetailResponse:
    """
    Get an order by ID.
    """

    return get_order_by_id(
        db=db,
        order_id=order_id,
    )


# ==========================================================
# Get Orders
# ==========================================================

@router.get(
    "",
    response_model=OrderListResponse,
)
def fetch_orders(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db),
) -> OrderListResponse:
    """
    Get all orders with pagination.
    """

    return get_orders(
        db=db,
        page=page,
        size=size,
    )


# ==========================================================
# Delete Order
# ==========================================================

@router.delete(
    "/{order_id}",
    response_model=OrderDeleteResponse,
)
def delete_order_by_id(
    order_id: UUID,
    db: Session = Depends(get_db),
) -> OrderDeleteResponse:
    """
    Soft delete an order.
    """

    return delete_order(
        db=db,
        order_id=order_id,
    )