# 🗄️ Repository Layer

The Repository Layer is responsible for all interactions with the database.

It acts as the data access layer between the Service Layer and PostgreSQL. Every SQL query used by the application should be written here.

The Repository Layer knows **how** to store and retrieve data.

It does **not** know **why** the data is being stored.

---

# 📌 Responsibilities

The Repository Layer is responsible for:

- INSERT data
- UPDATE data
- DELETE data
- SELECT data
- Execute SQL queries
- Communicate with PostgreSQL
- Return database results to the Service Layer

---

# ❌ The Repository Layer SHOULD NOT

- Contain Business Logic
- Validate Business Rules
- Handle HTTP Requests
- Return HTTP Responses
- Perform Password Hashing
- Send Emails
- Calculate Discounts

These responsibilities belong to the Service Layer.

---

# 📁 Current Repositories

```
customer_repository.py
```

Future structure:

```
repositories/

├── customer_repository.py
├── product_repository.py
├── inventory_repository.py
├── order_repository.py
├── payment_repository.py
└── shipment_repository.py
```

Each repository manages one database entity or business domain.

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

The Repository Layer is the only layer that should directly communicate with PostgreSQL.

---

# 🏗️ Why Do We Need a Repository?

Imagine the Service Layer writes SQL directly.

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

Now imagine the same SQL being copied into multiple services.

Maintenance becomes difficult.

Instead:

```
Customer Service

↓

Customer Repository

↓

PostgreSQL
```

The Service Layer doesn't know SQL.

It simply asks:

```
Create Customer

Find Customer

Update Customer
```

The Repository decides how those operations are executed.

---

# 🛍️ Real-World Analogy

Imagine a library.

```
Reader

↓

Librarian

↓

Book Shelf
```

The reader says:

> "I need a Python book."

The reader never walks into the storage room.

The librarian retrieves the book.

Similarly,

The Service Layer asks:

```
Find Customer by Email
```

The Repository executes the SQL and returns the result.

---

# 💻 Example

Customer Repository

```python
def get_customer_by_email(email: str):

    # Execute SQL

    return customer
```

Customer Service

```python
customer = repository.get_customer_by_email(email)

if customer:
    raise Exception("Customer already exists")
```

Notice that the Service Layer never writes SQL.

---

# 🛒 Example Flow

Customer Registration

```
Customer Request

↓

Customer Service

↓

Customer Repository

↓

INSERT INTO customers

↓

PostgreSQL

↓

Repository

↓

Service

↓

Router
```

---

# 📖 Typical Repository Functions

```
create_customer()

get_customer()

get_customer_by_email()

update_customer()

delete_customer()

list_customers()
```

These methods focus only on database operations.

---

# 📦 Repository Pattern

The Repository Pattern provides an abstraction over the database.

Instead of writing SQL everywhere,

Services call repository methods.

Example:

```
customer_repository.create_customer(customer)
```

instead of

```
INSERT INTO customers ...
```

inside every Service.

This improves:

- Maintainability
- Reusability
- Testability
- Separation of Concerns

---

# ✅ Best Practices

- One repository per business domain
- Keep SQL inside repositories
- Return domain objects or models
- Keep methods focused
- Reuse common queries
- Handle database exceptions appropriately

---

# ❌ Common Mistakes

- Writing business logic here
- Calling external APIs
- Sending emails
- Returning HTTP responses
- Accessing FastAPI request objects
- Mixing multiple business domains in one repository

---

# 📖 Naming Convention

Repository files should be named after the business domain.

Examples:

```
customer_repository.py

product_repository.py

order_repository.py
```

Avoid:

```
database.py

customer_sql.py

db_queries.py
```

---

# 💼 Interview Questions

### What is the Repository Pattern?

The Repository Pattern abstracts database access behind a set of methods, allowing the Service Layer to work without knowing SQL or database implementation details.

---

### Why use a Repository Layer?

It separates business logic from data access, making the application easier to maintain, test, and extend.

---

### Should Business Logic exist inside a Repository?

No.

Repositories should only interact with the database.

---

### Can multiple Services use the same Repository?

Yes.

For example:

Customer Service

Order Service

Loyalty Service

may all use

```
CustomerRepository
```

---

### Can one Service call multiple Repositories?

Yes.

This is very common in enterprise applications.

---

# 🛍️ ShopSphere Example

Customer Registration

```
Customer Service

↓

Customer Repository

↓

INSERT INTO retail.customers

↓

PostgreSQL

↓

Return Generated UUID

↓

Service Layer
```

Notice that the Repository knows SQL.

It does not know:

- Password Rules
- Email Validation
- Loyalty Program
- Business Policies

Those belong to the Service Layer.

---

# 🔄 Difference Between Service and Repository

| Service Layer | Repository Layer |
|---------------|------------------|
| Business Logic | Database Logic |
| Coordinates Processes | Executes SQL |
| Calls Repositories | Talks to PostgreSQL |
| Knows Business Rules | Knows Tables |
| Doesn't Write SQL | Doesn't Know Business |

---

# 🎯 Key Takeaway

The Repository Layer is the application's data access layer.

Its only responsibility is to communicate with PostgreSQL.

By keeping SQL inside repositories and business rules inside services, the application remains modular, scalable, and easy to maintain.