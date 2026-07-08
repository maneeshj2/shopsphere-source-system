# 🌐 REST API Fundamentals

## Goal

Understand what REST APIs are, why they exist, and how they enable communication between different systems.

This chapter explains REST APIs from a Backend and Data Engineering perspective using the ShopSphere project.

---

# What is an API?

API stands for

Application Programming Interface.

An API allows one application to communicate with another application.

Instead of accessing a database directly, applications communicate through APIs.

Example

```
Mobile App

↓

REST API

↓

Backend

↓

PostgreSQL
```

---

# Why Do We Need APIs?

Imagine an e-commerce company.

Customers use

- Website
- Mobile App
- Admin Portal

All three need customer data.

Without APIs

```
Website

↓

Database

Mobile

↓

Database

Admin

↓

Database
```

Everyone connects directly to PostgreSQL.

This is dangerous.

Instead

```
Website

↓

API

↓

Database

Mobile

↓

API

↓

Database

Admin

↓

API

↓

Database
```

Now the API controls access.

---

# Real World Analogy

Imagine a restaurant.

```
Customer

↓

Waiter

↓

Kitchen
```

Customers never enter the kitchen.

They tell the waiter.

The waiter communicates with the chef.

REST API = Waiter

Database = Kitchen

---

# What is REST?

REST stands for

Representational State Transfer.

REST is a set of architectural principles for designing web APIs.

REST is **not** a programming language.

REST is **not** a framework.

It is a design style.

---

# REST Principles

A REST API should be

- Stateless
- Client-Server
- Resource-Based
- Cacheable
- Uniform Interface

---

# Resource

Everything in REST is a Resource.

Example

```
Customer

Product

Order

Payment

Inventory
```

Resources are identified using URLs.

Example

```
/customers

/products

/orders
```

---

# HTTP Methods

REST APIs use HTTP methods.

---

## GET

Retrieve data.

Example

```
GET /customers
```

Returns

```
Customer List
```

---

## POST

Create new data.

Example

```
POST /customers
```

Creates

```
New Customer
```

---

## PUT

Replace an existing resource.

Example

```
PUT /customers/{customer_id}
```

---

## PATCH

Partially update a resource.

Example

```
PATCH /customers/{customer_id}
```

Update only

```
phone_number
```

instead of replacing the whole customer.

---

## DELETE

Delete a resource.

Example

```
DELETE /customers/{customer_id}
```

In ShopSphere

↓

Soft Delete

---

# CRUD Mapping

| CRUD | HTTP |
|------|------|
| Create | POST |
| Read | GET |
| Update | PUT / PATCH |
| Delete | DELETE |

---

# URL Design

Good

```
/customers

/customers/{customer_id}

/products

/orders
```

Bad

```
/getCustomers

/createCustomer

/deleteProduct
```

REST uses nouns.

Not verbs.

---

# HTTP Status Codes

## 200

Success

---

## 201

Created

Usually returned after POST.

---

## 204

Success

No Content.

---

## 400

Bad Request

Invalid Input.

---

## 401

Unauthorized

Authentication required.

---

## 403

Forbidden

Authenticated

Not allowed.

---

## 404

Not Found

Resource doesn't exist.

---

## 500

Internal Server Error.

Backend failure.

---

# Request

Example

```
POST /customers
```

Headers

```
Content-Type

application/json
```

Body

```json
{
    "first_name":"Maneesh",

    "email":"maneesh@gmail.com"
}
```

---

# Response

```json
{
    "customer_id":"550e...",

    "message":"Customer created successfully"
}
```

---

# JSON

REST APIs commonly exchange data using JSON.

Example

```json
{
    "customer_id":"123",

    "first_name":"Maneesh"
}
```

---

# Stateless

REST APIs do not remember previous requests.

Every request should contain all required information.

Example

```
Request 1

↓

Independent

Request 2

↓

Independent
```

The server should not rely on memory from previous requests.

---

# REST in ShopSphere

Customer Registration

```
Browser

↓

POST /customers

↓

Router

↓

Service

↓

Repository

↓

PostgreSQL

↓

Response

↓

Browser
```

---

# REST in Data Engineering

Typical Source System

```
Salesforce

↓

REST API

↓

Python

↓

JSON

↓

S3

↓

Snowflake
```

Exactly the architecture we will build.

---

# REST Best Practices

- Use nouns in URLs
- Use correct HTTP methods
- Return proper status codes
- Validate input
- Keep APIs stateless
- Version APIs when necessary
- Use consistent response structures

---

# Common Mistakes

❌ /getCustomer

❌ /createProduct

❌ Using POST for everything

❌ Returning different JSON structures

❌ Ignoring status codes

---

# Interview Questions

### What is REST?

REST is an architectural style for designing web APIs.

---

### Difference between PUT and PATCH?

PUT replaces the complete resource.

PATCH updates only specified fields.

---

### Why is REST stateless?

Because each request should contain all information required to process it.

This improves scalability and simplifies server design.

---

### Why shouldn't clients access databases directly?

APIs provide:

- Security
- Validation
- Business Logic
- Access Control
- Scalability

---

### Why use HTTP status codes?

They provide a standardized way for clients to understand the outcome of a request.

---

# Where We Used This in ShopSphere

Health Check

```
GET /health
```

Customer Registration

```
POST /customers
```

Future

```
GET /customers

PUT /customers/{customer_id}

DELETE /customers/{customer_id}
```

---

# Revision Notes

✅ REST is an architecture.

✅ APIs expose Resources.

✅ URLs use nouns.

✅ HTTP methods map to CRUD.

✅ APIs are stateless.

---

# Exercises

1. Design REST endpoints for a Product module.

2. Design REST endpoints for Orders.

3. Explain the difference between PUT and PATCH.

4. Design APIs for updating customer email.

5. Which HTTP status code should be returned when a customer is not found?

---

# Prerequisites

- 003-python-fundamentals.md
- 004-oops.md

---

# Next Chapter

➡️ 006-fastapi.md