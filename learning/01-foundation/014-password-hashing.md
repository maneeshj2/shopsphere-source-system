# 🔒 Password Hashing

## Goal

Understand why passwords should never be stored in plain text, how password hashing works, and how modern backend applications securely verify user passwords.

This chapter explains password hashing using the ShopSphere project.

---

# What is Password Hashing?

Password hashing is the process of converting a password into a fixed-length string using a one-way cryptographic algorithm.

Example

Password

```
Password@123
```

Hash

```
$2b$12$9EZn8...
```

Notice

You cannot recover the original password from the hash.

---

# Why Can't We Store Passwords?

Imagine our database gets hacked.

Database

```
email

password
```

If passwords are stored as plain text

```
Password123

Admin123

Hello@123
```

Attackers immediately know every user's password.

This is one of the biggest security mistakes a company can make.

---

# Correct Approach

Store

```
email

password_hash
```

Example

```
maneesh@gmail.com

↓

$2b$12$XhG...
```

Even database administrators should never know a user's password.

---

# Real World Analogy

Imagine placing a document inside a paper shredder.

```
Password

↓

Shredder

↓

Tiny Pieces
```

You can shred the paper.

You cannot reconstruct it perfectly.

Hashing works similarly.

---

# Hashing vs Encryption

Many people confuse these.

Hashing

```
Password

↓

Hash

↓

One Way
```

Encryption

```
Password

↓

Encrypted

↓

Decrypt

↓

Original Password
```

Passwords should be hashed.

Not encrypted.

---

# Properties of a Good Hash

A good hash should be

- One Way
- Deterministic
- Fast to Verify
- Difficult to Reverse
- Resistant to Collisions

---

# Password Verification

User enters

```
Password@123
```

Application

↓

Hash Password

↓

Compare with Stored Hash

If both hashes match

↓

Login Successful

Notice

We never compare plain text passwords.

---

# Internal Working

```
User Types Password

↓

Hash Function

↓

Generated Hash

↓

Compare

↓

Stored Hash

↓

Match?

↓

Login Success
```

---

# Why Same Password Doesn't Always Produce Same Hash

Modern algorithms use

**Salt**

Example

```
Password@123

↓

Salt Added

↓

Hash Generated
```

Each user gets a unique salt.

So

```
Password@123
```

for two users produces

different hashes.

---

# What is Salt?

Salt is random data added before hashing.

Example

```
Password

+

Random Salt

↓

Hash
```

Benefits

- Prevents Rainbow Table attacks
- Prevents duplicate hashes
- Improves security

---

# Popular Password Hashing Algorithms

Good

- bcrypt
- Argon2
- scrypt

Avoid

- MD5
- SHA1

These are no longer considered secure for password storage.

---

# bcrypt

ShopSphere will use

```
bcrypt
```

Why?

- Battle-tested
- Automatic Salt
- Slow by design
- Widely adopted

---

# Login Flow

```
POST /login

↓

Find Customer

↓

Read password_hash

↓

Verify Password

↓

Generate JWT

↓

Return Token
```

---

# Registration Flow

```
Customer Registration

↓

Receive Password

↓

Hash Password

↓

Store password_hash

↓

Discard Original Password
```

The original password is never stored.

---

# ShopSphere Example

Incoming Request

```json
{
    "email":"maneesh@gmail.com",
    "password":"Password@123"
}
```

Service Layer

↓

```python
hashed_password = hash_password(password)
```

Repository

↓

Stores

```
password_hash
```

Database

↓

```
$2b$12$....
```

---

# FastAPI Implementation

Future

```python
hashed_password = bcrypt.hashpw(...)
```

Verification

```python
bcrypt.checkpw(...)
```

Notice

We never compare strings directly.

---

# Enterprise Perspective

Every major company follows this approach.

Amazon

↓

bcrypt / Argon2

Google

↓

Secure Password Hashing

Netflix

↓

Password Hash + Salt

Nobody stores plain text passwords.

---

# Best Practices

- Never store plain text passwords
- Use bcrypt or Argon2
- Hash passwords immediately
- Never log passwords
- Always use HTTPS

---

# Common Mistakes

❌ Storing passwords directly

❌ Using MD5

❌ Using SHA1

❌ Logging passwords

❌ Sending passwords back in API responses

---

# Comparison

| Hashing | Encryption |
|----------|------------|
| One-way | Two-way |
| Cannot Recover Original | Can Decrypt |
| Password Storage | Data Protection |
| bcrypt | AES |

---

# Interview Questions

### Why shouldn't passwords be stored in plain text?

Because anyone with database access could immediately read user passwords.

---

### What is Password Hashing?

A one-way process that converts a password into a fixed-length hash for secure storage.

---

### Why use Salt?

Salt prevents attackers from using precomputed lookup tables and ensures identical passwords generate different hashes.

---

### Why bcrypt instead of MD5?

bcrypt is specifically designed for password storage, automatically includes a salt, and is intentionally slow to resist brute-force attacks.

---

### During login, do we decrypt the stored password?

No.

The stored hash is never decrypted.

The entered password is hashed and compared with the stored hash.

---

# Where We Will Use This in ShopSphere

Customer Registration

↓

Hash Password

↓

Store Hash

↓

Customer Login

↓

Verify Password

↓

Generate JWT

↓

Access Protected APIs

---

# Revision Notes

✅ Never store passwords.

✅ Store password_hash.

✅ Hashing is one-way.

✅ bcrypt automatically uses Salt.

✅ Compare hashes, not passwords.

---

# Exercises

1. Explain the difference between hashing and encryption.

2. Why is Salt required?

3. Why is MD5 not suitable for passwords?

4. Draw the complete registration flow.

5. Draw the complete login flow.

---

# Prerequisites

- Authentication
- JWT

---

# Next Chapter

➡️ 015-authorization.md