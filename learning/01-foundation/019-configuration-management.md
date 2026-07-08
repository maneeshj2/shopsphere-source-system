# ⚙️ Configuration Management

## Goal

Understand how applications manage configuration across different environments without hardcoding values.

This chapter explains configuration management using the ShopSphere project.

---

# What is Configuration?

Configuration is information that changes between environments but is **not part of the application logic**.

Examples

- Database Host
- Database Password
- API Keys
- JWT Secret
- AWS Credentials
- Redis Host
- S3 Bucket Name

These values should never be hardcoded.

---

# Why Do We Need Configuration?

Imagine this code.

```python
DATABASE_URL = "postgresql://admin:password@localhost:5432/shopsphere"
```

It works on your laptop.

Now the application moves to Production.

Production database

```
Host

10.50.100.20

Password

VeryStrongPassword

Database

shopsphere_prod
```

Now you have to modify the code.

This is bad practice.

---

# Better Approach

Application

↓

Reads

```
Environment Variables
```

↓

Uses Configuration

Now the code never changes.

Only configuration changes.

---

# Real World Analogy

Imagine buying a TV.

The TV works in

- India
- USA
- UK

Only the power adapter changes.

The TV software remains the same.

Configuration is like the adapter.

---

# Environment Variables

Environment variables are values provided by the operating system.

Example

```
DB_HOST

DB_PORT

DB_NAME

JWT_SECRET

AWS_REGION
```

Python reads them at runtime.

---

# .env File

During development we often use

```
.env
```

Example

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=shopsphere
DB_USER=shopsphere_admin
DB_PASSWORD=StrongPassword123

JWT_SECRET=my-secret-key

AWS_REGION=ap-south-1
```

The application loads these values automatically.

---

# FastAPI Configuration

ShopSphere uses

```python
class Settings(BaseSettings):
```

Example

```python
class Settings(BaseSettings):

    db_host: str

    db_port: int

    db_name: str
```

FastAPI creates

```python
settings = Settings()
```

Now

```python
settings.db_host
```

returns

```
localhost
```

---

# Configuration Flow

```
.env

↓

Environment Variables

↓

Settings Class

↓

Application

↓

Database Connection
```

---

# ShopSphere Example

Current

```
core/

settings.py
```

Responsible for

- Reading Environment Variables
- Validating Configuration
- Making Settings Available

Every module imports

```python
settings
```

instead of reading

```
os.getenv()
```

everywhere.

---

# Why Use a Settings Class?

Without it

```python
os.getenv("DB_HOST")

os.getenv("DB_PORT")

os.getenv("JWT_SECRET")
```

repeated everywhere.

Instead

```python
settings.db_host

settings.jwt_secret
```

Cleaner.

Centralized.

Type-safe.

---

# Different Environments

Development

```
localhost
```

Testing

```
test-db
```

Production

```
prod-db.company.com
```

Application code stays exactly the same.

Only configuration changes.

---

# Configuration vs Code

Application Logic

```python
create_customer()
```

Configuration

```
Database Password

JWT Secret

AWS Region
```

Never mix these.

---

# Secrets

Some configuration values are secrets.

Examples

- Database Password
- JWT Secret
- AWS Secret Key
- API Tokens

Never commit these to Git.

---

# .gitignore

Always ignore

```
.env
```

Example

```gitignore
.env
```

This prevents secrets from being pushed to GitHub.

---

# Production

Production environments usually don't use

```
.env
```

Instead

Cloud platforms provide

- Kubernetes Secrets
- AWS Secrets Manager
- Azure Key Vault
- HashiCorp Vault

These are more secure.

---

# Internal Working

```
Application Starts

↓

Read Environment Variables

↓

Create Settings Object

↓

Validate Configuration

↓

Application Ready
```

Configuration is loaded once during startup.

---

# ShopSphere Configuration

Current

```
Database

JWT

Application Name
```

Future

```
Redis

S3

Snowflake

SMTP

Kafka

Airflow

MinIO
```

Everything will come from configuration.

---

# Best Practices

- Never hardcode secrets
- Keep configuration centralized
- Validate configuration at startup
- Use different configurations for different environments
- Ignore .env in Git

---

# Common Mistakes

❌ Hardcoding passwords

❌ Committing .env to GitHub

❌ Duplicating configuration across files

❌ Mixing configuration with business logic

---

# Comparison

| Bad | Good |
|------|------|
| Hardcoded values | Environment Variables |
| Secrets in code | Secrets Manager |
| os.getenv() everywhere | Central Settings Class |
| One config for all environments | Separate configs |

---

# Interview Questions

### What is configuration?

Configuration consists of values that control application behavior without changing the code.

---

### Why shouldn't secrets be hardcoded?

Hardcoded secrets are difficult to rotate and may be exposed if the source code is leaked.

---

### What is the purpose of a `.env` file?

It provides environment-specific configuration during local development.

---

### Why use a Settings class?

To centralize configuration, provide type safety, and simplify access across the application.

---

### Should `.env` files be committed to Git?

No.

They often contain sensitive information and should be excluded using `.gitignore`.

---

# Where We Used This in ShopSphere

```
.env

↓

Settings()

↓

Database URL

↓

JWT Secret

↓

Application Configuration
```

---

# Revision Notes

✅ Configuration is not business logic.

✅ Store secrets outside the code.

✅ Use environment variables.

✅ Use a centralized Settings class.

✅ Never commit `.env`.

---

# Exercises

1. List five configuration values used in ShopSphere.

2. Why shouldn't database passwords be hardcoded?

3. Explain the difference between configuration and business logic.

4. Draw the configuration loading flow.

5. Why is a Settings class better than calling `os.getenv()` everywhere?

---

# Prerequisites

- FastAPI
- Dependency Injection

---

# Next Chapter

➡️ 020-logging.md