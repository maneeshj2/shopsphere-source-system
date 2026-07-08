# 🐳 Docker Fundamentals

## Goal

Understand Docker from a Data Engineer's perspective and learn why almost every modern application runs inside containers.

---

# What Problem Does Docker Solve?

Imagine two developers working on the same project.

Developer A

```
Python 3.12

PostgreSQL 17

MacOS
```

Developer B

```
Python 3.10

PostgreSQL 15

Windows
```

The application works on one machine but fails on another.

This is known as

> "It works on my machine."

Docker solves this problem by packaging the application together with everything it needs.

---

# What is Docker?

Docker is a containerization platform.

It packages:

- Application Code
- Runtime
- Dependencies
- Libraries
- Environment

into a single unit called a **Container**.

---

# Real World Analogy

Imagine shipping goods.

Without containers:

```
TV

Chair

Books

Food

Laptop
```

Everything is loaded separately.

With containers:

```
📦 Container

TV

Books

Laptop

Chair
```

The ship doesn't care what's inside.

It simply moves containers.

Docker works exactly the same way.

---

# Docker Components

```
Docker Engine

↓

Docker Image

↓

Docker Container
```

---

# Docker Image

Think of an Image as a blueprint.

It contains everything required to create a container.

Example:

```
PostgreSQL Image

↓

Can create many PostgreSQL Containers
```

---

# Docker Container

A running instance of an Image.

Example

```
Image

↓

Run

↓

Container
```

Just like

```
Python Class

↓

Object
```

---

# Dockerfile

A Dockerfile contains instructions for building an image.

Example

```dockerfile
FROM python:3.12

COPY .

RUN pip install -r requirements.txt

CMD ["uvicorn","app.main:app"]
```

Docker executes these instructions step by step.

---

# Docker Compose

Docker Compose starts multiple containers together.

Example

```
FastAPI

↓

PostgreSQL

↓

Redis

↓

MinIO
```

Instead of running each individually,

Docker Compose starts everything with one command.

---

# ShopSphere Architecture

Current

```
Docker

↓

PostgreSQL
```

Future

```
Docker

├── FastAPI

├── PostgreSQL

├── MinIO

├── Redis

└── Airflow
```

Everything will run together.

---

# Common Docker Commands

Start containers

```bash
docker compose up -d
```

Stop containers

```bash
docker compose down
```

Stop and remove volumes

```bash
docker compose down -v
```

View containers

```bash
docker ps
```

View logs

```bash
docker logs <container>
```

Access PostgreSQL

```bash
docker exec -it shopsphere-postgres psql -U shopsphere_admin -d shopsphere
```

---

# Docker Volumes

Containers are temporary.

Data should not be.

Volumes keep data even after containers stop.

Example

```
Container Deleted

↓

Volume Remains

↓

Data Safe
```

---

# Why did we use `docker compose down -v`?

Because PostgreSQL executes

```
init.sql
```

only when creating a fresh database.

Removing the volume forces PostgreSQL to recreate the database.

---

# Why Docker Matters for Data Engineers

Docker is widely used for:

- Airflow
- Kafka
- Spark
- MinIO
- PostgreSQL
- MySQL
- Redis
- Trino
- Superset

Understanding Docker is an essential skill for modern data platforms.

---

# Best Practices

- One responsibility per container
- Use Docker Compose for local development
- Keep images lightweight
- Never hardcode secrets
- Persist important data using volumes

---

# Common Mistakes

❌ Confusing Images with Containers

❌ Storing important data inside containers

❌ Rebuilding images unnecessarily

❌ Forgetting to mount volumes

---

# Interview Questions

### What is Docker?

Docker is a platform for packaging applications and their dependencies into portable containers.

---

### Difference between Image and Container?

Image = Blueprint

Container = Running Instance

---

### Why use Docker?

Consistency

Portability

Isolation

Scalability

Simplified Deployment

---

### What is Docker Compose?

Docker Compose manages multiple containers as one application.

---

### Why use Volumes?

To persist data independently of the container lifecycle.

---

# ShopSphere Example

```
Developer

↓

docker compose up

↓

PostgreSQL Container

↓

Database Ready

↓

FastAPI Connects

↓

Application Runs
```

---

# Revision Notes

✅ Docker packages applications.

✅ Images create Containers.

✅ Compose manages multiple containers.

✅ Volumes preserve data.

✅ Containers are disposable.

---

# Next Topic

002-postgresql.md