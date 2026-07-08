# 🌐 API Layer

The API Layer is the entry point of the ShopSphere application.

Every HTTP request from a client (Browser, Mobile App, Swagger UI, Postman, etc.) enters the application through this layer.

The API Layer is responsible for receiving requests, validating request formats using Pydantic schemas, forwarding requests to the appropriate Service Layer, and returning HTTP responses.

---

# 📌 Responsibilities

The API Layer should only:

- Receive HTTP Requests
- Accept Request Schemas
- Call the appropriate Service Layer
- Return Response Schemas
- Define HTTP Status Codes
- Define API Routes

---

# ❌ The API Layer SHOULD NOT

- Contain Business Logic
- Execute SQL Queries
- Open Database Connections
- Hash Passwords
- Calculate Prices
- Perform Complex Validations

These responsibilities belong to the Service Layer.

---

# 📁 Current APIs

```
health.py
customers.py
```

As the application grows, more API files will be added.

```
api/

├── health.py
├── customers.py
├── products.py
├── orders.py
├── inventory.py
├── payments.py
└── shipments.py
```

Each file represents one business domain.

---

# 📚 API Design

Each API file owns one business domain.

Example:

```
customers.py

POST   /customers

GET    /customers/{customer_id}

PUT    /customers/{customer_id}

DELETE /customers/{customer_id}
```

Similarly,

```
products.py

GET    /products

POST   /products

PUT    /products/{product_id}
```

This keeps the project modular and easy to maintain.

---

# 🔄 Request Flow

Every request follows the same path.

```
Browser / Swagger

        │

        ▼

API Router

        │

        ▼

Pydantic Request Schema

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

Browser / Swagger
```

---

# 🧠 Why Routers Should Be Thin

Routers should act like receptionists.

Their responsibility is to receive a request and forward it to the appropriate service.

Good Router:

```python
@router.post("/")
def create_customer(customer: CustomerCreateRequest):
    return customer_service.create_customer(customer)
```

Bad Router:

```python
@router.post("/")
def create_customer():

    validate_email()

    calculate_discount()

    hash_password()

    execute_sql()

    send_email()
```

Business logic should never be written inside routers.

---

# 📦 APIRouter

Every business domain gets its own router.

Example:

```python
router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)
```

The `prefix` avoids repeating `/customers` on every endpoint.

Instead of writing:

```python
@router.post("/customers")

@router.get("/customers")

@router.put("/customers/{id}")
```

We write:

```python
prefix="/customers"

@router.post("/")

@router.get("/{customer_id}")

@router.put("/{customer_id}")
```

FastAPI automatically combines them.

---

# 📖 Naming Convention

Each router file should be named after the business domain.

Examples:

```
customers.py

products.py

orders.py

payments.py
```

Avoid names like:

```
customer_api.py

product_routes.py

api_customer.py
```

Keep naming simple and predictable.

---

# ✅ Best Practices

- One router per business domain
- Keep routers small
- Delegate all business logic to Services
- Use Request Schemas
- Use Response Schemas
- Return meaningful HTTP Status Codes
- Group APIs using tags

---

# ❌ Common Mistakes

- Writing SQL inside routers
- Writing Business Logic inside routers
- Returning raw database objects
- Not validating request payloads
- Returning different response structures for similar APIs

---

# 💼 Interview Questions

### What is APIRouter?

APIRouter is a FastAPI component used to organize related endpoints into modular groups.

---

### Why do we use APIRouter instead of putting everything in main.py?

It keeps the application modular, improves maintainability, and allows each business domain to be developed independently.

---

### What should a Router contain?

Only HTTP-related concerns:

- Request Handling
- Response Handling
- Calling Service Layer

---

### What should never be inside a Router?

- SQL Queries
- Business Logic
- Password Hashing
- Complex Calculations

---

# 🛍️ ShopSphere Example

Customer Registration

```
POST /customers
```

Router receives:

```json
{
    "first_name": "Maneesh",
    "email": "maneesh@gmail.com",
    "password": "Password@123"
}
```

↓

Validates request format

↓

Calls

```
customer_service.create_customer()
```

↓

Returns

```json
{
    "customer_id": "...",
    "message": "Customer created successfully"
}
```

Notice that the Router never talks directly to PostgreSQL.

It always communicates through the Service Layer.

---

# 🎯 Key Takeaway

The API Layer is responsible for handling HTTP communication only.

It should never contain business logic or database operations.

A clean Router simply receives a request, delegates work to the Service Layer, and returns a response.