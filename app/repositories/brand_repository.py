from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.brand import Brand


class BrandRepository:

    @staticmethod
    def create_brand(
        db: Session,
        brand: Brand,
    ) -> Brand:

        db.add(brand)
        db.commit()
        db.refresh(brand)

        return brand

    @staticmethod
    def get_brand_by_name(
        db: Session,
        brand_name: str,
    ) -> Brand | None:

        statement = select(Brand).where(
            Brand.brand_name == brand_name,
            Brand.is_current.is_(True),
            Brand.is_deleted.is_(False),
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()

    @staticmethod
    def get_brand_by_id(
        db: Session,
        brand_id: UUID,
    ) -> Brand | None:

        statement = select(Brand).where(
            Brand.brand_id == brand_id,
            Brand.is_current.is_(True),
            Brand.is_deleted.is_(False),
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()

    @staticmethod
    def get_brands(
        db: Session,
        limit: int,
        offset: int,
    ) -> list[Brand]:

        statement = (
            select(Brand)
            .where(
                Brand.is_current.is_(True),
                Brand.is_deleted.is_(False),
            )
            .offset(offset)
            .limit(limit)
        )

        result = db.execute(statement)

        return result.scalars().all()

    @staticmethod
    def get_total_brands(
        db: Session,
    ) -> int:

        statement = (
            select(func.count())
            .select_from(Brand)
            .where(
                Brand.is_current.is_(True),
                Brand.is_deleted.is_(False),
            )
        )

        result = db.execute(statement)

        return result.scalar_one()

    @staticmethod
    def update_brand(
        db: Session,
        brand: Brand,
    ) -> Brand:

        db.commit()
        db.refresh(brand)

        return brand

    @staticmethod
    def delete_brand(
        db: Session,
        brand: Brand,
    ) -> Brand:

        brand.is_current = False
        brand.is_deleted = True

        db.commit()
        db.refresh(brand)

        return brand