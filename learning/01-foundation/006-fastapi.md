# ⚡ FastAPI Fundamentals

## Goal

Understand how FastAPI works internally and how it is used to build modern REST APIs.

This chapter explains FastAPI from an enterprise backend perspective using the ShopSphere project.

---

# What is FastAPI?

FastAPI is a modern Python web framework used to build REST APIs.

It is designed to be:

- Fast
- Easy to Learn
- Type Safe
- Production Ready

FastAPI automatically provides:

- Request Validation
- Response Validation
- Interactive API Documentation
- Data Serialization
- Error Handling

---

# Why FastAPI?

Compared to Flask

✅ Automatic Validation

✅ Swagger UI

✅ Type Hints

✅ Better Performance

✅ Better Developer Experience

Compared to Django

✅ Lightweight

✅ API Focused

✅ Easier Microservices

---

# What Does FastAPI Do?

Imagine someone visits

```
POST /customers
```

FastAPI is responsible for

- Receiving HTTP Request
- Finding Correct API
- Validating Request
- Calling Your Code
- Returning HTTP Response

Everything else is your responsibility.

---

# FastAPI Architecture

```
Browser

↓

FastAPI

↓

Router

↓

Service

↓

Repository

↓

PostgreSQL

↓

Response

↓

Browser
```

FastAPI acts as the framework that connects everything together.

---

# Creating the Application

Example

```python
from fastapi import FastAPI

app = FastAPI()
```

This creates one FastAPI application.

Think of it as creating the entire backend server.

---

# Running the Application

```
uvicorn app.main:app --reload
```

Meaning

```
app

↓

main.py

↓

app object
```

Uvicorn starts the FastAPI server.

---

# APIRouter

Instead of putting every API in

```
main.py
```

FastAPI provides

```
APIRouter
```

Example

```python
router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)
```

Each business domain gets its own router.

---

# Router Registration

Creating a router is not enough.

It must be registered.

Example

```python
app.include_router(customer_router)
```

Now FastAPI knows about

```
/customers
```

---

# API Endpoint

Example

```python
@router.post("/")
```

creates

```
POST /customers
```

because

```
prefix="/customers"
```

is automatically added.

---

# Decorators

FastAPI uses decorators.

Example

```python
@router.post("/")
```

Internally

```python
create_customer = router.post("/")(
    create_customer
)
```

The decorator registers the function as an API endpoint.

---

# Request Handling

Example

```python
def create_customer(
    customer: CustomerCreateRequest
):
```

FastAPI automatically

- Reads JSON
- Creates Python Object
- Validates Data

before your function executes.

---

# Response Handling

Example

```python
response_model=CustomerCreateResponse
```

FastAPI automatically

- Converts Python Objects to JSON
- Validates Response Structure

---

# Dependency Injection

FastAPI supports dependency injection.

Example

```python
Depends(get_db)
```

We'll use this later for

- Database Sessions
- Authentication
- Authorization

---

# Swagger UI

One of FastAPI's biggest advantages.

Automatically available at

```
/docs
```

Features

- API Testing
- Documentation
- Request Examples
- Response Examples

No extra work required.

---

# OpenAPI

FastAPI automatically generates

```
openapi.json
```

Other applications can use this document to understand your APIs.

---

# FastAPI Project Structure

```
app/

api/

schemas/

services/

repositories/

db/

main.py
```

This keeps the project modular.

---

# Request Lifecycle

```
Browser

↓

FastAPI

↓

Router

↓

Pydantic Schema

↓

Service

↓

Repository

↓

PostgreSQL

↓

Response

↓

Browser
```

Every request follows this flow.

---

# FastAPI Features Used in ShopSphere

Current

✅ FastAPI()

✅ APIRouter()

✅ include_router()

✅ Swagger

Future

⏳ Dependency Injection

⏳ Authentication

⏳ Middleware

⏳ Background Tasks

⏳ File Upload

---

# Best Practices

- One router per business domain

- Keep routers thin

- Use Pydantic Schemas

- Delegate business logic to Services

- Keep configuration centralized

---

# Common Mistakes

❌ Putting everything in main.py

❌ Writing SQL inside routers

❌ Mixing business logic with HTTP handling

❌ Returning inconsistent responses

---

# Interview Questions

### What is FastAPI?

A modern Python framework for building high-performance REST APIs.

---

### Why FastAPI over Flask?

Automatic validation

Type hints

Swagger

Better performance

---

### What is APIRouter?

A component used to organize related endpoints into modular groups.

---

### What does include_router() do?

Registers a router with the FastAPI application.

Without it, the APIs inside that router are not accessible.

---

### What is Swagger?

Automatically generated interactive API documentation.

---

### What is OpenAPI?

A standard specification describing REST APIs.

FastAPI generates it automatically.

---

# Where We Used This in ShopSphere

Application

```python
app = FastAPI()
```

Routers

```python
APIRouter()
```

Registration

```python
include_router()
```

Swagger

```
/docs
```

Customer API

```
POST /customers
```

---

# Revision Notes

✅ FastAPI creates the application.

✅ APIRouter groups APIs.

✅ include_router registers routers.

✅ Swagger is automatic.

✅ FastAPI validates requests.

---

# Exercises

1. Create a Product Router.

2. Add GET /products.

3. Add POST /products.

4. Register Product Router in main.py.

5. Explain why include_router() is required.

---

# Prerequisites

- Python Fundamentals

- OOP

- REST APIs

---

# Next Chapter

➡️ 007-pydantic.md