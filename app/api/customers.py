from fastapi import APIRouter

from app.schemas.customer import (
    CustomerCreateRequest,
    CustomerCreateResponse,
)
from app.services import customer_service

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)


@router.post(
    "/",
    response_model=CustomerCreateResponse,
)
def create_customer(
    customer: CustomerCreateRequest,
):
    return customer_service.create_customer(customer)