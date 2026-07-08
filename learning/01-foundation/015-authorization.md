# 🛡️ Authorization Fundamentals

## Goal

Understand what Authorization is, why it is required, and how applications control what authenticated users are allowed to do.

This chapter explains Authorization using the ShopSphere project.

---

# What is Authorization?

Authorization is the process of determining **what an authenticated user is allowed to access or perform**.

Authentication proves your identity.

Authorization determines your permissions.

---

# Authentication vs Authorization

Authentication

```
Who are you?
```

Authorization

```
What are you allowed to do?
```

Example

```
Login

↓

Identity Verified

↓

Authentication

↓

Check User Role

↓

Authorization

↓

Allow Access
```

---

# Why Do We Need Authorization?

Imagine every logged-in user could access everything.

Customer

↓

Delete Products

↓

Refund Payments

↓

Change Prices

↓

Delete Orders

Obviously this should never happen.

Instead

```
Customer

↓

Can View Products

Can Place Orders

Can View Own Profile
```

Admin

↓

Can Manage Products

Can View All Orders

Can Process Refunds

Can Manage Users

---

# Real World Analogy

Imagine an office building.

Reception verifies your identity.

↓

You receive an access card.

↓

The card determines

- Which floor you can enter
- Which rooms you can access

Authentication

↓

Identity

Authorization

↓

Access

---

# ShopSphere Example

Customer Login

↓

JWT

↓

Role

↓

customer

↓

Customer APIs Only

Admin Login

↓

JWT

↓

Role

↓

admin

↓

Admin APIs

---

# Authorization Flow

```
User

↓

JWT

↓

FastAPI

↓

Verify JWT

↓

Extract Role

↓

Check Permission

↓

API Executes
```

---

# User Roles

Typical roles

```
Customer

Admin

Warehouse Staff

Support Agent

Finance
```

Each role has different permissions.

---

# Role-Based Access Control (RBAC)

Most enterprise applications use RBAC.

Example

| Role | Permissions |
|------|-------------|
| Customer | View own profile, place orders |
| Admin | Manage products, users, orders |
| Warehouse | Update inventory |
| Finance | View payments, process refunds |

---

# Resource Ownership

Sometimes the role is not enough.

Example

Customer

↓

GET /orders/123

Question

Does this order belong to this customer?

Authorization must check ownership as well.

---

# Example

Customer A

```
GET /orders/101
```

Order belongs to Customer A

↓

Allowed

---

Customer B

```
GET /orders/101
```

Order belongs to Customer A

↓

403 Forbidden

---

# Permission Check

```
JWT

↓

Role

↓

Customer

↓

Requested API

↓

/admin/products

↓

Permission Denied
```

---

# HTTP Status Codes

Authentication Failure

```
401 Unauthorized
```

Meaning

You are not logged in.

---

Authorization Failure

```
403 Forbidden
```

Meaning

You are logged in,

but you don't have permission.

---

# FastAPI Authorization

Future

```python
@router.get("/admin/products")
```

↓

Dependency

↓

Verify JWT

↓

Verify Role

↓

Execute API

---

# Internal Working

```
Request

↓

JWT Verification

↓

Read User Role

↓

Read API Permission

↓

Allowed?

↓

Yes

↓

Execute

↓

No

↓

403
```

---

# ShopSphere Example

Customer

↓

POST /orders

↓

Allowed

Customer

↓

DELETE /products

↓

Forbidden

Admin

↓

DELETE /products

↓

Allowed

---

# Authorization Strategies

## Role-Based Access Control (RBAC)

Permission depends on role.

Example

```
Admin

↓

Everything
```

---

## Attribute-Based Access Control (ABAC)

Permission depends on attributes.

Example

```
Department

Location

Time

Project
```

---

## Ownership-Based Authorization

Permission depends on ownership.

Example

```
Customer

↓

Own Orders

Only
```

---

# Enterprise Perspective

Most companies combine multiple approaches.

Example

```
JWT

↓

Role

↓

Department

↓

Ownership

↓

Permission

↓

API
```

---

# Best Practices

- Apply the principle of least privilege
- Never trust data from the client
- Verify permissions on every protected request
- Separate Authentication and Authorization
- Use roles and permissions consistently

---

# Common Mistakes

❌ Checking permissions only in the frontend

❌ Assuming authenticated users can access everything

❌ Hardcoding roles throughout the application

❌ Returning sensitive data before checking permissions

---

# Comparison

| Authentication | Authorization |
|---------------|---------------|
| Identity | Permissions |
| Login | Access Control |
| JWT Validation | Role Check |
| Happens First | Happens Second |

---

# Interview Questions

### What is Authorization?

Authorization determines what an authenticated user is allowed to access.

---

### What is the difference between Authentication and Authorization?

Authentication verifies identity.

Authorization verifies permissions.

---

### What is RBAC?

Role-Based Access Control is an authorization model where permissions are assigned to roles instead of individual users.

---

### Why is 403 different from 401?

401 means the user is not authenticated.

403 means the user is authenticated but lacks permission.

---

### Should Authorization be implemented only in the frontend?

No.

Authorization must always be enforced on the backend because frontend checks can be bypassed.

---

# Where We Will Use This in ShopSphere

Customer

↓

View Own Orders

Update Own Profile

Create Orders

Admin

↓

Manage Products

Manage Inventory

View All Customers

Warehouse

↓

Update Inventory

Finance

↓

View Payments

Issue Refunds

---

# Revision Notes

✅ Authentication identifies users.

✅ Authorization controls permissions.

✅ RBAC is the most common authorization model.

✅ 401 = Not Authenticated.

✅ 403 = Authenticated but Forbidden.

---

# Exercises

1. Explain the difference between Authentication and Authorization.

2. Design roles for ShopSphere.

3. Which APIs should only Admins access?

4. Why is ownership checking important?

5. Explain the difference between 401 and 403.

---

# Prerequisites

- Authentication
- JWT
- Password Hashing

---

# Next Chapter

➡️ 016-dependency-injection.md