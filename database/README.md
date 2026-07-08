# 🗄️ Database Layer

The `database` folder contains all SQL scripts required to create, initialize, and populate the ShopSphere PostgreSQL database.

Unlike the `app/` folder, which contains Python application code, this folder contains only database-related artifacts such as schemas, DDL scripts, seed data, and initialization scripts.

The goal is to keep database design separate from application logic.

---

# 📌 Responsibilities

The Database Layer is responsible for:

- Database Initialization
- Schema Creation
- Table Definitions
- Constraints
- Indexes
- Seed Data
- Database Extensions
- Database Versioning (Future)

---

# ❌ The Database Layer SHOULD NOT

- Contain Python Code
- Implement Business Logic
- Handle API Requests
- Validate Input Data
- Store Application Configuration

Those responsibilities belong to the application.

---

# 📁 Folder Structure

```
database/

├── init.sql
├── schema/
├── seed/
└── README.md
```

Future structure:

```
database/

├── init.sql
├── schema/
│   ├── customers.sql
│   ├── products.sql
│   ├── orders.sql
│   ├── inventory.sql
│   └── payments.sql
│
├── seed/
│   ├── customers.sql
│   ├── products.sql
│   └── inventory.sql
│
├── migrations/
│   └── (Future - Alembic/Flyway)
│
└── README.md
```

---

# 🔄 Position in the Architecture

```
Application

        │

        ▼

Repository Layer

        │

        ▼

PostgreSQL Database

        ▲

        │

Database SQL Scripts
```

The application interacts with PostgreSQL.

The SQL scripts define what PostgreSQL looks like.

---

# 🏗️ Why Keep SQL Separate?

Keeping SQL scripts outside Python provides several advantages:

- Easier Database Review
- Better Version Control
- Independent Database Development
- Easier Production Deployment
- Cleaner Project Structure

Database engineers and application developers can work independently.

---

# 🛍️ Real-World Analogy

Imagine constructing a shopping mall.

The architect first creates:

- Building Layout
- Electrical Plan
- Plumbing Plan

Only after the building is complete do businesses move in.

Similarly,

The database structure is created before the application starts storing data.

---

# 📦 Folder Responsibilities

### schema/

Contains DDL scripts.

Examples:

```
CREATE TABLE

ALTER TABLE

CREATE INDEX

CREATE VIEW
```

---

### seed/

Contains sample or reference data.

Examples:

```
Countries

States

Categories

Demo Customers

Test Products
```

Seed data is mainly used for development and testing.

---

### init.sql

Acts as the database installer.

Responsibilities:

- Enable PostgreSQL extensions
- Create schemas
- Execute all table scripts
- Execute initialization SQL

Think of it as the master entry point for database creation.

---

# 🏢 Enterprise Workflow

Typical development process:

```
Developer writes SQL

↓

Commit to Git

↓

CI/CD Pipeline

↓

Deploy Database Changes

↓

Application Uses Updated Schema
```

Database changes are version-controlled just like application code.

---

# 📖 Naming Convention

Schema files:

```
customers.sql

products.sql

orders.sql
```

Seed files:

```
customers_seed.sql

products_seed.sql
```

Keep names singular, descriptive, and business-oriented.

---

# 📚 Database Design Principles

ShopSphere follows:

- Third Normal Form (3NF)
- Primary Keys
- Foreign Keys
- Soft Deletes
- Audit Columns
- UUID Primary Keys
- Meaningful Naming Conventions

As the project grows, additional patterns such as partitioning and indexing strategies will be introduced.

---

# 🔄 Database Lifecycle

```
Docker Starts

↓

PostgreSQL Starts

↓

init.sql Executes

↓

Schema Created

↓

Tables Created

↓

Seed Data Loaded

↓

Application Connects
```

This ensures the application always starts with a consistent database.

---

# 🚀 Future Enhancements

Later in the project we will add:

- Views
- Materialized Views
- Stored Procedures
- Triggers
- Index Optimization
- Database Migrations
- Performance Tuning
- Query Plans
- Partitioning

This project will gradually evolve into a production-style OLTP database.

---

# ✅ Best Practices

- Keep one table per SQL file
- Use meaningful table names
- Use consistent naming conventions
- Add audit columns
- Use constraints appropriately
- Review SQL before deployment

---

# ❌ Common Mistakes

- Putting multiple tables in one file
- Hardcoding sample data into DDL scripts
- Ignoring indexes
- Missing primary keys
- Mixing application logic with SQL

---

# 🔗 Related Layers

### Used By

- Repository Layer

### Contains

- Database Schema
- Table Definitions
- Seed Data

### Creates

- PostgreSQL Objects

---

# 💼 Interview Questions

### Why keep SQL scripts outside application code?

Separating SQL from application code improves maintainability, enables independent database versioning, and allows database changes to be reviewed and deployed separately.

---

### What is init.sql?

`init.sql` is the master initialization script responsible for creating the database structure and executing all required SQL files.

---

### Why create one SQL file per table?

It improves readability, modularity, version control, and makes future maintenance much easier.

---

### Why use UUID instead of SERIAL?

UUIDs provide globally unique identifiers, reduce predictability, and simplify distributed system architectures.

---

# 🛍️ ShopSphere Example

```
database/

↓

customers.sql

↓

Creates

retail.customers

↓

Repository Layer

↓

Customer Service

↓

API
```

The database scripts define the storage layer.

The application simply uses that structure.

---

# 🎯 Key Takeaway

The `database` folder is the source of truth for the PostgreSQL schema.

It defines how data is stored, while the application defines how data is processed.

Keeping these responsibilities separate leads to a cleaner, more maintainable architecture.

---

# 🧠 Interview Summary

✅ SQL scripts belong outside application code.

✅ One table per SQL file.

✅ init.sql orchestrates database initialization.

Most Asked Question:

**"Why separate database scripts from backend code?"**

Answer:

It improves maintainability, enables independent database deployments, supports version control, and allows database engineers and backend developers to work independently.

---

# 📚 Further Reading

See:

learning/

- 003-postgresql.md
- 010-database-design.md
- 011-normalization.md
- 013-indexing.md