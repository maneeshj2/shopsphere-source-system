# 🏗️ Project Architecture

## Goal

Understand how all the components of ShopSphere work together to process a request.

By the end of this chapter, you should understand the complete request lifecycle from the browser to PostgreSQL and back.

---

# Why Do We Need an Architecture?

Imagine a project with

- 500 APIs
- 300 Database Tables
- 50 Developers

Without an architecture,

everyone writes code differently.

Soon the project becomes difficult to maintain.

Architecture provides consistency.

---

# ShopSphere Architecture

```
                Browser / Mobile App

                        │

                HTTP Request

                        │

                FastAPI Application

                        │

              ┌────────────────┐
              │     Router     │
              └────────────────┘

                        │

              Validate Request
                 (Pydantic)

                        │

              ┌────────────────┐
              │    Service     │
              └────────────────┘

                        │

              Business Rules

                        │

              ┌────────────────┐
              │   Repository   │
              └────────────────┘

                        │

              Database Session

                        │

                 PostgreSQL

                        │

                 Query Result

                        │

              Repository

                        │

              Service

                        │

           Response Model (Pydantic)

                        │

              JSON Response

                        │

                Browser
```

---

# Layer Responsibilities

## API Layer

Responsible for

- Receiving HTTP Requests
- Returning HTTP Responses
- Calling Services

Should NOT

- Write SQL
- Hash Passwords
- Implement Business Logic

---

## Pydantic Layer

Responsible for

- Request Validation
- Response Validation
- Data Serialization

Acts as the contract between the client and the backend.

---

## Service Layer

Responsible for

- Business Rules
- Business Validation
- Calling Repositories
- Data Transformation

Examples

- Hash Password
- Calculate Loyalty Points
- Check Stock Availability

---

## Repository Layer

Responsible for

- Database Access
- CRUD Operations
- Executing SQL / ORM

Should NOT

- Implement Business Logic
- Return HTTP Responses

---

## Database Layer

Responsible for

- Creating Database Sessions
- Managing Transactions
- Connecting to PostgreSQL

---

## PostgreSQL

Stores

- Customers
- Products
- Orders
- Inventory
- Payments

Acts as the OLTP database.

---

# Complete Request Flow

Customer Registration

```
Browser

↓

POST /customers

↓

Router

↓

CustomerCreateRequest

↓

Customer Service

↓

Hash Password

↓

Customer Repository

↓

INSERT INTO customers

↓

Commit

↓

CustomerCreateResponse

↓

JSON

↓

Browser
```

---

# Folder Structure

```
app/

├── api/
├── core/
├── db/
├── models/
├── repositories/
├── schemas/
├── services/
├── utils/
└── main.py
```

Every folder has one responsibility.

---

# Dependency Flow

```
Router

↓

Service

↓

Repository

↓

Database
```

Notice

Dependencies always move downward.

Repositories should never call Routers.

Services should never call APIs.

---

# Data Flow

Incoming

```
JSON

↓

Pydantic

↓

Python Object

↓

Service

↓

Repository

↓

Database
```

Outgoing

```
Database

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

# Why Separate Layers?

Imagine password hashing.

Without layers

```
Router

↓

Hash Password
```

Another API

↓

Hash Password

Duplicate code.

With layers

```
Router

↓

Service

↓

hash_password()

↓

Repository
```

Reusable.

Maintainable.

---

# Benefits

- Loose Coupling
- Better Testing
- Easier Maintenance
- Code Reuse
- Clear Responsibilities
- Enterprise Ready

---

# Internal Working

```
HTTP Request

↓

FastAPI

↓

Router Match

↓

Dependency Injection

↓

Pydantic Validation

↓

Service

↓

Repository

↓

Session

↓

PostgreSQL

↓

Rows

↓

Repository

↓

Service

↓

Pydantic Response

↓

JSON Serialization

↓

HTTP Response
```

---

# Enterprise Perspective

Large companies follow very similar layered architectures.

Example

Amazon

```
API Gateway

↓

Microservice

↓

Service

↓

Repository

↓

Aurora PostgreSQL
```

Netflix

```
API

↓

Business Service

↓

Data Access Layer

↓

Database
```

The concepts remain the same.

---

# ShopSphere Today

Current

✅ Docker

✅ PostgreSQL

✅ FastAPI

✅ Pydantic

✅ Service Layer

✅ Repository

Future

⏳ Authentication

⏳ Product Module

⏳ Orders

⏳ Payments

⏳ Snowflake Pipeline

---

# Best Practices

- One responsibility per layer
- Keep routers thin
- Keep services focused
- Keep repositories database-specific
- Use dependency injection
- Validate requests early

---

# Common Mistakes

❌ SQL inside Router

❌ Business Logic inside Repository

❌ Returning HTTP Responses from Service

❌ One giant Service class

❌ Tight coupling between layers

---

# Comparison

| Layer | Responsibility |
|--------|----------------|
| Router | HTTP |
| Pydantic | Validation |
| Service | Business Logic |
| Repository | Database |
| PostgreSQL | Data Storage |

---

# Interview Questions

### Why use a layered architecture?

To separate concerns, improve maintainability, enable testing, and make the application easier to scale.

---

### Which layer contains business logic?

The Service Layer.

---

### Which layer communicates with PostgreSQL?

The Repository Layer using a database session.

---

### Should a Router call PostgreSQL directly?

No.

The Router should delegate work to the Service Layer.

---

### Why shouldn't business logic be placed in the Repository?

The Repository should focus only on data access. Mixing business rules with SQL makes the application harder to maintain and test.

---

# Where We Used This in ShopSphere

```
Browser

↓

POST /customers

↓

Router

↓

CustomerCreateRequest

↓

Customer Service

↓

Customer Repository

↓

PostgreSQL

↓

CustomerCreateResponse

↓

Browser
```

---

# Revision Notes

✅ Router handles HTTP.

✅ Pydantic validates data.

✅ Service contains business logic.

✅ Repository performs database operations.

✅ PostgreSQL stores data.

---

# Exercises

1. Draw the complete request flow for customer registration.

2. Explain why SQL should not be written in the Router.

3. Which layer should calculate loyalty points?

4. Which layer should hash passwords?

5. Which layer should execute INSERT statements?

---

# Prerequisites

- FastAPI
- Pydantic
- Service Layer
- Repository Pattern
- Dependency Injection

---

# Next Chapter

➡️ 018-request-lifecycle.md