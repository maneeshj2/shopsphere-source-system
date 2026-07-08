from app.schemas.customer import (
    CustomerCreateRequest,
    CustomerCreateResponse,
)


def create_customer(
    customer: CustomerCreateRequest,
) -> CustomerCreateResponse:

    # Business logic will come later

    return CustomerCreateResponse(
        customer_id="TEMP-UUID",
        message="Customer created successfully",
    )