from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.order import Order


class OrderRepository:
    """
    Repository class for Order database operations.
    """

    @staticmethod
    def create_order(
        db: Session,
        order: Order,
    ) -> Order:

        db.add(order)
        db.flush()
        db.refresh(order)

        return order

    @staticmethod
    def get_order_by_id(
        db: Session,
        order_id: UUID,
    ) -> Order | None:

        stmt = (
            select(Order)
            .where(Order.order_id == order_id)
        )

        return db.execute(stmt).scalar_one_or_none()

    @staticmethod
    def get_orders(
        db: Session,
        limit: int,
        offset: int,
    ) -> list[Order]:

        stmt = (
            select(Order)
            .order_by(Order.order_date.desc())
            .limit(limit)
            .offset(offset)
        )

        return list(db.execute(stmt).scalars().all())

    @staticmethod
    def get_total_orders(
        db: Session,
    ) -> int:

        stmt = (
            select(func.count())
            .select_from(Order)
        )

        return db.execute(stmt).scalar_one()

    @staticmethod
    def delete_order(
        db: Session,
        order: Order,
    ) -> None:

        db.delete(order)
        db.flush()