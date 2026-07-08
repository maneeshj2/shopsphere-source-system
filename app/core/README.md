# ⚙️ Core Layer

The Core Layer contains the application's global configuration, settings, and shared infrastructure that are used across multiple modules.

Think of this folder as the central place for application-wide configuration.

It does not contain business logic.

---

# 📌 Responsibilities

The Core Layer is responsible for:

- Application Configuration
- Environment Variables
- Database Configuration
- Security Configuration
- Global Constants
- Shared Dependencies
- Common Application Settings

---

# ❌ The Core Layer SHOULD NOT

- Execute SQL Queries
- Contain Business Logic
- Handle HTTP Requests
- Validate Business Rules
- Store Database Models

Those responsibilities belong to their respective layers.

---

# 📁 Current Files

```
core/

└── config.py
```

Future structure:

```
core/

├── config.py
├── security.py
├── constants.py
├── logging.py
├── exceptions.py
└── dependencies.py
```

As the application grows, more global configurations will be added here.

---

# 🔄 Position in the Architecture

```
                 Configuration

                       │

       ┌───────────────┼───────────────┐

       ▼               ▼               ▼

   Database        API Layer      Service Layer

       ▼               ▼               ▼

             Entire Application
```

The Core Layer is shared by the whole application.

It doesn't belong to any specific business domain.

---

# 🏗️ Why Do We Need This Layer?

Imagine every file contains:

```python
DATABASE_URL = "postgresql://..."
```

or

```python
SECRET_KEY = "abc123"
```

Now imagine the database password changes.

You would have to update multiple files.

Instead,

every module imports configuration from one place.

```
config.py

↓

Application

↓

Everyone shares the same configuration
```

---

# 🛍️ Real-World Analogy

Imagine an office building.

Every employee needs:

- Office Address
- Wi-Fi Password
- Company Name
- Working Hours

Instead of asking each employee to remember these individually,

the company publishes them centrally.

Similarly,

the Core Layer stores application-wide configuration.

---

# 💻 Current Example

Our current configuration:

```python
settings = Settings()
```

contains

```
DATABASE_URL
```

Whenever a Repository or Database Layer needs the connection string,

it imports:

```python
from app.core.config import settings
```

No hardcoding.

---

# 📦 Typical Configuration

Examples of configuration stored here:

```
Database URL

API Version

Application Name

JWT Secret

JWT Expiry

Redis URL

S3 Bucket Name

Snowflake Credentials

SMTP Server

Application Environment
```

These values usually come from environment variables.

---

# 🔐 Environment Variables

Sensitive information should never be hardcoded.

Instead of:

```python
DATABASE_URL = "postgres://admin:password@..."
```

use

```
.env

↓

config.py

↓

Application
```

This improves:

- Security
- Maintainability
- Portability

---

# 📖 Why Use Pydantic Settings?

ShopSphere uses:

```python
BaseSettings
```

because it automatically:

- Reads `.env`
- Validates configuration
- Provides type safety
- Supports default values

This reduces configuration errors.

---

# ✅ Best Practices

- Keep configuration centralized
- Never hardcode secrets
- Use environment variables
- Use typed settings
- Separate configuration from business logic

---

# ❌ Common Mistakes

- Hardcoding passwords
- Duplicating configuration
- Putting business logic in config files
- Mixing application settings with constants

---

# 🔗 Related Layers

### Used By

- Database Layer
- Repository Layer
- API Layer
- Service Layer

### Depends On

- Environment Variables
- `.env` file
- Pydantic Settings

The Core Layer provides configuration to the entire application.

---

# 💼 Interview Questions

### What is the purpose of the Core Layer?

The Core Layer centralizes application-wide configuration and shared infrastructure so that all modules use a single source of truth.

---

### Why shouldn't we hardcode configuration?

Hardcoded values are difficult to maintain, insecure, and make deployment across environments (Development, QA, Production) much harder.

---

### Why use environment variables?

Environment variables allow sensitive information and environment-specific settings to be changed without modifying application code.

---

### Why use BaseSettings?

`BaseSettings` automatically loads configuration from environment variables and validates it using Pydantic.

---

# 🛍️ ShopSphere Example

Current

```
DATABASE_URL

↓

config.py

↓

database.py

↓

PostgreSQL
```

Future

```
DATABASE_URL

SNOWFLAKE_URL

AWS_ACCESS_KEY

JWT_SECRET

↓

config.py

↓

Entire Application
```

One place.

Everyone imports from it.

---

# 🚀 Future Expansion

As ShopSphere grows, this folder will also manage:

- JWT Authentication
- Application Logging
- Global Exception Handling
- Dependency Injection
- Role-Based Access Control (RBAC)
- Feature Flags

This makes the application easier to configure and deploy.

---

# 🎯 Key Takeaway

The Core Layer provides shared configuration and infrastructure for the entire application.

It acts as the single source of truth for settings, secrets, and global application behavior.

---

# 🧠 Interview Summary

✅ One place for configuration.

✅ Never hardcode secrets.

✅ Use environment variables.

Most Asked Question:

**"Why should application configuration be centralized?"**

Answer:

Centralized configuration improves security, maintainability, and consistency. It allows applications to run in different environments without changing the source code.

---

# 📚 Further Reading

See:

learning/

- 001-environment-variables.md
- 002-pydantic-settings.md
- 009-project-architecture.md