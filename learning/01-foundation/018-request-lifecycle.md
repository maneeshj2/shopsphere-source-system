# 🔄 Complete Request Lifecycle

## Goal

Understand the complete lifecycle of an HTTP request in ShopSphere, from the moment a client sends a request until the response is returned.

This chapter ties together everything learned so far.

---

# Why Learn the Request Lifecycle?

Imagine someone asks you in an interview:

> "What happens internally when someone calls a FastAPI endpoint?"

Most developers answer:

> "FastAPI calls the function."

That answer is only 5% of the story.

The real flow involves:

- HTTP
- Uvicorn
- FastAPI
- Routing
- Dependency Injection
- Pydantic
- Service Layer
- Repository
- Database Session
- PostgreSQL
- JSON Serialization

Understanding this flow makes you a much stronger backend engineer.

---

# High Level Flow

```
Browser

↓

HTTP Request

↓

Uvicorn

↓

FastAPI

↓

Router

↓

Dependency Injection

↓

Pydantic Validation

↓

Service Layer

↓

Repository

↓

Database Session

↓

PostgreSQL

↓

Repository

↓

Service

↓

Pydantic Response

↓

JSON

↓

Browser
```

---

# Step 1

Customer clicks

```
Register
```

Browser creates

```
POST /customers
```

Request Body

```json
{
    "first_name":"Maneesh",
    "email":"maneesh@gmail.com",
    "password":"Password@123"
}
```

---

# Step 2

Browser sends HTTP request

↓

Internet

↓

FastAPI Server

---

# Step 3

Uvicorn receives the request

Remember

```
uvicorn app.main:app
```

Uvicorn is the ASGI server.

Its job is

- Listen on a port
- Receive HTTP requests
- Pass requests to FastAPI

---

# Step 4

FastAPI receives the request

FastAPI now asks

```
Which API should handle

POST /customers ?
```

---

# Step 5

Router Matching

FastAPI checks

```
include_router(...)
```

Finds

```python
@router.post("/")
```

inside

```
customers.py
```

Request is routed correctly.

---

# Step 6

Dependency Injection

Before executing the API

FastAPI resolves

```python
Depends(get_db)
```

Result

```
Database Session Created
```

Other dependencies may include

- Current User
- Logger
- Configuration

---

# Step 7

Pydantic Validation

Incoming JSON

↓

CustomerCreateRequest

Checks

- Required fields
- Email format
- Password length
- Data types

If validation fails

↓

HTTP 422

API never executes.

---

# Step 8

Router Executes

Example

```python
create_customer(...)
```

Notice

Router contains almost no business logic.

It simply delegates work.

---

# Step 9

Service Layer

Customer Service receives

```
CustomerCreateRequest
```

Business Logic

- Check Email Exists
- Hash Password
- Generate Loyalty Points
- Prepare Customer Object

---

# Step 10

Repository Layer

Repository receives

```
Customer Object
```

Executes

```
INSERT INTO customers
```

using SQLAlchemy or SQL.

---

# Step 11

Database Session

Repository uses

```
Session
```

to

- Track Changes
- Execute SQL
- Manage Transaction

---

# Step 12

PostgreSQL

Receives SQL

```
INSERT

↓

Execute

↓

Commit

↓

Return Row
```

Customer now exists.

---

# Step 13

Repository Returns

Repository returns

```
Customer Object
```

to Service.

---

# Step 14

Service Layer

Service prepares

```
CustomerCreateResponse
```

Notice

Password Hash

↓

Never returned.

---

# Step 15

Pydantic Response Validation

FastAPI validates

```
CustomerCreateResponse
```

Ensures

Only expected fields are returned.

---

# Step 16

JSON Serialization

Python Object

↓

JSON

Automatically handled by FastAPI.

---

# Step 17

HTTP Response

FastAPI returns

```
201 Created
```

along with JSON.

Browser receives response.

Registration successful.

---

# Complete End-to-End Flow

```
Browser

↓

HTTP

↓

Uvicorn

↓

FastAPI

↓

Router

↓

Depends()

↓

Pydantic

↓

Service

↓

Repository

↓

Session

↓

PostgreSQL

↓

Session

↓

Repository

↓

Service

↓

Pydantic

↓

JSON

↓

Browser
```

---

# What If Something Goes Wrong?

Example

Invalid Email

↓

Pydantic

↓

422

---

Database Error

↓

Repository

↓

Exception

↓

Service

↓

Router

↓

500

---

Customer Already Exists

↓

Service

↓

409 Conflict

---

# ShopSphere Example

```
POST /customers

↓

Validate

↓

Hash Password

↓

Insert Customer

↓

Commit

↓

Return customer_id

↓

201 Created
```

---

# Internal Components

| Component | Responsibility |
|-----------|----------------|
| Browser | Sends Request |
| Uvicorn | Receives HTTP |
| FastAPI | Framework |
| Router | Finds API |
| Depends | Injects Dependencies |
| Pydantic | Validation |
| Service | Business Logic |
| Repository | Database Access |
| Session | Transaction |
| PostgreSQL | Data Storage |

---

# Enterprise Perspective

This same request flow exists in almost every backend framework.

Spring Boot

↓

Tomcat

↓

Controller

↓

Service

↓

Repository

↓

Database

.NET

↓

Kestrel

↓

Controller

↓

Service

↓

Repository

↓

SQL Server

Only the framework changes.

The architecture remains almost identical.

---

# Best Practices

- Keep Routers thin
- Validate early
- Use Dependency Injection
- Keep Services focused
- Repositories should only access data
- Return consistent responses

---

# Common Mistakes

❌ Business Logic in Router

❌ SQL in Router

❌ Multiple commits per request

❌ Returning password_hash

❌ Ignoring validation errors

---

# Interview Questions

### What happens when a request reaches FastAPI?

The request is received by Uvicorn, routed by FastAPI, validated by Pydantic, processed by the Service Layer, persisted through the Repository Layer, committed to PostgreSQL, and finally serialized into a JSON response.

---

### Which layer performs validation?

Pydantic.

---

### Which layer contains business logic?

Service Layer.

---

### Which layer talks to PostgreSQL?

Repository Layer.

---

### Which component converts Python objects into JSON?

FastAPI using Pydantic serialization.

---

# Where We Use This in ShopSphere

Customer Registration

↓

Complete request flow

Product Creation

↓

Same lifecycle

Order Creation

↓

Same lifecycle

Authentication

↓

Same lifecycle

Only the Service changes.

---

# Revision Notes

✅ Browser sends HTTP.

✅ Uvicorn receives.

✅ FastAPI routes.

✅ Pydantic validates.

✅ Service executes business logic.

✅ Repository talks to PostgreSQL.

✅ FastAPI serializes the response.

---

# Exercises

1. Draw the complete request lifecycle from memory.

2. What happens before the Router executes?

3. Why is Pydantic executed before the Service Layer?

4. Which component creates the Database Session?

5. What happens after PostgreSQL commits the transaction?

---

# Prerequisites

- FastAPI
- Pydantic
- Dependency Injection
- Service Layer
- Repository Pattern
- Database Sessions

---

# Next Chapter

➡️ 019-configuration-management.md