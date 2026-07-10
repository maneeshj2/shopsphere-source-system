from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.customer import (
    CustomerCreateRequest,
    CustomerCreateResponse,
    CustomerDeleteResponse,
    CustomerListResponse,
    CustomerResponse,
    CustomerUpdateRequest,
)
from app.services.customer_service import (
    create_customer,
    delete_customer,
    get_customer_by_id,
    get_customers,
    update_customer,
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)


# =====================================
# Create Customer
# =====================================

@router.post(
    "",
    response_model=CustomerCreateResponse,
    status_code=201,
)
def register_customer(
    customer: CustomerCreateRequest,
    db: Session = Depends(get_db),
) -> CustomerCreateResponse:
    """
    Register a new customer.
    """

    return create_customer(
        db=db,
        customer=customer,
    )


# =====================================
# Get Customer by ID
# =====================================

@router.get(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def fetch_customer_by_id(
    customer_id: UUID,
    db: Session = Depends(get_db),
) -> CustomerResponse:
    """
    Fetch a customer using customer ID.
    """

    return get_customer_by_id(
        db=db,
        customer_id=customer_id,
    )


# =====================================
# Get Customers
# =====================================

@router.get(
    "",
    response_model=CustomerListResponse,
)
def fetch_customers(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db),
) -> CustomerListResponse:
    """
    Fetch customers with pagination.
    """

    return get_customers(
        db=db,
        page=page,
        size=size,
    )


# =====================================
# Update Customer
# =====================================

@router.put(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def update_customer_by_id(
    customer_id: UUID,
    request: CustomerUpdateRequest,
    db: Session = Depends(get_db),
) -> CustomerResponse:
    """
    Update customer details.
    """

    return update_customer(
        db=db,
        customer_id=customer_id,
        request=request,
    )

# =====================================
# Delete Customer
# =====================================

@router.delete(
    "/{customer_id}",
    response_model=CustomerDeleteResponse,
)
def delete_customer_by_id(
    customer_id: UUID,
    db: Session = Depends(get_db),
) -> CustomerDeleteResponse:
    """
    Soft delete a customer.
    """

    return delete_customer(
        db=db,
        customer_id=customer_id,
    )