# 🧠 Service Layer

The Service Layer is the brain of the application.

It contains all business logic and business rules. The Service Layer sits between the API Layer and the Repository Layer, ensuring that requests are validated, processed, and transformed before data is stored or retrieved from the database.

---

# 📌 Responsibilities

The Service Layer is responsible for:

- Implementing Business Logic
- Applying Business Rules
- Validating Business Conditions
- Transforming Data
- Calling one or more Repositories
- Coordinating multiple operations
- Returning business objects to the API Layer

---

# ❌ The Service Layer SHOULD NOT

- Receive HTTP Requests
- Return HTTP Responses
- Execute Raw SQL
- Manage Database Connections

Those responsibilities belong to the API Layer and Repository Layer.

---

# 📁 Current Services

```
customer_service.py
```

Future services:

```
services/

├── customer_service.py
├── product_service.py
├── order_service.py
├── inventory_service.py
├── payment_service.py
└── shipment_service.py
```

Each service represents one business domain.

---

# 🔄 Position in the Architecture

```
Browser

    │

    ▼

API Router

    │

    ▼

Service Layer

    │

    ▼

Repository Layer

    │

    ▼

PostgreSQL
```

The Service Layer acts as the bridge between the API and the database.

---

# 🛍️ Real-World Analogy

Imagine a restaurant.

```
Customer

↓

Waiter

↓

Chef

↓

Kitchen

↓

Chef

↓

Waiter

↓

Customer
```

| Restaurant | ShopSphere |
|------------|------------|
| Customer | Browser / Swagger |
| Waiter | API Router |
| Chef | Service Layer |
| Kitchen | PostgreSQL |

The waiter never cooks.

Similarly, the Router never contains business logic.

The Chef decides how the food should be prepared.

Similarly, the Service Layer decides how the business process should work.

---

# 🛒 Example

Customer Registration

Request:

```json
{
    "email":"maneesh@gmail.com",
    "password":"Password@123"
}
```

The Service Layer may perform:

- Check if email already exists
- Validate password policy
- Hash password
- Generate customer UUID (if application-generated)
- Create customer
- Send welcome email
- Award loyalty points
- Return response

Notice that multiple operations happen before saving data.

---

# 📦 Example Flow

```
POST /customers

        │

        ▼

Customer Router

        │

        ▼

Customer Service

        │

        ├── Validate Email

        ├── Hash Password

        ├── Call Repository

        └── Return Response
```

---

# 🧩 Why Do We Need a Service Layer?

Without a Service Layer:

```
Router

↓

Validation

↓

SQL

↓

Email

↓

Calculations

↓

Response
```

The Router becomes very large and difficult to maintain.

With a Service Layer:

```
Router

↓

Service

↓

Repository

↓

Database
```

Each layer has one responsibility.

---

# 💻 Example

Good:

```python
def create_customer(customer):

    validate_customer(customer)

    hashed_password = hash_password(customer.password)

    repository.create_customer(customer, hashed_password)

    return success_response
```

Bad:

```python
def create_customer():

    if ...

    execute_sql()

    send_email()

    update_inventory()

    call_payment_gateway()
```

Everything mixed together.

---

# 🔄 One Service Can Call Multiple Repositories

Example:

Order Creation

```
Order Service

        │

        ├── Customer Repository

        ├── Product Repository

        ├── Inventory Repository

        ├── Payment Repository

        └── Shipment Repository
```

The Service Layer coordinates the complete business transaction.

---

# ✅ Best Practices

- One Service per business domain
- Keep functions focused
- Business logic belongs here
- Call repositories instead of writing SQL
- Return business objects, not HTTP responses
- Reuse common helper functions

---

# ❌ Common Mistakes

- Writing SQL in Services
- Returning JSON responses directly
- Accessing FastAPI Request objects
- Mixing business logic with HTTP logic
- Making Services depend on Routers

---

# 📖 Naming Convention

Service files should be named after the business domain.

Examples:

```
customer_service.py

product_service.py

order_service.py
```

Avoid:

```
customer_logic.py

customer_handler.py

service_customer.py
```

---

# 💼 Interview Questions

### What is the Service Layer?

The Service Layer contains all business logic and coordinates interactions between the API Layer and the Repository Layer.

---

### Why is the Service Layer important?

It separates business logic from HTTP handling and database access, making the application easier to maintain, test, and extend.

---

### Can one Service call multiple Repositories?

Yes.

This is very common.

Example:

Creating an order may involve:

- Customer Repository
- Inventory Repository
- Payment Repository
- Shipment Repository

The Service Layer coordinates all these operations.

---

### Should SQL be written inside the Service Layer?

No.

SQL belongs in the Repository Layer.

---

### Should HTTP responses be created here?

No.

The Service Layer should return business results.

The Router decides how to convert those into HTTP responses.

---

# 🛍️ ShopSphere Example

Customer Registration

```
Customer Request

↓

Customer Service

↓

Validate Email

↓

Hash Password

↓

Repository

↓

PostgreSQL

↓

Return Customer Response
```

The Service Layer knows the business process.

It does not know how HTTP works.

It does not know how SQL is executed.

Its only responsibility is implementing business rules.

---

# 🎯 Key Takeaway

The Service Layer is the heart of the application.

Whenever business requirements change, this is usually the only layer that needs modification.

Keeping business logic centralized makes the application cleaner, more maintainable, and easier to test.