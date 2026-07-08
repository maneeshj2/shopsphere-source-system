# 🔐 Authentication Fundamentals

## Goal

Understand what Authentication is, why it is required, and how users prove their identity before accessing protected resources.

This chapter explains Authentication using the ShopSphere project.

---

# What is Authentication?

Authentication is the process of verifying **who a user is**.

The system checks whether the person making the request is actually the person they claim to be.

Think of Authentication as proving your identity.

---

# Authentication vs Authorization

Many people confuse these two terms.

Authentication answers

> Who are you?

Authorization answers

> What are you allowed to do?

Example

```
Login

↓

Identity Verified

↓

Authentication Successful

↓

Check Permissions

↓

Authorization
```

Authentication always happens first.

---

# Why Do We Need Authentication?

Imagine ShopSphere has customer accounts.

Without Authentication

```
Anyone

↓

Update Customer

↓

Delete Orders

↓

View Payments
```

This is obviously dangerous.

Instead

```
User

↓

Login

↓

Identity Verified

↓

Access Granted
```

---

# Real World Analogy

Imagine entering an airport.

```
Show Passport

↓

Identity Verified

↓

Enter Airport
```

Showing the passport is Authentication.

Being allowed into the VIP Lounge is Authorization.

---

# ShopSphere Example

Customer

↓

POST /login

↓

Verify Email

↓

Verify Password

↓

Issue JWT Token

↓

Customer uses Token

↓

Access Protected APIs

---

# Login Flow

```
Browser

↓

POST /login

↓

Authentication Service

↓

Customer Repository

↓

PostgreSQL

↓

Password Verified

↓

Generate JWT

↓

Return Token
```

---

# Credentials

Authentication usually requires credentials.

Examples

```
Email + Password

Username + Password

Google Login

GitHub Login

Fingerprint

Face Recognition
```

In ShopSphere we will use

```
Email

Password
```

---

# Password Verification

Customer enters

```
Password123
```

Database stores

```
$2b$12$...
```

Notice

The original password is **never stored**.

The password entered by the user is hashed and compared with the stored hash.

---

# Authentication Flow

```
User

↓

Email + Password

↓

Service

↓

Repository

↓

Customer Record

↓

Verify Password

↓

Generate JWT

↓

Return Token
```

---

# Protected APIs

Some APIs should be public.

Example

```
GET /products
```

Anyone can view products.

Others require authentication.

Example

```
GET /orders

PUT /customers/profile

POST /payments
```

Only logged-in users should access them.

---

# Session-Based Authentication

Traditional applications often use Sessions.

```
Login

↓

Session Created

↓

Session ID Stored

↓

Browser Sends Session ID
```

Server stores user state.

---

# Token-Based Authentication

Modern APIs usually use Tokens.

```
Login

↓

JWT Generated

↓

Browser Stores Token

↓

Token Sent with Every Request
```

Server remains stateless.

We'll implement this approach in ShopSphere.

---

# Authentication in FastAPI

Future

```
POST /login

↓

Verify Credentials

↓

Return JWT

↓

Protected APIs use Depends()
```

---

# Internal Working

```
Login Request

↓

Read Email

↓

Read Password

↓

Find Customer

↓

Compare Password Hash

↓

Success?

↓

Generate Token

↓

Return Token
```

---

# ShopSphere Architecture

```
Browser

↓

Login API

↓

Authentication Service

↓

Customer Repository

↓

Database

↓

JWT

↓

Browser

↓

Protected APIs
```

---

# Why Separate Authentication Service?

Authentication is its own business process.

It involves

- Finding User
- Verifying Password
- Generating Token
- Handling Failed Logins

Keeping this logic separate makes the application easier to maintain.

---

# Enterprise Perspective

Large companies often delegate Authentication to dedicated identity providers.

Examples

- Auth0
- Okta
- Azure Active Directory
- AWS Cognito
- Keycloak

Your application trusts these providers instead of verifying passwords itself.

---

# Best Practices

- Never store plain text passwords
- Always use HTTPS
- Hash passwords before storing
- Separate Authentication from Authorization
- Use short-lived access tokens

---

# Common Mistakes

❌ Storing plain text passwords

❌ Returning passwords in API responses

❌ Confusing Authentication with Authorization

❌ Creating custom password hashing algorithms

---

# Comparison

| Authentication | Authorization |
|---------------|---------------|
| Who are you? | What can you do? |
| Login | Permissions |
| Identity | Access Control |
| Happens First | Happens After |

---

# Interview Questions

### What is Authentication?

Authentication is the process of verifying the identity of a user or system.

---

### What is the difference between Authentication and Authorization?

Authentication verifies identity.

Authorization determines permissions.

---

### Why shouldn't passwords be stored in plain text?

If the database is compromised, attackers would immediately know every user's password.

Passwords should always be stored as secure hashes.

---

### What are common authentication methods?

- Username & Password
- OAuth
- JWT
- SSO
- Biometrics

---

### Why is Token-based Authentication popular for APIs?

Because it is stateless, scalable, and works well across web, mobile, and microservices.

---

# Where We Will Use This in ShopSphere

```
POST /login

↓

Verify Customer

↓

Generate JWT

↓

Return Token

↓

Customer calls

GET /orders

Authorization: Bearer <token>
```

---

# Revision Notes

✅ Authentication = Identity Verification

✅ Authorization = Permission Check

✅ Login verifies credentials

✅ Passwords are hashed

✅ JWT is commonly used for APIs

---

# Exercises

1. Explain the difference between Authentication and Authorization.

2. Why shouldn't passwords be stored in plain text?

3. Draw the complete login flow.

4. List three APIs that should require authentication.

5. Explain why JWT is better than Session IDs for REST APIs.

---

# Prerequisites

- FastAPI
- Service Layer
- Repository Pattern

---

# Next Chapter

➡️ 013-jwt.md