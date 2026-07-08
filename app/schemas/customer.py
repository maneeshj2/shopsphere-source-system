from datetime import date

from pydantic import BaseModel, EmailStr, Field


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