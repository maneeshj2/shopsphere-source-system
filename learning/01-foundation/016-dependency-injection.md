# 🔌 Dependency Injection (DI)

## Goal

Understand what Dependency Injection (DI) is, why frameworks like FastAPI use it, and how it helps build clean, maintainable, and testable applications.

This chapter explains Dependency Injection using the ShopSphere project.

---

# What is Dependency Injection?

Dependency Injection is a design pattern where an object receives the things it needs (its dependencies) instead of creating them itself.

Instead of

```
Customer Service

↓

Create Database Session
```

We do

```
Database Session

↓

Injected

↓

Customer Service
```

FastAPI provides this feature using

```python
Depends()
```

---

# Why Do We Need Dependency Injection?

Imagine every API creates its own database connection.

```python
@router.post("/")
def create_customer():

    db = SessionLocal()

    ...
```

Every API repeats the same code.

Now imagine 100 APIs.

You'll have

```
SessionLocal()

SessionLocal()

SessionLocal()

SessionLocal()
```

everywhere.

Not ideal.

---

# Better Approach

Create the session once.

FastAPI injects it wherever needed.

```
FastAPI

↓

Create Session

↓

Inject Session

↓

API

↓

Close Session
```

Cleaner.

Reusable.

Safer.

---

# Real World Analogy

Imagine a restaurant.

Without DI

Chef

↓

Walks to storage

↓

Gets vegetables

↓

Returns

↓

Cooks

With DI

Kitchen Staff

↓

Brings vegetables

↓

Chef

↓

Starts cooking immediately

The chef doesn't care where the vegetables came from.

Similarly,

Your code shouldn't care where the database session came from.

---

# What is a Dependency?

Anything your code needs.

Examples

```
Database Session

Current User

JWT Verification

Logger

Configuration

Redis Client

S3 Client
```

All of these are dependencies.

---

# FastAPI Example

```python
from fastapi import Depends

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()
```

API

```python
@router.post("/")

def create_customer(
    db = Depends(get_db)
):
```

FastAPI automatically

- Calls get_db()
- Creates Session
- Passes Session
- Closes Session

---

# Internal Working

```
HTTP Request

↓

FastAPI

↓

Depends(get_db)

↓

Create Session

↓

Inject into Function

↓

Execute API

↓

Close Session
```

Your API never creates the session itself.

---

# ShopSphere Example

Customer Registration

```
POST /customers

↓

Depends(get_db)

↓

Repository

↓

Database

↓

Response
```

---

# Multiple Dependencies

An API can have many dependencies.

Example

```python
def create_order(

    db = Depends(get_db),

    user = Depends(get_current_user)

):
```

FastAPI injects both.

```
Database Session

+

Current User

↓

API
```

---

# Dependency Graph

Imagine

```
API

↓

Current User

↓

JWT Verification

↓

Database Session
```

FastAPI automatically resolves the dependency graph.

---

# Dependency Reuse

One dependency

↓

Many APIs

Example

```
get_db()

↓

Customers

↓

Products

↓

Orders

↓

Payments
```

One implementation.

Used everywhere.

---

# Why is DI Useful?

Without DI

```
API

↓

Creates Everything
```

With DI

```
API

↓

Receives Everything
```

This makes code

- Cleaner
- Easier to Test
- Easier to Reuse

---

# Testing

Imagine testing

```
Customer Service
```

Instead of a real database

↓

Inject

```
Fake Database
```

This is one of the biggest advantages of Dependency Injection.

---

# Enterprise Perspective

Dependency Injection isn't unique to FastAPI.

Other frameworks use the same concept.

Spring Boot

↓

@Autowired

.NET

↓

Constructor Injection

Angular

↓

Dependency Injection

FastAPI

↓

Depends()

Different syntax.

Same idea.

---

# ShopSphere Dependencies

Current

```
Database Session
```

Future

```
Database Session

Current User

JWT

Configuration

Logger

Redis

S3

Snowflake Client
```

All will be injected.

---

# Best Practices

- Keep dependencies small
- Reuse dependencies
- Avoid creating dependencies inside business logic
- Close resources properly
- Use Depends() consistently

---

# Common Mistakes

❌ Creating database sessions manually everywhere

❌ Opening multiple sessions in one request

❌ Forgetting to close resources

❌ Mixing dependency creation with business logic

---

# Comparison

| Without DI | With DI |
|------------|---------|
| Create dependencies manually | Dependencies injected automatically |
| Duplicate code | Reusable code |
| Harder to test | Easier to test |
| Tight coupling | Loose coupling |

---

# Interview Questions

### What is Dependency Injection?

A design pattern where objects receive their dependencies instead of creating them directly.

---

### What is Depends() in FastAPI?

Depends() tells FastAPI to create or retrieve a dependency and inject it into the function automatically.

---

### Why is Dependency Injection useful?

It reduces code duplication, improves testability, promotes loose coupling, and makes applications easier to maintain.

---

### What are common FastAPI dependencies?

- Database Session
- Current User
- JWT Verification
- Configuration
- Logger

---

### Does Depends() only work with databases?

No.

It can inject any dependency, including authentication, configuration, cache clients, and external services.

---

# Where We Will Use This in ShopSphere

Today

```
Depends(get_db)
```

Soon

```
Depends(get_current_user)
```

Later

```
Depends(get_admin_user)

Depends(get_settings)

Depends(get_logger)
```

---

# Revision Notes

✅ Dependency = Something your code needs.

✅ Depends() injects dependencies.

✅ FastAPI manages the lifecycle.

✅ One dependency can be reused by many APIs.

✅ DI improves testing and maintainability.

---

# Exercises

1. Explain what a dependency is.

2. Why is creating SessionLocal() inside every API a bad idea?

3. Draw the lifecycle of Depends(get_db).

4. List five things that can be injected using Depends().

5. Explain Dependency Injection using a real-world analogy.

---

# Prerequisites

- FastAPI
- Database Sessions
- SQLAlchemy

---

# Next Chapter

➡️ 017-project-architecture.md