# 🛍️ ShopSphere Source System

> An e-commerce transactional source system built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Alembic** to simulate a production-ready OLTP application.

---

# 📖 Overview

ShopSphere is a REST API-based transactional application designed to act as the **source system** for an end-to-end Data Engineering platform.

The application manages customers, products, categories, brands, and orders while exposing data through REST APIs. Instead of allowing direct database access, downstream systems consume data through APIs, closely mirroring how modern enterprise applications integrate with Data Engineering platforms.

This repository focuses only on the **OLTP application**.

The extraction, ingestion, transformation, and analytics pipeline are implemented in a separate repository.

---

# 🏗️ Architecture

```
                  Client
                     │
                     ▼
              FastAPI REST APIs
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

---

# 🎯 Project Objectives

- Build a realistic transactional source system
- Design a normalized OLTP database
- Expose business entities through REST APIs
- Follow a layered architecture
- Simulate enterprise application development
- Provide a reliable data source for downstream ETL pipelines

---

# 🚀 Features

## Customer Management

- Create Customer
- Retrieve Customer
- Update Customer
- Soft Delete Customer

## Brand Management

- Create Brand
- Retrieve Brand
- Update Brand
- Soft Delete Brand

## Category Management

- Create Category
- Retrieve Category
- Update Category
- Soft Delete Category

## Product Management

- Create Product
- Product Catalog
- Brand & Category Relationships
- Inventory Quantity Tracking
- Soft Delete Product

## Order Management

- Create Orders
- Multiple Order Items
- Automatic Order Total Calculation
- Stock Deduction
- Order History

---

# 🏛️ Project Structure

```
shopsphere-source-system/

├── alembic/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── requirements.txt
├── .env.example
└── README.md
```

---

# 🧩 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| FastAPI | REST API Framework |
| PostgreSQL | OLTP Database |
| SQLAlchemy | ORM |
| Alembic | Database Migrations |
| Pydantic | Request & Response Validation |
| Docker | Local Development Environment |

---

# 📐 Design Principles

The project follows common enterprise backend practices:

- Layered Architecture
- Repository Pattern
- Service Layer Pattern
- Separation of Concerns
- Modular Design
- Reusable Components
- API-First Development
- Database Migrations with Alembic

---

# 🔄 Data Flow

```
                Client
                   │
                   ▼
           FastAPI REST APIs
                   │
                   ▼
            Business Logic
                   │
                   ▼
            Repository Layer
                   │
                   ▼
              PostgreSQL
```

---

# 📊 Current Status

### Core Infrastructure

- ✅ FastAPI
- ✅ PostgreSQL
- ✅ SQLAlchemy
- ✅ Alembic
- ✅ Docker
- ✅ Layered Architecture

### Business Modules

- ✅ Customer
- ✅ Brand
- ✅ Category
- ✅ Product
- ✅ Order

### Business Logic

- ✅ Inventory Management
- ✅ Order Total Calculation
- ✅ Product Relationships
- ✅ Pagination
- ✅ Input Validation
- ✅ Error Handling

---

# 🔗 Related Project

This application acts as the source system for the **ShopSphere Data Engineering Platform**, where data is extracted through REST APIs and loaded into a modern analytics stack.

The downstream platform includes:

- Python ETL
- REST API Client
- Parquet Landing Layer
- Snowflake
- dbt
- Power BI

---

# 👨‍💻 Author

**Maneesh Joshi**

Senior Data Engineer

Building production-style Data Engineering projects from source system to analytics.