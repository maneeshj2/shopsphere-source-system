# Source System Architecture

## Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python 3.12+ |
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| API Server | Uvicorn |
| Containerization | Docker |
| Documentation | Swagger/OpenAPI |

---

## High-Level Architecture

```

Website / Mobile App / POS
│
▼
FastAPI
│
▼
Business Services
│
▼
SQLAlchemy
│
▼
PostgreSQL

```

---

## Repository Structure

- app/
- api/
- core/
- db/
- models/
- schemas/
- services/
- utils/
- docker/
- docs/
- scripts/
- tests/

---

## Purpose

This repository simulates a production-grade operational retail system that serves as the source application for the ShopSphere Analytics Platform.