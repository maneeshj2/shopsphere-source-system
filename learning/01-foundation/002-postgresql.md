# 🐘 PostgreSQL Fundamentals

## Goal

Understand PostgreSQL from a Backend and Data Engineering perspective and learn how it acts as the transactional (OLTP) database for ShopSphere.

---

# What is PostgreSQL?

PostgreSQL is an open-source Relational Database Management System (RDBMS).

It stores application data in structured tables and provides ACID-compliant transactions, indexing, constraints, and advanced SQL capabilities.

It is one of the most widely used enterprise databases.

---

# Why PostgreSQL?

Compared to MySQL:

✅ Better Standards Compliance

✅ Better JSON Support

✅ Better Indexing Options

✅ Better Extensions

✅ Excellent Performance

✅ Enterprise Features

---

# What is an OLTP Database?

OLTP stands for

Online Transaction Processing

These databases are optimized for

- Fast Inserts
- Fast Updates
- Fast Deletes
- Small Queries
- Thousands of Concurrent Users

Example:

```
Customer Registration

↓

Insert One Row

↓

Completed in milliseconds
```

ShopSphere is an OLTP application.

---

# OLTP vs OLAP

| OLTP | OLAP |
|------|------|
| PostgreSQL | Snowflake |
| Insert Heavy | Read Heavy |
| Normalized | Denormalized |
| Small Queries | Large Queries |
| Application Users | Business Users |
| Real-Time | Analytics |

Example

```
Customer buys a product

↓

PostgreSQL

↓

API

↓

Snowflake

↓

Dashboard
```

---

# PostgreSQL Architecture

```
Application

↓

Connection

↓

PostgreSQL Server

↓

Database

↓

Schema

↓

Tables

↓

Rows
```

---

# ShopSphere Database

```
shopsphere

↓

retail

↓

customers

products

orders

payments
```

---

# Database

A Database is the top-level container.

Example

```
shopsphere
```

---

# Schema

A Schema groups related database objects.

Example

```
retail
```

Think of a Schema as a folder.

---

# Table

A table stores records.

Example

```
customers
```

---

# Row

A single customer.

```
Customer

↓

One Row
```

---

# Column

One attribute.

Example

```
first_name

email

phone_number
```

---

# Primary Key

Uniquely identifies a row.

Example

```
customer_id
```

Properties

- Unique
- Not Null
- Immutable

---

# Foreign Key

Connects two tables.

Example

```
orders

↓

customer_id

↓

customers.customer_id
```

This creates relationships.

---

# Constraints

Constraints protect data integrity.

Examples

```
PRIMARY KEY

FOREIGN KEY

UNIQUE

CHECK

NOT NULL
```

The database rejects invalid data automatically.

---

# Index

Indexes improve query performance.

Without Index

```
Search Entire Table
```

With Index

```
Jump Directly to Record
```

Example

```
email

customer_id
```

---

# UUID

ShopSphere uses UUID instead of SERIAL.

Benefits

- Globally Unique

- Secure

- Better for Distributed Systems

---

# Audit Columns

Every transactional table should contain

```
created_at

updated_at

created_by

updated_by
```

These support auditing and troubleshooting.

---

# Soft Delete

Instead of deleting

```
DELETE
```

we update

```
is_deleted = TRUE
```

Benefits

- Recovery

- History

- Audit

---

# Transactions

A Transaction ensures that either

Everything succeeds

or

Nothing changes.

Example

```
Create Order

↓

Reduce Inventory

↓

Create Payment

↓

Commit
```

If payment fails,

Everything rolls back.

---

# ACID Properties

A

Atomicity

All or Nothing

---

C

Consistency

Valid State

---

I

Isolation

Concurrent Transactions

---

D

Durability

Committed Data Never Lost

---

# PostgreSQL Extensions

Extensions add extra functionality.

Example

```
pgcrypto
```

Used in ShopSphere for

```
gen_random_uuid()
```

---

# Common SQL Commands

Create Table

```sql
CREATE TABLE
```

Insert

```sql
INSERT
```

Read

```sql
SELECT
```

Update

```sql
UPDATE
```

Delete

```sql
DELETE
```

---

# Common psql Commands

List Databases

```sql
\l
```

Connect Database

```sql
\c shopsphere
```

List Schemas

```sql
\dn
```

List Tables

```sql
\dt retail.*
```

Describe Table

```sql
\d retail.customers
```

Quit

```sql
\q
```

---

# How ShopSphere Uses PostgreSQL

```
Browser

↓

POST /customers

↓

Service

↓

Repository

↓

INSERT

↓

PostgreSQL

↓

customer_id

↓

API Response
```

---

# PostgreSQL in Data Engineering

Source System

↓

Extraction

↓

JSON

↓

S3 / MinIO

↓

Snowflake RAW

↓

dbt

↓

MART

PostgreSQL is the operational source system.

Snowflake is the analytical system.

---

# Best Practices

- Use UUID Primary Keys

- Add Constraints

- Use Audit Columns

- Normalize Transaction Tables

- Index Frequently Queried Columns

- Use Transactions

---

# Common Mistakes

❌ Using VARCHAR for everything

❌ Missing Constraints

❌ No Primary Keys

❌ Hard Deletes

❌ No Indexes

---

# Interview Questions

### What is PostgreSQL?

An enterprise-grade relational database.

---

### Difference between PostgreSQL and Snowflake?

PostgreSQL is OLTP.

Snowflake is OLAP.

---

### What is ACID?

Atomicity

Consistency

Isolation

Durability

---

### Why UUID?

Globally unique identifiers suitable for distributed systems.

---

### What is a Transaction?

A group of operations executed as one unit of work.

---

### Difference between DELETE and Soft Delete?

DELETE removes data.

Soft Delete marks data as inactive while preserving history.

---

# Revision Notes

✅ PostgreSQL is our OLTP database.

✅ Tables belong to Schemas.

✅ Schemas belong to Databases.

✅ UUID is our PK.

✅ Constraints protect data.

✅ Transactions guarantee consistency.

---

# ShopSphere Progress

✔ Docker

✔ PostgreSQL

✔ FastAPI

⏳ Customer Registration

⏳ Repository Layer

⏳ Database Integration

---

# Next Topic

➡️ 003-python-fundamentals.md