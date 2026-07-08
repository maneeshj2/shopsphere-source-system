c# 🌱 Seed Data

The `seed` folder contains SQL scripts used to populate the database with initial or sample data.

Unlike the `schema` folder, which defines the database structure, the `seed` folder inserts data into existing tables.

Seed data helps developers, testers, and automated pipelines work with realistic datasets without manually entering records.

---

# 📌 Responsibilities

The Seed Layer is responsible for:

- Loading Reference Data
- Loading Sample Data
- Loading Development Data
- Loading Test Data
- Populating Lookup Tables

---

# ❌ The Seed Layer SHOULD NOT

- Create Tables
- Alter Database Structure
- Contain Business Logic
- Modify Production Data
- Execute DDL Statements

The schema must already exist before seed scripts are executed.

---

# 📁 Folder Structure

```
seed/

├── categories.sql
├── products.sql
├── suppliers.sql
├── customers.sql
└── inventory.sql
```

Each file inserts data into one business entity.

---

# 🔄 Position in the Architecture

```
Schema Scripts

        │

        ▼

Database Tables Created

        │

        ▼

Seed Scripts

        │

        ▼

Sample Data Available

        │

        ▼

Application Ready
```

Seed scripts run **after** the schema has been created.

---

# 🏗️ Why Do We Need Seed Data?

Imagine opening ShopSphere for the first time.

Without seed data:

```
Products

0 Records

Categories

0 Records

Customers

0 Records
```

Nothing works.

With seed data:

```
Products

250 Records

Categories

15 Records

Customers

100 Demo Customers
```

The application is immediately usable.

---

# 🛍️ Real-World Analogy

Imagine opening a new supermarket.

The building is complete.

The shelves exist.

But there are no products.

The supermarket cannot operate.

Seed data is the process of filling those shelves before customers arrive.

---

# 📦 Types of Seed Data

## Reference Data

Rarely changes.

Examples

```
Countries

States

Currencies

Payment Methods

Order Statuses
```

---

## Sample Data

Used for development.

Examples

```
Demo Customers

Products

Orders

Reviews
```

---

## Test Data

Used for automated testing.

Usually small, predictable, and repeatable.

---

# 💻 Example

customers.sql

```sql
INSERT INTO retail.customers
(
    customer_id,
    first_name,
    last_name,
    email
)

VALUES
(
    gen_random_uuid(),
    'John',
    'Doe',
    'john@example.com'
);
```

---

# 🔄 Execution Order

Seed scripts should follow dependency order.

Example

```
Categories

↓

Products

↓

Customers

↓

Orders

↓

Order Items

↓

Payments
```

Never insert child records before parent records.

---

# 🛒 ShopSphere Strategy

During development we may seed:

- Product Categories
- Brands
- Suppliers
- Warehouses
- Demo Products
- Demo Customers

This allows API development without manually entering data.

---

# 📖 Naming Convention

Use descriptive names.

Examples

```
customers.sql

products.sql

categories.sql
```

Avoid

```
seed1.sql

insert.sql

demo.sql
```

---

# 🧠 Idempotent Seed Scripts

Whenever possible, seed scripts should be safe to run multiple times.

Example:

```sql
INSERT ...

ON CONFLICT DO NOTHING;
```

or

```sql
WHERE NOT EXISTS (...)
```

This prevents duplicate data during development.

---

# ✅ Best Practices

- One entity per seed file
- Keep data realistic
- Use meaningful sample values
- Follow foreign key order
- Make scripts repeatable where possible
- Separate reference data from demo data

---

# ❌ Common Mistakes

- Mixing schema creation with seed data
- Hardcoding IDs unnecessarily
- Ignoring foreign key dependencies
- Inserting unrealistic sample data
- Making seed scripts non-repeatable

---

# 🔗 Related Layers

### Runs After

- init.sql
- Schema Scripts

### Supports

- API Development
- Manual Testing
- Integration Testing
- Demo Environments

---

# 💼 Interview Questions

### What is seed data?

Seed data is the initial dataset loaded into a database after the schema has been created. It helps developers and testers work with realistic data.

---

### Why separate schema and seed scripts?

Schema defines the structure of the database.

Seed scripts populate that structure with data.

Keeping them separate improves maintainability and deployment flexibility.

---

### Should production databases use demo seed data?

No.

Production environments usually receive data from real business operations.

Only reference data (such as countries, currencies, or status codes) is typically seeded.

---

### What does idempotent mean?

An idempotent script can be executed multiple times without producing unintended duplicate data or side effects.

---

# 🛍️ ShopSphere Example

```
Schema

↓

customers table created

↓

customers.sql

↓

100 demo customers inserted

↓

Swagger APIs immediately usable
```

This makes development and testing much faster.

---

# 🎯 Key Takeaway

The `seed` folder provides the initial data required for development, testing, and demonstration.

It complements the schema by populating tables with realistic and reusable datasets.

---

# 🧠 Interview Summary

✅ Schema creates structure.

✅ Seed inserts data.

✅ Reference data is different from demo data.

✅ Seed scripts should be repeatable.

Most Asked Question:

**"What is the difference between schema scripts and seed scripts?"**

Answer:

Schema scripts define database objects such as tables and constraints.

Seed scripts populate those objects with initial or sample data.

---

# 📚 Further Reading

See:

learning/

- PostgreSQL
- Database Design
- Data Modeling
- ETL Fundamentals
- CI/CD Database Deployments