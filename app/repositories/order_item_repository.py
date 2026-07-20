from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.order_item import OrderItem


class OrderItemRepository:
    """
    Repository class for OrderItem database operations.
    """

    @staticmethod
    def create_order_items(
        db: Session,
        order_items: list[OrderItem],
    ) -> list[OrderItem]:
        """
        Persist multiple order items.
        """

        db.add_all(order_items)
        db.flush()

        return order_items

    @staticmethod
    def get_order_items_by_order_id(
        db: Session,
        order_id: UUID,
    ) -> list[OrderItem]:
        """
        Retrieve all active order items for an order.
        """

        stmt = (
            select(OrderItem)
            .where(
                OrderItem.order_id == order_id,
            )
            .order_by(OrderItem.created_at)
        )

        return list(db.execute(stmt).scalars().all())