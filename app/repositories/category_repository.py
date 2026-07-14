from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.category import Category


class CategoryRepository:

    @staticmethod
    def create_category(
        db: Session,
        category: Category,
    ) -> Category:

        db.add(category)
        db.commit()
        db.refresh(category)

        return category

    @staticmethod
    def get_category_by_name(
        db: Session,
        category_name: str,
    ) -> Category | None:

        statement = select(Category).where(
            Category.category_name == category_name,
            Category.is_current.is_(True),
            Category.is_deleted.is_(False),
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()

    @staticmethod
    def get_category_by_id(
        db: Session,
        category_id: UUID,
    ) -> Category | None:

        statement = select(Category).where(
            Category.category_id == category_id,
            Category.is_current.is_(True),
            Category.is_deleted.is_(False),
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()

    @staticmethod
    def get_categories(
        db: Session,
        limit: int,
        offset: int,
    ) -> list[Category]:

        statement = (
            select(Category)
            .where(
                Category.is_current.is_(True),
                Category.is_deleted.is_(False),
            )
            .offset(offset)
            .limit(limit)
        )

        result = db.execute(statement)

        return result.scalars().all()

    @staticmethod
    def get_total_categories(
        db: Session,
    ) -> int:

        statement = (
            select(func.count())
            .select_from(Category)
            .where(
                Category.is_current.is_(True),
                Category.is_deleted.is_(False),
            )
        )

        result = db.execute(statement)

        return result.scalar_one()

    @staticmethod
    def update_category(
        db: Session,
        category: Category,
    ) -> Category:

        db.commit()
        db.refresh(category)

        return category

    @staticmethod
    def delete_category(
        db: Session,
        category: Category,
    ) -> Category:

        category.is_current = False
        category.is_deleted = True

        db.commit()
        db.refresh(category)

        return category