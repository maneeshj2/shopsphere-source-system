from uuid import UUID

from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository
from app.schemas.customer import (
    CustomerCreateRequest,
    CustomerCreateResponse,
    CustomerDeleteResponse,
    CustomerListResponse,
    CustomerResponse,
    CustomerUpdateRequest,
)
from app.utils.password import hash_password



# =====================================
# Helper
# =====================================

def _build_customer_response(customer: Customer) -> CustomerResponse:
    """
    Convert Customer model to CustomerResponse schema.
    """

    return CustomerResponse(
        customer_id=str(customer.customer_id),
        first_name=customer.first_name,
        last_name=customer.last_name,
        email=customer.email,
        phone_number=customer.phone_number,
        date_of_birth=customer.date_of_birth,
        loyalty_points=customer.loyalty_points,
    )


# =====================================
# Create Customer
# =====================================

def create_customer(
    db: Session,
    customer: CustomerCreateRequest,
) -> CustomerCreateResponse:

    existing_customer = CustomerRepository.get_customer_by_email(
        db=db,
        email=customer.email,
    )

    if existing_customer:
        raise ValueError("Customer with this email already exists.")

    new_customer = Customer(
        first_name=customer.first_name,
        last_name=customer.last_name,
        email=customer.email,
        phone_number=customer.phone_number,
        password_hash=hash_password(customer.password),
        date_of_birth=customer.date_of_birth,
    )

    saved_customer = CustomerRepository.create_customer(
        db=db,
        customer=new_customer,
    )

    return CustomerCreateResponse(
        customer_id=str(saved_customer.customer_id),
        message="Customer created successfully.",
    )


# =====================================
# Get Customer by ID
# =====================================

def get_customer_by_id(
    db: Session,
    customer_id: UUID,
) -> CustomerResponse:

    customer = CustomerRepository.get_customer_by_id(
        db=db,
        customer_id=customer_id,
    )

    if customer is None:
        raise ValueError("Customer not found.")

    return _build_customer_response(customer)


# =====================================
# Get Customers
# =====================================

def get_customers(
    db: Session,
    page: int,
    size: int,
) -> CustomerListResponse:

    limit = size
    offset = (page - 1) * size

    customers = CustomerRepository.get_customers(
        db=db,
        limit=limit,
        offset=offset,
    )

    total_records = CustomerRepository.get_total_customers(
        db=db,
    )

    customer_responses = [
        _build_customer_response(customer)
        for customer in customers
    ]

    return CustomerListResponse(
        customers=customer_responses,
        total_records=total_records,
        page=page,
        size=size,
    )


# =====================================
# Update Customer
# =====================================

def update_customer(
    db: Session,
    customer_id: UUID,
    request: CustomerUpdateRequest,
) -> CustomerResponse:

    customer = CustomerRepository.get_customer_by_id(
        db=db,
        customer_id=customer_id,
    )

    if customer is None:
        raise ValueError("Customer not found.")

    if request.first_name is not None:
        customer.first_name = request.first_name

    if request.last_name is not None:
        customer.last_name = request.last_name

    if request.phone_number is not None:
        customer.phone_number = request.phone_number

    if request.date_of_birth is not None:
        customer.date_of_birth = request.date_of_birth

    updated_customer = CustomerRepository.update_customer(
        db=db,
        customer=customer,
    )

    return _build_customer_response(updated_customer)

def delete_customer(
    db: Session,
    customer_id: UUID,
) -> CustomerDeleteResponse:
    """
    Soft delete a customer.
    """

    customer = CustomerRepository.get_customer_by_id(
        db=db,
        customer_id=customer_id,
    )

    if customer is None:
        raise ValueError("Customer not found.")

    CustomerRepository.delete_customer(
        db=db,
        customer=customer,
    )

    return CustomerDeleteResponse(
        message="Customer deleted successfully.",
    )