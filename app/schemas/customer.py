from datetime import date

from pydantic import BaseModel, EmailStr, Field


# =====================================
# Create Customer
# =====================================

class CustomerCreateRequest(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone_number: str = Field(..., min_length=10, max_length=20)
    password: str = Field(..., min_length=8)
    date_of_birth: date


class CustomerCreateResponse(BaseModel):
    customer_id: str
    message: str


# =====================================
# Update Customer
# =====================================

class CustomerUpdateRequest(BaseModel):
    first_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )
    last_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )
    phone_number: str | None = Field(
        default=None,
        min_length=10,
        max_length=20,
    )
    date_of_birth: date | None = None


# =====================================
# Customer Response
# =====================================

class CustomerResponse(BaseModel):
    customer_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    date_of_birth: date
    loyalty_points: int


# =====================================
# Customer List Response
# =====================================

class CustomerListResponse(BaseModel):
    customers: list[CustomerResponse]
    total_records: int
    page: int
    size: int

# =====================================
# Delete Customer
# =====================================

class CustomerDeleteResponse(BaseModel):
    message: str