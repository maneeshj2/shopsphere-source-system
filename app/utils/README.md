# 🧰 Utilities Layer

The `utils` folder contains reusable helper functions that are shared across the application.

Utilities are generic functions that do not belong to any specific business domain and can be safely reused by multiple modules.

The goal of this layer is to avoid duplicate code.

---

# 📌 Responsibilities

The Utilities Layer is responsible for:

- Reusable helper functions
- Data formatting
- Date & Time helpers
- UUID helpers
- Password hashing
- Common validation helpers
- Generic utility functions

---

# ❌ The Utilities Layer SHOULD NOT

- Contain Business Logic
- Execute SQL Queries
- Handle HTTP Requests
- Access PostgreSQL
- Call External APIs

Utilities should be generic and independent.

---

# 📁 Current Structure

```
utils/

(Currently Empty)
```

Future structure:

```
utils/

├── password.py
├── uuid_helper.py
├── datetime_helper.py
├── validators.py
├── response_helper.py
├── file_helper.py
└── constants.py
```

Every utility should have one clear responsibility.

---

# 🔄 Position in the Architecture

```
                API Layer

                   │

            Service Layer

                   │

        ┌──────────┴──────────┐

        ▼                     ▼

 Repository Layer        Utilities

        │

        ▼

    PostgreSQL
```

Utilities can be used by multiple layers.

They should never depend on any business domain.

---

# 🏗️ Why Do We Need Utilities?

Imagine we need to hash passwords.

Without Utilities:

```
Customer Service

↓

Hash Password
```

```
Admin Service

↓

Hash Password
```

```
Employee Service

↓

Hash Password
```

The same code gets copied everywhere.

Instead:

```
Customer Service

↓

password.hash()

↓

Result
```

One implementation.

Everyone reuses it.

---

# 🛍️ Real-World Analogy

Imagine a toolbox.

Inside it you have:

- Screwdriver
- Hammer
- Wrench
- Measuring Tape

The toolbox itself doesn't build a house.

It simply provides tools that anyone can use.

The Utilities Layer works the same way.

---

# 💻 Example

Password Utility

```python
def hash_password(password: str):

    ...
```

Customer Service

```python
hashed_password = hash_password(customer.password)
```

Notice that the Service Layer uses the utility.

The utility does not know anything about Customers.

---

# 📦 Typical Utilities

Examples include:

```
Password Hashing

UUID Generation

Date Formatting

String Formatting

Email Validation

Phone Number Formatting

File Utilities

JSON Utilities

Response Helpers
```

These are generic and reusable.

---

# 📖 What Should NOT Become a Utility?

Bad Example:

```python
create_customer()
```

Why?

Because it belongs to the Customer business domain.

Good Example:

```python
generate_uuid()
```

Because every module can use it.

---

# 🔄 Utility vs Service

| Utility | Service |
|----------|----------|
| Generic | Business Specific |
| Reusable Everywhere | One Business Domain |
| Stateless | Contains Business Rules |
| No Database Access | May Use Repository |
| No Business Knowledge | Knows Business Rules |

---

# 📚 Example

Good Utility

```python
format_phone_number()
```

Bad Utility

```python
register_customer()
```

The second one belongs inside the Service Layer.

---

# ✅ Best Practices

- Keep functions generic
- Make utilities reusable
- Keep utilities independent
- Write small focused functions
- Avoid business-specific code

---

# ❌ Common Mistakes

- Putting business logic here
- Accessing the database
- Importing FastAPI routers
- Creating utilities that depend on Services
- Writing very large helper files

---

# 🔗 Related Layers

### Used By

- API Layer
- Service Layer
- Repository Layer

Utilities are shared across the application.

---

# 💼 Interview Questions

### What is the Utilities Layer?

The Utilities Layer contains reusable helper functions that can be shared across different parts of the application.

---

### When should code be moved to a Utility?

When it is generic, reusable, and does not belong to a specific business domain.

---

### Should Utilities contain Business Logic?

No.

Business rules belong in the Service Layer.

Utilities should remain generic.

---

### Can Utilities access the Database?

No.

Database operations belong in the Repository Layer.

---

# 🛍️ ShopSphere Example

Customer Registration

```
Customer Service

↓

password.hash()

↓

Repository

↓

PostgreSQL
```

The password hashing function is reusable.

The customer registration logic is not.

---

# 🚀 Future Utilities

As ShopSphere grows, this folder will contain:

- Password Hashing
- JWT Token Generation
- UUID Helpers
- Date Utilities
- File Upload Helpers
- Email Utilities
- Common Validators

These utilities will be reused throughout the application.

---

# 🎯 Key Takeaway

The Utilities Layer contains generic helper functions that improve code reuse and reduce duplication.

It should never contain business logic or database operations.

---

# 🧠 Interview Summary

✅ Generic helper functions belong here.

✅ Business logic does not.

✅ Utilities should be reusable and independent.

Most Asked Question:

**"How do you decide whether code belongs in a Utility or a Service?"**

Answer:

If the function is generic and reusable across multiple domains, it belongs in the Utilities Layer.

If it implements a business rule or process, it belongs in the Service Layer.

---

# 📚 Further Reading

See:

learning/

- 006-service-layer.md
- 012-utility-functions.md
- 009-project-architecture.md