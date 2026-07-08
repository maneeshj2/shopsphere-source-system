# 🛍️ ShopSphere Source System

> An enterprise-grade e-commerce source system built using **FastAPI**, **PostgreSQL**, **Docker**, and **Python** to simulate a real-world OLTP application for Data Engineering.

---

# 📖 Project Overview

ShopSphere is designed to mimic how modern e-commerce companies expose transactional data through REST APIs.

Instead of connecting directly to the production database, downstream data engineering systems consume data through APIs, making the architecture more secure, scalable, and loosely coupled.

This project will eventually demonstrate the complete data journey:

```
Customer
    │
    ▼
FastAPI APIs
    │
    ▼
PostgreSQL (OLTP)
    │
    ▼
Python Extractor
    │
    ▼
JSON Files
    │
    ▼
S3 / MinIO
    │
    ▼
Snowflake RAW
    │
    ▼
dbt STAGING
    │
    ▼
dbt MART
    │
    ▼
Power BI / Tableau
```

---

# 🎯 Project Goals

- Learn Enterprise FastAPI Development
- Build Production-Ready REST APIs
- Design a Realistic OLTP Database
- Implement Clean Architecture
- Simulate Source Systems used by Data Engineering teams
- Build a complete Data Pipeline into Snowflake

---

# 🏗️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| FastAPI | REST API Framework |
| PostgreSQL | OLTP Database |
| SQLAlchemy | Database Connectivity |
| Docker | Infrastructure |
| Pydantic | Request & Response Validation |
| Alembic *(Later)* | Database Versioning |
| Snowflake *(Later)* | Data Warehouse |
| dbt *(Later)* | Data Transformation |
| Airflow *(Later)* | Pipeline Orchestration |

---

# 📁 Project Structure

```
shopsphere-source-system/

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
├── database/
│   ├── schema/
│   ├── seed/
│   └── init.sql
│
├── docker/
├── docs/
├── learning/
├── tests/
│
├── requirements.txt
└── README.md
```

---

# 📚 Architecture

```
                Client

                   │

                   ▼

          FastAPI Router Layer

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

# 🧩 Design Principles

This project follows several enterprise software engineering principles:

- Separation of Concerns
- Layered Architecture
- Single Responsibility Principle
- API First Design
- Clean Code
- Modular Development
- Reusable Components

---

# 🚀 Features

### Customer Module

- Customer Registration
- Customer Lookup
- Customer Update
- Soft Delete

### Product Module *(Upcoming)*

- Product Catalog
- Categories
- Brands
- Suppliers

### Order Module *(Upcoming)*

- Shopping Cart
- Orders
- Payments
- Shipments

### Inventory Module *(Upcoming)*

- Warehouses
- Inventory Tracking
- Stock Movement

---

# 📖 Documentation

Each folder contains its own `README.md` explaining:

- Purpose
- Responsibilities
- Best Practices
- Folder Contents
- Common Mistakes
- Interview Notes

---

# 🎓 Learning Notes

The `learning/` folder contains topic-wise notes on:

- Docker
- PostgreSQL
- FastAPI
- REST APIs
- SQLAlchemy
- Pydantic
- Service Layer
- Repository Pattern
- System Design

---

# 💼 Interview Preparation

This repository is also intended to serve as interview preparation material.

Each module contains:

- Architecture Discussion
- Best Practices
- Enterprise Examples
- Common Interview Questions
- Design Decisions

---

# 👨‍💻 Current Progress

- ✅ Docker Setup
- ✅ PostgreSQL Setup
- ✅ FastAPI Setup
- ✅ Health Check API
- ✅ Customer API Skeleton
- ⏳ Customer Database Integration
- ⏳ Repository Layer
- ⏳ Authentication
- ⏳ Product Module
- ⏳ Order Module

---

# 📌 Author

**Maneesh Joshi**

Senior Data Engineer

Learning Backend Engineering through a real-world enterprise project.