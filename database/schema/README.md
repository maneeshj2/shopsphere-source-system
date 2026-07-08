# 🏗️ Database Schema

The `schema` folder contains all Data Definition Language (DDL) scripts used to create the ShopSphere database structure.

Each SQL file defines exactly one database object, such as a table, view, or index.

The objective is to keep database objects modular, maintainable, and easy to version control.

---

# 📌 Responsibilities

The Schema Layer is responsible for:

- Creating Tables
- Creating Constraints
- Creating Indexes
- Creating Views
- Defining Relationships
- Defining Default Values
- Defining Data Types

---

# ❌ The Schema Layer SHOULD NOT

- Insert Business Data
- Update Existing Records
- Delete Records
- Contain Business Logic
- Execute ETL Processes

Those responsibilities belong to Seed Scripts or the Application Layer.

---

# 📁 Folder Structure

```
schema/

├── customers.sql
├── products.sql
├── categories.sql
├── inventory.sql
├── orders.sql
├── order_items.sql
├── payments.sql
├── shipments.sql
└── suppliers.sql
```

Each file creates exactly one business entity.

---

# 📖 SQL File Standard

Each SQL file follows the same structure.

```
Table Header

↓

CREATE TABLE

↓

Constraints

↓

Indexes (Future)

↓

Comments (Optional)
```

Example:

```sql
-- ==========================================
-- Table : customers
-- Purpose : Stores customer information
-- ==========================================

CREATE TABLE retail.customers
(
    ...
);
```

---

# 🏛️ Naming Convention

## Tables

Use plural nouns.

✅

```
customers

products

orders

payments
```

Avoid

```
customer_tbl

tbl_customer

customer_master
```

---

## Columns

Use snake_case.

Example

```
customer_id

first_name

phone_number

created_at
```

Avoid

```
CustomerID

CustomerName

PhoneNumber
```

---

## Primary Keys

Always use

```
<table_name>_id
```

Example

```
customer_id

product_id

order_id
```

Benefits:

- Self-documenting
- Easier JOINs
- Better readability

---

## Foreign Keys

Always reference the primary key name.

Example

```
customer_id

product_id

order_id
```

Never use generic names like

```
id

cust

prodid
```

---

# 📦 Data Types

| Data | Type |
|------|------|
| UUID | UUID |
| Name | VARCHAR(100) |
| Email | VARCHAR(255) |
| Phone | VARCHAR(20) |
| Description | TEXT |
| Date | DATE |
| Timestamp | TIMESTAMP |
| Price | NUMERIC(10,2) |
| Quantity | INTEGER |
| Boolean | BOOLEAN |

Use the smallest appropriate data type without sacrificing future flexibility.

---

# 🔑 Primary Key Strategy

ShopSphere uses UUIDs.

Example

```sql
customer_id UUID PRIMARY KEY
DEFAULT gen_random_uuid()
```

Benefits

- Globally Unique
- Difficult to Guess
- Better for Distributed Systems

---

# 🔗 Foreign Key Strategy

Example

```
orders

↓

customer_id

↓

customers.customer_id
```

Always enforce referential integrity unless there is a strong business reason not to.

---

# 🧾 Audit Columns

Every transactional table should contain:

```sql
created_at

updated_at

created_by

updated_by
```

Soft delete support:

```sql
is_deleted

deleted_at
```

These columns provide traceability and support operational requirements.

---

# 🗑️ Soft Delete Strategy

Records are not physically deleted.

Instead:

```sql
is_deleted = TRUE

deleted_at = CURRENT_TIMESTAMP
```

Benefits

- Auditability
- Recovery
- Historical Analysis

---

# 📈 Indexing Strategy

Indexes will be added after the application is functional.

Typical indexes:

```
email

customer_id

order_date

product_id
```

Avoid creating unnecessary indexes during early development.

---

# 🧩 Constraints

Use constraints whenever possible.

Examples

```
PRIMARY KEY

FOREIGN KEY

UNIQUE

NOT NULL

CHECK
```

Database constraints protect data integrity even if the application has bugs.

---

# 🔄 Schema Evolution

When changing a table:

❌ Never edit production tables directly.

Instead:

- Create a migration
- Review changes
- Test changes
- Deploy safely

For this learning project, we may recreate the database frequently, but production systems use migrations.

---

# 🛍️ ShopSphere Standards

Every table should include:

- UUID Primary Key
- Audit Columns
- Soft Delete Columns
- Meaningful Constraints
- Descriptive Column Names

These standards apply across every module.

---

# 🧠 Design Philosophy

The database should enforce structural integrity.

The application should enforce business rules.

Examples

Database

```
email UNIQUE
```

Application

```
Email domain allowed?
```

Database

```
price NUMERIC(10,2)
```

Application

```
Can this customer receive a discount?
```

Each layer has its own responsibility.

---

# ✅ Best Practices

- One table per file
- Use snake_case
- Use UUID primary keys
- Add audit columns
- Define constraints
- Keep SQL readable
- Use comments for complex logic

---

# ❌ Common Mistakes

- Using SELECT * in production scripts
- Mixing DDL and DML
- Missing constraints
- Inconsistent naming
- No audit columns
- No foreign keys

---

# 🔗 Related Layers

### Used By

- init.sql
- Repository Layer

### Creates

- PostgreSQL Tables
- Constraints
- Indexes

---

# 💼 Interview Questions

### Why create one table per SQL file?

It improves readability, modularity, version control, and makes reviews easier.

---

### Why use UUID instead of SERIAL?

UUIDs are globally unique, more secure, and better suited for distributed systems.

---

### Why add audit columns?

Audit columns provide traceability, support debugging, and enable historical reporting.

---

### Why use database constraints if the application already validates data?

Because the database is the final line of defense. Constraints protect data integrity even if the application contains bugs.

---

# 🛍️ ShopSphere Example

```
customers.sql

↓

Creates

retail.customers

↓

Repository

↓

Customer Service

↓

API
```

Everything starts with a well-designed table.

---

# 🎯 Key Takeaway

The `schema` folder defines the structure of the ShopSphere database.

It establishes the rules for how data is stored, ensuring consistency, integrity, and maintainability across the application.

---

# 🧠 Interview Summary

✅ One table per SQL file.

✅ UUID primary keys.

✅ Audit columns.

✅ Soft delete strategy.

✅ Database constraints complement application validation.

Most Asked Question:

**"What standards do you follow while designing database tables?"**

A strong answer should include:

- Consistent naming conventions
- Appropriate data types
- Primary and foreign keys
- Constraints
- Audit columns
- Soft deletes
- Indexing strategy
- Version-controlled DDL scripts

---

# 📚 Further Reading

See:

learning/

- Database Design
- PostgreSQL
- Normalization
- Indexing
- Constraints
- Primary Keys