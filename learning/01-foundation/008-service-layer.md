# 🧠 Service Layer

## Goal

Understand the purpose of the Service Layer, why enterprise applications use it, and how it keeps business logic separate from APIs and database operations.

This chapter uses ShopSphere to demonstrate how real-world applications organize business logic.

---

# What is the Service Layer?

The Service Layer is the part of the application responsible for implementing business rules.

It receives validated data from the API Layer, performs business operations, communicates with repositories, and returns the result.

It acts as the brain of the application.

---

# Why Do We Need a Service Layer?

Imagine we don't have one.

```
API

↓

Validate Email

↓

Hash Password

↓

Generate UUID

↓

Check Existing Customer

↓

Save Customer

↓

Send Welcome Email

↓

Return Response
```

Everything is inside the API.

After a few months,

every API becomes hundreds of lines long.

Maintenance becomes difficult.

---

# With Service Layer

```
API

↓

Customer Service

↓

Customer Repository

↓

PostgreSQL
```

Each layer has one responsibility.

---

# Real World Analogy

Imagine a bank.

```
Customer

↓

Receptionist

↓

Bank Manager

↓

Cashier
```

Receptionist

Receives requests.

Bank Manager

Makes decisions.

Cashier

Handles money.

In ShopSphere

```
Browser

↓

API

↓

Service

↓

Repository

↓

Database
```

The Service Layer is the Bank Manager.

---

# Responsibilities

The Service Layer should

- Implement business rules
- Validate business conditions
- Coordinate multiple repositories
- Transform data
- Call external services
- Return business results

---

# What It Should NOT Do

The Service Layer should not

- Receive HTTP requests
- Return HTTP responses
- Execute SQL directly
- Create database connections

Those belong to other layers.

---

# Typical Flow

Customer Registration

```
Browser

↓

POST /customers

↓

Router

↓

Customer Service

↓

Customer Repository

↓

PostgreSQL

↓

Response
```

---

# Example

```python
def create_customer(customer):

    validate_customer(customer)

    hashed_password = hash_password(customer.password)

    repository.create_customer(customer, hashed_password)

    return response
```

Notice

No HTTP.

No SQL.

Only business logic.

---

# Why Not Write Everything in the Router?

Bad Example

```python
@router.post("/")

def create_customer():

    validate_email()

    hash_password()

    execute_sql()

    send_email()

    update_inventory()
```

This Router now has

- Validation
- Security
- SQL
- Email
- Inventory

Everything mixed together.

---

# Good Example

```python
@router.post("/")

def create_customer(customer):

    return customer_service.create_customer(customer)
```

Simple.

Easy to understand.

Easy to maintain.

---

# Service Calling Repository

```
Customer Service

↓

Customer Repository

↓

INSERT customer

↓

Database
```

The Service knows **what** to do.

The Repository knows **how** to do it.

---

# One Service Can Call Multiple Repositories

Example

Order Creation

```
Order Service

↓

Customer Repository

↓

Inventory Repository

↓

Payment Repository

↓

Shipment Repository
```

One business process.

Multiple repositories.

---

# Business Rules

Business rules belong here.

Examples

✔ Email must be unique

✔ Customer must be 18+

✔ Order total must be positive

✔ Product stock must exist

✔ Loyalty points calculation

---

# Data Transformation

Example

Incoming Request

```json
{
    "password":"Password123"
}
```

Service

↓

Hash Password

↓

Repository

```
password_hash
```

The Service transforms the data.

---

# External Services

Sometimes the Service talks to

```
SMTP

Redis

Payment Gateway

SMS Service

Kafka

AWS S3
```

The Router should never do this directly.

---

# Error Handling

Service Layer decides

```
Customer Exists?

↓

Raise Exception
```

The API converts that exception into

```
HTTP 409
```

---

# Internal Working

```
HTTP Request

↓

Router

↓

Validated Request

↓

Service

↓

Business Logic

↓

Repository

↓

Database

↓

Service

↓

Response Object

↓

Router

↓

HTTP Response
```

---

# ShopSphere Example

Customer Registration

```
Receive Customer

↓

Check Email Exists

↓

Hash Password

↓

Assign Loyalty Points

↓

Repository

↓

Customer Created

↓

Return Response
```

Notice

Everything related to business happens here.

---

# Service vs Repository

| Service | Repository |
|----------|------------|
| Business Logic | Database Logic |
| Knows Business | Knows SQL |
| Calls Repository | Talks to PostgreSQL |
| No SQL | SQL Allowed |
| Coordinates Work | Performs CRUD |

---

# Service vs Router

| Router | Service |
|----------|---------|
| HTTP | Business |
| Request | Validation |
| Response | Calculations |
| Status Codes | Rules |
| API Layer | Business Layer |

---

# Enterprise Example

Amazon

Customer places order

↓

Order Service

↓

Inventory Service

↓

Payment Service

↓

Shipping Service

↓

Notification Service

Every service has one responsibility.

---

# Best Practices

- Keep Services focused
- One Service per business domain
- Reuse business logic
- Keep methods small
- Don't write SQL here

---

# Common Mistakes

❌ SQL inside Service

❌ HTTP responses inside Service

❌ Very large methods

❌ Business logic inside Router

❌ Repository calling Service

---

# Interview Questions

### What is the Service Layer?

The Service Layer contains business logic and coordinates application workflows.

---

### Why is Service Layer required?

It separates business logic from HTTP handling and database access, making the application easier to maintain and test.

---

### Can one Service call multiple Repositories?

Yes.

This is very common in enterprise applications.

---

### Should SQL be written inside Service?

No.

SQL belongs in the Repository Layer.

---

### Should HTTP responses be created inside Service?

No.

The Router handles HTTP.

The Service returns business objects.

---

# Where We Used This in ShopSphere

Customer Registration

```
Customer Router

↓

Customer Service

↓

Hash Password

↓

Repository

↓

Database
```

Future

```
Order Service

↓

Inventory

↓

Payment

↓

Shipment
```

---

# Revision Notes

✅ Service = Business Logic

✅ Repository = Database Logic

✅ Router = HTTP Layer

✅ One Service can call many Repositories

✅ Service should never execute SQL directly

---

# Exercises

1. Write the flow for Product Registration.

2. List five business rules for an Order Service.

3. Explain why password hashing belongs in the Service Layer.

4. Can a Service call another Service? Give one example.

5. What happens if the Repository throws an exception?

---

# Prerequisites

- REST APIs
- FastAPI
- Pydantic

---

# Next Chapter

➡️ 009-repository-pattern.md