# 🏛️ Models Layer

The Models Layer contains the SQLAlchemy ORM models that represent the application's database tables.

Each model maps a Python class to a PostgreSQL table, allowing developers to work with Python objects instead of writing SQL for every operation.

> **Note:**  
> In the current version of ShopSphere, we are using raw SQL to understand database design and SQL fundamentals. SQLAlchemy Models will be introduced in a later phase of the project.

---

# 📌 Responsibilities

The Models Layer is responsible for:

- Representing database tables as Python classes
- Defining table columns
- Defining relationships between tables
- Mapping Python objects to database records
- Supporting ORM-based database operations

---

# ❌ The Models Layer SHOULD NOT

- Contain Business Logic
- Execute SQL Queries
- Handle HTTP Requests
- Validate API Requests
- Call External APIs

Models should only describe how data is stored.

---

# 📁 Current Structure

```
models/

(Currently Empty)
```

Future structure:

```
models/

├── customer.py
├── product.py
├── order.py
├── inventory.py
├── payment.py
└── shipment.py
```

Each model represents one database table.

---

# 🔄 Position in the Architecture

```
Browser

    │

    ▼

API Layer

    │

    ▼

Service Layer

    │

    ▼

Repository Layer

    │

    ▼

SQLAlchemy Models

    │

    ▼

PostgreSQL
```

The Repository Layer uses Models to interact with the database.

---

# 🏗️ Why Do We Need Models?

Without ORM:

```python
cursor.execute("""
INSERT INTO customers ...
""")
```

With ORM:

```python
customer = Customer(
    first_name="Maneesh",
    email="maneesh@gmail.com"
)

session.add(customer)
session.commit()
```

The ORM generates SQL automatically.

---

# 🛍️ Real-World Analogy

Imagine an employee ID card.

```
Employee

↓

ID Card

↓

HR Database
```

The ID card represents the employee.

Similarly,

A Model represents a database table.

The model itself is **not** the database.

It is simply a structured representation of it.

---

# 💻 Example

Future Customer Model

```python
class Customer(Base):

    __tablename__ = "customers"

    customer_id = Column(UUID)

    first_name = Column(String)

    email = Column(String)
```

This class represents the `customers` table.

---

# 📦 Model Relationships

Models can define relationships.

Example:

```
Customer

↓

Orders

↓

Order Items

↓

Products
```

Using SQLAlchemy:

```python
customer.orders
```

instead of manually writing JOIN queries.

---

# 🔄 SQL vs ORM

Raw SQL

```
SELECT *
FROM customers
WHERE customer_id = ...
```

ORM

```python
session.query(Customer).filter(...)
```

Both produce the same result.

The difference is how the query is written.

---

# 🧠 Why Are We Learning SQL First?

Understanding SQL is essential for Data Engineers.

By learning SQL before ORM, we gain:

- Better database knowledge
- Better query optimization skills
- Easier debugging
- Stronger interview preparation

Once the fundamentals are clear, ORM becomes much easier to understand.

---

# 📖 Typical Model Contents

A Model usually contains:

- Table Name
- Primary Key
- Columns
- Foreign Keys
- Relationships
- Constraints

Nothing more.

Business logic should remain in the Service Layer.

---

# ✅ Best Practices

- One Model per table
- Keep models simple
- Use meaningful column names
- Define relationships clearly
- Avoid business logic inside models

---

# ❌ Common Mistakes

- Writing business logic inside models
- Returning models directly to APIs
- Mixing API validation with ORM models
- Creating very large models with unrelated functionality

---

# 🔗 Related Layers

### ⬆ Used By

- Repository Layer

### ⬇ Maps To

- PostgreSQL Tables

Models act as the bridge between Python objects and database tables.

---

# 💼 Interview Questions

### What is an ORM?

An Object Relational Mapper (ORM) maps database tables to programming language objects, allowing developers to interact with the database using code instead of writing SQL for every operation.

---

### What is a SQLAlchemy Model?

A SQLAlchemy Model is a Python class that represents a database table.

---

### Should Models contain business logic?

No.

Models should only represent data structures.

Business logic belongs in the Service Layer.

---

### Why are we not using Models yet?

This project starts with raw SQL to build a strong understanding of relational databases and SQL. SQLAlchemy Models will be introduced later to demonstrate ORM concepts.

---

# 🛍️ ShopSphere Roadmap

Current Phase

```
Repository

↓

Raw SQL

↓

PostgreSQL
```

Future Phase

```
Repository

↓

SQLAlchemy Models

↓

PostgreSQL
```

This progression helps us understand both approaches used in enterprise applications.

---

# 🎯 Key Takeaway

Models represent database tables as Python classes.

They simplify database interaction through ORM but are not a replacement for understanding SQL.

A strong backend engineer should understand both raw SQL and ORM-based development.

---

# 🧠 Interview Summary

✅ Models represent database tables.

✅ Models are not API Schemas.

✅ Models should not contain business logic.

Most Asked Question:

**"What is the difference between a Pydantic Schema and a SQLAlchemy Model?"**

Answer:

A Pydantic Schema defines the API contract and validates incoming/outgoing data.

A SQLAlchemy Model represents the database table and is used for persistence.

---

# 📚 Further Reading

See:

learning/

- 005-pydantic.md
- 008-sqlalchemy.md
- 011-orm-vs-sql.md (Coming Soon)