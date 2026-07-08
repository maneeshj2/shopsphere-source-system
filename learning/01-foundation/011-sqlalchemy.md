# 🏛️ SQLAlchemy Fundamentals

## Goal

Understand what SQLAlchemy is, why it is used, and how it helps Python applications interact with relational databases.

This chapter explains SQLAlchemy using the ShopSphere project and compares ORM-based development with raw SQL.

---

# What is SQLAlchemy?

SQLAlchemy is Python's most popular database toolkit and Object Relational Mapper (ORM).

It allows Python applications to communicate with relational databases without writing SQL for every operation.

Think of SQLAlchemy as a translator between Python objects and database tables.

---

# Why Do We Need SQLAlchemy?

Without SQLAlchemy

```
Python

↓

SQL Query

↓

PostgreSQL
```

Every operation requires SQL.

With SQLAlchemy

```
Python Object

↓

SQLAlchemy

↓

Generated SQL

↓

PostgreSQL
```

You work with Python objects.

SQLAlchemy generates SQL.

---

# What is an ORM?

ORM stands for

Object Relational Mapper

It maps

```
Python Class

↓

Database Table
```

and

```
Python Object

↓

Database Row
```

---

# Real World Analogy

Imagine travelling to Japan.

You speak English.

The shopkeeper speaks Japanese.

You need a translator.

```
You

↓

Translator

↓

Shopkeeper
```

SQLAlchemy is the translator.

```
Python

↓

SQLAlchemy

↓

PostgreSQL
```

---

# ShopSphere Today

Current

```
Repository

↓

Raw SQL

↓

PostgreSQL
```

Future

```
Repository

↓

SQLAlchemy

↓

PostgreSQL
```

Both approaches are valid.

---

# SQL vs ORM

Raw SQL

```sql
SELECT *

FROM customers

WHERE email='abc@gmail.com';
```

SQLAlchemy

```python
session.query(Customer).filter(
    Customer.email == "abc@gmail.com"
).first()
```

Both execute SQL.

Only the syntax changes.

---

# Model

Every table becomes a Python class.

Example

```python
class Customer(Base):

    __tablename__ = "customers"
```

Think of

```
Customer

↓

customers table
```

---

# Columns

```python
customer_id = Column(UUID)

email = Column(String)

created_at = Column(DateTime)
```

Each column maps to a database column.

---

# Creating an Object

```python
customer = Customer(
    first_name="Maneesh",
    email="maneesh@gmail.com"
)
```

This creates a Python object.

Nothing is stored yet.

---

# Saving Data

```python
session.add(customer)

session.commit()
```

Meaning

```
Create Object

↓

Track Object

↓

Commit

↓

INSERT executed
```

---

# Querying Data

```python
customer = session.query(Customer).first()
```

Equivalent SQL

```sql
SELECT *

FROM customers

LIMIT 1;
```

---

# Updating Data

```python
customer.phone = "9999999999"

session.commit()
```

Equivalent SQL

```sql
UPDATE customers

SET phone='9999999999'
```

---

# Deleting Data

```python
session.delete(customer)

session.commit()
```

Equivalent SQL

```sql
DELETE

FROM customers
```

In ShopSphere

↓

Soft Delete instead.

---

# Relationships

Customer

↓

Orders

↓

Order Items

↓

Products

SQLAlchemy allows

```python
customer.orders
```

instead of writing JOINs manually.

---

# Session

Every ORM operation uses a Session.

```
Customer Object

↓

Session

↓

SQL Generated

↓

Database
```

No Session

↓

No Database Operations.

---

# Internal Working

```
Python Object

↓

SQLAlchemy

↓

SQL Generated

↓

PostgreSQL

↓

Rows Returned

↓

Python Objects
```

---

# SQLAlchemy Components

Engine

↓

Connection

↓

Session

↓

Models

↓

Queries

Everything works together.

---

# Why Learn Raw SQL First?

Because

Understanding SQL

↓

Understanding ORM

↓

Better Debugging

↓

Better Performance

Many developers know SQLAlchemy.

Few understand the SQL it generates.

Enterprise engineers should know both.

---

# SQLAlchemy in ShopSphere

Future

```
CustomerRepository

↓

Customer Model

↓

Session

↓

PostgreSQL
```

Instead of

```
Repository

↓

Raw SQL
```

---

# ORM Advantages

- Less Boilerplate
- Object-Oriented
- Easier Maintenance
- Database Agnostic
- Relationship Support
- Automatic Mapping

---

# ORM Disadvantages

- Can generate inefficient SQL
- Harder to optimize complex queries
- Learning curve
- May hide database behavior

For complex reporting,

raw SQL is often better.

---

# When to Use ORM

Good For

- CRUD APIs
- Small to Medium Queries
- Business Applications

Not Ideal For

- Complex Analytics
- Large ETL Jobs
- Heavy Reporting
- Warehouse Queries

---

# Comparison

| Raw SQL | SQLAlchemy |
|----------|------------|
| Manual SQL | Python Objects |
| More Control | Faster Development |
| Better for Analytics | Better for CRUD |
| Harder to Maintain | Easier to Read |

---

# Best Practices

- Keep Models simple
- Use Sessions properly
- Avoid loading unnecessary data
- Understand generated SQL
- Use raw SQL when appropriate

---

# Common Mistakes

❌ Not calling commit()

❌ Loading entire tables unnecessarily

❌ Ignoring generated SQL

❌ Mixing ORM and business logic

---

# Interview Questions

### What is SQLAlchemy?

A Python database toolkit and ORM.

---

### What is an ORM?

A framework that maps database tables to programming language objects.

---

### Why use SQLAlchemy?

To simplify database interaction using Python objects instead of writing SQL for every operation.

---

### Is SQLAlchemy a replacement for SQL?

No.

SQLAlchemy generates SQL.

Understanding SQL is still essential.

---

### When would you prefer raw SQL?

Complex reporting

Analytics

Warehouse queries

Performance-critical operations

---

# Where We Will Use This in ShopSphere

Future

```
CustomerRepository

↓

Customer Model

↓

Session

↓

PostgreSQL
```

Current

↓

Raw SQL

Later

↓

ORM

---

# Snowflake Connection

As Data Engineers,

we usually write SQL directly.

dbt

↓

SQL

Snowflake

Backend applications,

however,

usually prefer ORMs because

they perform many CRUD operations.

Understanding both approaches makes you much stronger.

---

# Revision Notes

✅ ORM maps objects to tables.

✅ SQLAlchemy generates SQL.

✅ Session executes operations.

✅ commit() persists changes.

✅ Raw SQL is still important.

---

# Exercises

1. Create a Product model.

2. Insert a Product using SQLAlchemy.

3. Query all Products.

4. Update Product price.

5. Explain the difference between ORM and raw SQL.

---

# Prerequisites

- Python OOP
- Database Sessions
- Repository Pattern

---

# Next Chapter

➡️ 012-authentication.md