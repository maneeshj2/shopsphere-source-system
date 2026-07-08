# 📦 Pydantic Fundamentals

## Goal

Understand how Pydantic validates data, converts JSON into Python objects, and acts as the contract between API clients and the backend.

This chapter explains Pydantic using examples from the ShopSphere project.

---

# What is Pydantic?

Pydantic is a Python library used for

- Data Validation
- Data Parsing
- Serialization
- Type Checking

FastAPI uses Pydantic extensively for validating API requests and responses.

---

# Why Do We Need Pydantic?

Imagine a client sends

```json
{
    "first_name": 123,
    "email": "not-an-email",
    "password": true
}
```

Without validation

↓

Invalid data reaches the database.

With Pydantic

↓

The request is rejected before our business logic executes.

---

# Where Does Pydantic Fit?

```
Browser

↓

JSON Request

↓

Pydantic

↓

Python Object

↓

Service Layer

↓

Repository

↓

PostgreSQL
```

Every request first passes through Pydantic.

---

# Real World Analogy

Imagine airport security.

Passenger

↓

Passport Verification

↓

Security Check

↓

Airport

Pydantic is the security checkpoint.

Only valid data is allowed inside.

---

# Creating a Model

Example

```python
from pydantic import BaseModel

class CustomerCreateRequest(BaseModel):

    first_name: str

    last_name: str

    email: EmailStr

    password: str
```

This defines the expected request structure.

---

# Creating an Object

```python
customer = CustomerCreateRequest(
    first_name="Maneesh",
    last_name="Joshi",
    email="maneesh@gmail.com",
    password="Password@123"
)
```

Pydantic validates every field.

---

# JSON → Python Object

Incoming JSON

```json
{
    "first_name":"Maneesh",
    "email":"maneesh@gmail.com"
}
```

Automatically becomes

```python
CustomerCreateRequest(
    first_name="Maneesh",
    email="maneesh@gmail.com"
)
```

No manual conversion required.

---

# Type Validation

Example

```python
age: int
```

Valid

```json
{
    "age":25
}
```

Invalid

```json
{
    "age":"Twenty Five"
}
```

Pydantic raises a validation error.

---

# Email Validation

Example

```python
from pydantic import EmailStr

email: EmailStr
```

Valid

```
abc@gmail.com
```

Invalid

```
abcgmail
```

Pydantic rejects invalid email formats automatically.

---

# Optional Fields

```python
from typing import Optional

phone_number: Optional[str] = None
```

The field is not required.

---

# Default Values

```python
country = "India"
```

If the client doesn't send the value,

Pydantic uses the default.

---

# Field Validation

Example

```python
from pydantic import Field

password: str = Field(
    min_length=8,
    max_length=20
)
```

Now

```
123
```

is rejected.

---

# Response Models

Pydantic is also used for responses.

Example

```python
class CustomerResponse(BaseModel):

    customer_id: UUID

    first_name: str

    email: EmailStr
```

The response structure is validated before being returned.

---

# Request Model vs Response Model

Request

```python
CustomerCreateRequest
```

Contains

```
password
```

Response

```python
CustomerResponse
```

Contains

```
customer_id

created_at
```

Never return passwords.

---

# Validation Errors

If validation fails,

FastAPI automatically returns

```json
{
    "detail":[
        ...
    ]
}
```

with HTTP

```
422 Unprocessable Entity
```

No extra coding required.

---

# Nested Models

Example

```python
class Address(BaseModel):

    city: str

    state: str

class Customer(BaseModel):

    first_name: str

    address: Address
```

Pydantic validates nested objects automatically.

---

# Lists

Example

```python
products: list[str]
```

or

```python
products: list[Product]
```

---

# Model Dump

Convert a Pydantic object to a dictionary.

```python
customer.model_dump()
```

Useful before saving data.

---

# Model Validation Flow

```
JSON

↓

Pydantic

↓

Python Object

↓

Business Logic

↓

Database
```

---

# ShopSphere Example

Customer Registration

Incoming JSON

↓

CustomerCreateRequest

↓

Customer Service

↓

Hash Password

↓

Repository

↓

Database

↓

CustomerResponse

↓

Browser

---

# Why Not Use Dictionaries?

Dictionary

```python
customer["email"]
```

No validation.

No autocomplete.

No type safety.

Pydantic Model

```python
customer.email
```

Validation.

Autocomplete.

Type Safety.

Cleaner code.

---

# Best Practices

- Separate Request and Response models
- Use EmailStr for emails
- Validate early
- Use Field() for constraints
- Keep models small
- One responsibility per model

---

# Common Mistakes

❌ One model for every API

❌ Returning password_hash

❌ Using dict instead of models

❌ Mixing database models with API models

---

# Interview Questions

### What is Pydantic?

A data validation library used by FastAPI.

---

### Why use Pydantic?

To validate and parse incoming and outgoing API data.

---

### Difference between BaseModel and SQLAlchemy Model?

BaseModel

↓

API Contract

SQLAlchemy Model

↓

Database Table

---

### What happens if validation fails?

FastAPI automatically returns

HTTP 422

with validation details.

---

### Why separate Request and Response Models?

To avoid exposing internal fields such as

- password_hash
- audit columns
- internal flags

---

# Where We Used This in ShopSphere

Customer Registration

```python
CustomerCreateRequest
```

Customer Response

```python
CustomerCreateResponse
```

Email Validation

```python
EmailStr
```

Password Validation

```python
Field(min_length=8)
```

---

# Revision Notes

✅ BaseModel

✅ EmailStr

✅ Field()

✅ Optional

✅ Response Models

✅ Validation

---

# Exercises

1. Create ProductCreateRequest.

2. Create ProductResponse.

3. Add validation for product price.

4. Make product description optional.

5. Add a minimum password length of 8.

---

# Prerequisites

- Python Fundamentals
- REST APIs
- FastAPI

---

# Next Chapter

➡️ 008-service-layer.md