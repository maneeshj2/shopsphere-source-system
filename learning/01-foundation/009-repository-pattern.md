# 🗄️ Repository Pattern

## Goal

Understand what the Repository Pattern is, why it is used in enterprise applications, and how it separates business logic from database operations.

This chapter explains the Repository Pattern using the ShopSphere project.

---

# What is the Repository Pattern?

The Repository Pattern is a design pattern that separates **database access** from **business logic**.

Instead of writing SQL inside the Service Layer, all database operations are moved into Repository classes.

Think of the Repository as the application's Data Access Layer (DAL).

---

# Why Do We Need a Repository?

Imagine there is no Repository.

```
Customer Service

↓

SELECT ...

↓

INSERT ...

↓

UPDATE ...

↓

DELETE ...
```

Now imagine five services doing this.

The same SQL gets copied everywhere.

Maintenance becomes difficult.

Instead

```
Customer Service

↓

Customer Repository

↓

PostgreSQL
```

Now SQL exists in only one place.

---

# Real World Analogy

Imagine a library.

Reader

↓

Librarian

↓

Bookshelf

The reader never walks into the storage room.

The librarian fetches the book.

Similarly,

Service

↓

Repository

↓

Database

---

# Architecture

```
Browser

↓

Router

↓

Service

↓

Repository

↓

Database
```

Each layer has a single responsibility.

---

# Responsibilities

Repository should

- Read Data
- Insert Data
- Update Data
- Delete Data
- Execute SQL
- Return Database Results

---

# Repository SHOULD NOT

- Validate Business Rules
- Hash Passwords
- Calculate Discounts
- Send Emails
- Handle HTTP Requests

Those belong to the Service Layer.

---

# Typical Repository

```python
class CustomerRepository:

    def create_customer(...):

        ...

    def get_customer(...):

        ...

    def update_customer(...):

        ...

    def delete_customer(...):

        ...
```

Notice

Only CRUD operations.

---

# CRUD

Create

↓

INSERT

Read

↓

SELECT

Update

↓

UPDATE

Delete

↓

DELETE

---

# Example

Service

```python
customer = repository.get_customer_by_email(email)
```

Repository

```python
SELECT *

FROM customers

WHERE email = ...
```

The Service doesn't know SQL.

The Repository doesn't know business rules.

---

# Internal Working

```
Customer Service

↓

repository.get_customer()

↓

SQL Generated

↓

PostgreSQL

↓

Rows Returned

↓

Repository

↓

Customer Object

↓

Service
```

---

# ShopSphere Example

Customer Registration

```
Customer Service

↓

Check Existing Customer

↓

Customer Repository

↓

SELECT

↓

Database

↓

Customer Exists?

↓

Service
```

If customer doesn't exist

↓

Repository

↓

INSERT

↓

Database

---

# Repository vs Service

| Repository | Service |
|------------|----------|
| Executes SQL | Business Logic |
| CRUD | Rules |
| Database Access | Process |
| No Business Knowledge | Knows Business |

---

# Repository vs Database Layer

Database Layer

↓

Creates Connection

Repository

↓

Uses Connection

↓

Executes SQL

Example

```
Database

↓

Session

↓

Repository

↓

SELECT
```

---

# One Repository Per Entity

Good

```
CustomerRepository

ProductRepository

OrderRepository
```

Avoid

```
DatabaseRepository
```

Large repositories become difficult to maintain.

---

# One Service Can Call Many Repositories

Example

Order Service

↓

Customer Repository

↓

Inventory Repository

↓

Payment Repository

↓

Shipment Repository

This is very common in enterprise applications.

---

# Error Handling

Repository

↓

Database Error

↓

Raise Exception

↓

Service

↓

Business Decision

↓

Router

↓

HTTP Response

Each layer handles only its own responsibility.

---

# SQL in Repository

Good

```python
SELECT *

FROM customers

WHERE customer_id = ...
```

Bad

Router

↓

SQL

Or

Service

↓

SQL

SQL belongs only inside Repository.

---

# Why This Pattern Matters

Benefits

- Cleaner Code
- Reusable Queries
- Easier Testing
- Easier Maintenance
- Better Separation of Concerns

---

# Enterprise Example

Netflix

Movie Service

↓

Movie Repository

↓

PostgreSQL

Amazon

Order Service

↓

Order Repository

↓

Aurora Database

Same pattern.

---

# Best Practices

- One Repository per business entity
- Keep methods small
- One responsibility per method
- Return domain objects
- Handle database exceptions properly

---

# Common Mistakes

❌ Business logic inside Repository

❌ HTTP responses inside Repository

❌ Calling APIs from Repository

❌ Repository calling Service

❌ One Repository for the entire application

---

# Interview Questions

### What is the Repository Pattern?

A design pattern that separates database operations from business logic.

---

### Why use a Repository?

To isolate SQL from business logic, making the application easier to maintain and test.

---

### Should SQL exist in the Service Layer?

No.

It belongs in the Repository.

---

### Can multiple Services use one Repository?

Yes.

For example

Customer Service

Order Service

Loyalty Service

may all use

Customer Repository.

---

### Can Repository call another Repository?

Usually no.

If coordination between multiple repositories is required,

the Service Layer should do it.

---

# Where We Used This in ShopSphere

Customer API

↓

Customer Service

↓

Customer Repository

↓

PostgreSQL

Future

Product Repository

Order Repository

Inventory Repository

Payment Repository

---

# Enterprise Perspective

In enterprise applications, Repository implementations may change without affecting business logic.

Example

Today

```
Customer Repository

↓

PostgreSQL
```

Tomorrow

```
Customer Repository

↓

Oracle
```

or

```
Customer Repository

↓

Snowflake
```

or

```
Customer Repository

↓

REST API
```

The Service Layer doesn't care.

It simply calls

```python
repository.get_customer()
```

This abstraction makes applications much easier to migrate and maintain.

---

# Revision Notes

✅ Repository = Database Layer

✅ Service = Business Layer

✅ Repository executes SQL

✅ Repository never contains business logic

✅ One Repository per entity

---

# Exercises

1. Design a ProductRepository.

2. Write five methods for OrderRepository.

3. Explain why SQL should not be written in the Service Layer.

4. Can a Repository send emails? Why?

5. Explain the complete request flow from Router to Repository.

---

# Prerequisites

- FastAPI
- Pydantic
- Service Layer

---

# Next Chapter

➡️ 010-sqlalchemy.md