from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:

    @staticmethod
    def create_product(
        db: Session,
        product: Product,
    ) -> Product:

        db.add(product)
        db.commit()
        db.refresh(product)

        return product

    @staticmethod
    def get_product_by_id(
        db: Session,
        product_id: UUID,
    ) -> Product | None:

        statement = select(Product).where(
            Product.product_id == product_id,
            Product.is_current.is_(True),
            Product.is_deleted.is_(False),
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()

    @staticmethod
    def get_product_by_sku(
        db: Session,
        sku: str,
    ) -> Product | None:

        statement = select(Product).where(
            Product.sku == sku,
            Product.is_current.is_(True),
            Product.is_deleted.is_(False),
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()

    @staticmethod
    def get_products(
        db: Session,
        limit: int,
        offset: int,
    ) -> list[Product]:

        statement = (
            select(Product)
            .where(
                Product.is_current.is_(True),
                Product.is_deleted.is_(False),
            )
            .offset(offset)
            .limit(limit)
        )

        result = db.execute(statement)

        return result.scalars().all()

    @staticmethod
    def get_total_products(
        db: Session,
    ) -> int:

        statement = (
            select(func.count())
            .select_from(Product)
            .where(
                Product.is_current.is_(True),
                Product.is_deleted.is_(False),
            )
        )

        result = db.execute(statement)

        return result.scalar_one()

    @staticmethod
    def update_product(
        db: Session,
        product: Product,
    ) -> Product:

        db.commit()
        db.refresh(product)

        return product

    @staticmethod
    def delete_product(
        db: Session,
        product: Product,
    ) -> Product:

        product.is_current = False
        product.is_deleted = True

        db.commit()
        db.refresh(product)

        return product