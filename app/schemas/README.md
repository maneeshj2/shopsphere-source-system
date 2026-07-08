# 📑 Schemas Layer

The Schemas Layer defines the structure of data entering and leaving the application.

Schemas act as the contract between the client and the backend, ensuring that only valid and expected data is accepted or returned.

ShopSphere uses **Pydantic** to define schemas and automatically validate incoming and outgoing data.

---

# 📌 Responsibilities

The Schemas Layer is responsible for:

- Validating incoming requests
- Defining API response structures
- Data type validation
- Required field validation
- Field constraints (length, format, etc.)
- Automatic serialization and deserialization

---

# ❌ The Schemas Layer SHOULD NOT

- Execute SQL
- Contain Business Logic
- Connect to PostgreSQL
- Perform Business Validations
- Handle HTTP Requests

Those responsibilities belong to other layers.

---

# 📁 Current Files

```
schemas/

└── customer.py
```

Future structure:

```
schemas/

├── customer.py
├── product.py
├── order.py
├── inventory.py
├── payment.py
└── shipment.py
```

Each schema file represents one business domain.

---

# 🔄 Position in the Architecture

```
Browser

    │

    ▼

Request Schema

    │

    ▼

API Layer

    │

    ▼

Service Layer

    │

    ▼

Repository

    │

    ▼

PostgreSQL

    │

    ▼

Response Schema

    │

    ▼

Browser
```

Schemas sit at the boundary between the client and the application.

---

# 🏗️ Why Do We Need Schemas?

Imagine a client sends:

```json
{
    "email":"abcgmail",
    "age":"twenty"
}
```

Without Schemas:

The application must manually validate every field.

With Schemas:

Pydantic automatically validates:

- Required fields
- Data types
- Email format
- String lengths
- Date formats

before our code executes.

---

# 🛍️ Real-World Analogy

Imagine airport security.

```
Passenger

↓

Security Check

↓

Airport
```

Only passengers with valid documents can enter.

Similarly,

Only valid requests enter the application.

Invalid requests are rejected immediately.

---

# 💻 Example

```python
class CustomerCreateRequest(BaseModel):

    first_name: str

    email: EmailStr

    password: str
```

Pydantic automatically validates:

✅ Email Format

✅ Required Fields

✅ Data Types

before the Router executes.

---

# 📦 Types of Schemas

Typically, every entity has multiple schemas.

Example:

```
CustomerCreateRequest

CustomerUpdateRequest

CustomerResponse

CustomerListResponse
```

Each schema serves a different purpose.

---

# 🛒 Why Request and Response Schemas are Different

Customer Request

```json
{
    "email":"maneesh@gmail.com",
    "password":"Password@123"
}
```

Customer Response

```json
{
    "customer_id":"550e...",
    "email":"maneesh@gmail.com",
    "created_at":"2026-07-09T10:30:00"
}
```

Notice:

The request contains:

```
password
```

The response never returns:

```
password

password_hash
```

This improves security and keeps the API contract clean.

---

# 🔄 Request Lifecycle

```
Client

↓

Request Schema

↓

Validation

↓

Router

↓

Service

↓

Repository

↓

Database

↓

Response Schema

↓

Client
```

Every request passes through a Schema before entering the application.

---

# 📖 Common Pydantic Features

```
BaseModel

Field()

EmailStr

date

datetime

Optional

list

dict

Literal

Enum
```

We'll gradually use these throughout the project.

---

# 📚 Request vs Database Table

These are NOT the same.

Example

Request

```
password
```

Database

```
password_hash
```

Request

```
No customer_id
```

Database

```
customer_id UUID
```

Request

```
No created_at
```

Database

```
created_at TIMESTAMP
```

The Service Layer transforms request data into database data.

---

# 🧠 Why Not Use Database Tables Directly?

Database tables contain:

- Audit Columns
- Internal Flags
- Password Hashes
- Soft Delete Indicators
- System Metadata

Clients should never see or provide these values.

Schemas expose only what clients are allowed to send or receive.

---

# ✅ Best Practices

- Separate Request and Response Schemas
- Use meaningful class names
- Validate data as early as possible
- Never expose sensitive fields
- Keep Schemas focused on API contracts

---

# ❌ Common Mistakes

- Returning database models directly
- Using one schema for everything
- Exposing password hashes
- Putting business logic inside schemas
- Using schemas for database operations

---

# 🔗 Related Layers

### ⬆ Used By

- API Layer

### ⬇ Used By

- Service Layer

Schemas are the bridge between external clients and internal business logic.

---

# 💼 Interview Questions

### What is a Pydantic Schema?

A Pydantic Schema defines the structure and validation rules for incoming and outgoing API data.

---

### Why separate Request and Response Schemas?

To avoid exposing sensitive or internal fields and to keep API contracts independent of database design.

---

### Are Schemas the same as Database Tables?

No.

Schemas represent API contracts.

Database tables represent data storage.

They often have different fields and responsibilities.

---

### Why not use SQLAlchemy Models as API Schemas?

Keeping them separate decouples the API from the database, allowing each to evolve independently.

---

# 🛍️ ShopSphere Example

Customer Registration

Client Sends

```
first_name

email

password
```

↓

Schema validates input

↓

Service hashes password

↓

Repository stores

```
password_hash
```

↓

Response Schema returns

```
customer_id

message
```

The client never sees the internal database structure.

---

# 🎯 Key Takeaway

Schemas define the API contract.

They ensure that incoming requests are valid and outgoing responses expose only the appropriate information.

A well-designed Schema Layer keeps the application secure, consistent, and easy to maintain.

---

# 🧠 Interview Summary

✅ Schemas validate API data.

✅ Request and Response Schemas should be separate.

✅ Schemas are API contracts, not database tables.

Most Asked Question:

**"Why use Pydantic Schemas when we already have SQLAlchemy Models?"**

Answer:

Schemas represent API contracts.

Models represent database structure.

Keeping them separate provides better security, flexibility, and maintainability.

---

# 📚 Further Reading

See:

learning/

- 005-pydantic.md
- 004-rest-api.md
- 007-service-layer.md