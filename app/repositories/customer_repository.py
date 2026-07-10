from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.customer import Customer


class CustomerRepository:

    @staticmethod
    def create_customer(
        db: Session,
        customer: Customer,
    ) -> Customer:
        """
        Save a new customer to the database.
        """

        db.add(customer)
        db.commit()
        db.refresh(customer)

        return customer

    @staticmethod
    def get_customer_by_email(
        db: Session,
        email: str,
    ) -> Customer | None:
        """
        Fetch a customer by email.
        """

        statement = select(Customer).where(
            Customer.email == email,
            Customer.is_current.is_(True),
            Customer.is_deleted.is_(False),
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()

    @staticmethod
    def get_customer_by_id(
        db: Session,
        customer_id: UUID,
    ) -> Customer | None:
        """
        Fetch a customer by customer ID.
        """

        statement = select(Customer).where(
            Customer.customer_id == customer_id,
            Customer.is_current.is_(True),
            Customer.is_deleted.is_(False),
        )

        result = db.execute(statement)

        return result.scalar_one_or_none()

    @staticmethod
    def get_customers(
        db: Session,
        limit: int,
        offset: int,
    ) -> list[Customer]:
        """
        Fetch customers using pagination.
        """

        statement = (
            select(Customer)
            .where(
                Customer.is_current.is_(True),
                Customer.is_deleted.is_(False),
            )
            .offset(offset)
            .limit(limit)
        )

        result = db.execute(statement)

        return result.scalars().all()

    @staticmethod
    def get_total_customers(
        db: Session,
    ) -> int:
        """
        Get total number of customers.
        """

        statement = (
            select(func.count())
            .select_from(Customer)
            .where(
                Customer.is_current.is_(True),
                Customer.is_deleted.is_(False),
            )
        )

        result = db.execute(statement)

        return result.scalar_one()

    @staticmethod
    def update_customer(
        db: Session,
        customer: Customer,
    ) -> Customer:
        """
        Update an existing customer.
        """

        db.commit()
        db.refresh(customer)

        return customer
    
    @staticmethod
    def delete_customer(
        db: Session,
        customer: Customer,
    ) -> Customer:
        """
        Soft delete a customer.
        """

        customer.is_current = False
        customer.is_deleted = True

        db.commit()
        db.refresh(customer)

        return customer