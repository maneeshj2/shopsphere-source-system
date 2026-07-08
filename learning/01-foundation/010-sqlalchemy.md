# 💾 Database Sessions

## Goal

Understand what a Database Session is, why every backend application uses it, and how it manages communication between the application and PostgreSQL.

This chapter explains Database Sessions using the ShopSphere project.

---

# What is a Database Session?

A Database Session represents a conversation between your application and the database.

Think of it as a temporary workspace where database operations happen before they become permanent.

---

# Why Do We Need Sessions?

Imagine writing directly to PostgreSQL.

```
INSERT Customer

↓

Immediately Saved
```

What happens if the next operation fails?

Example

```
Create Customer

↓

Create Order

↓

Payment Fails
```

Now

Customer Exists

Order Doesn't Exist

Payment Doesn't Exist

The database is inconsistent.

---

# With Sessions

```
Session Starts

↓

Create Customer

↓

Create Order

↓

Create Payment

↓

Everything Successful?

↓

YES

↓

COMMIT

↓

Data Saved
```

If something fails

↓

ROLLBACK

↓

Nothing Saved

---

# Real World Analogy

Imagine writing an email.

```
Open Gmail

↓

Write Email

↓

Edit

↓

Attach File

↓

Review

↓

Send
```

Until you click **Send**,

nothing reaches the recipient.

The Session works the same way.

```
Database Session

↓

INSERT

↓

UPDATE

↓

DELETE

↓

COMMIT
```

Until Commit,

nothing is permanently stored.

---

# Session Lifecycle

```
Request Arrives

↓

Open Session

↓

Execute SQL

↓

Commit

↓

Close Session
```

Every API request usually gets its own Session.

---

# ShopSphere Flow

```
POST /customers

↓

Router

↓

Service

↓

Repository

↓

Database Session

↓

INSERT

↓

COMMIT

↓

Customer Created
```

---

# What Happens Internally?

```
Application

↓

Session Created

↓

Transaction Started

↓

SQL Executed

↓

Rows Modified

↓

Commit

↓

Transaction Ends

↓

Session Closed
```

---

# Session vs Connection

These two terms are often confused.

Connection

↓

Physical connection to PostgreSQL

Session

↓

Logical conversation using that connection

One connection can create many sessions over time.

---

# Session Responsibilities

A Session

- Tracks changes
- Executes SQL
- Starts transactions
- Commits transactions
- Rolls back failed transactions
- Closes database resources

---

# Commit

Commit makes changes permanent.

Example

```
INSERT Customer

↓

Commit

↓

Customer Saved
```

Without Commit,

another application cannot see the new data.

---

# Rollback

Rollback cancels everything done in the current transaction.

Example

```
INSERT Customer

↓

INSERT Order

↓

Payment Failed

↓

ROLLBACK
```

Result

No Customer

No Order

Database remains consistent.

---

# Multiple Operations

Imagine creating an order.

```
Session

↓

Insert Order

↓

Insert Order Items

↓

Reduce Inventory

↓

Insert Payment

↓

Commit
```

All succeed together.

Or

Nothing succeeds.

---

# Auto Commit vs Manual Commit

Auto Commit

```
Every SQL

↓

Immediately Saved
```

Manual Commit

```
Multiple SQL Statements

↓

Commit Once
```

Enterprise applications almost always use manual commits.

---

# SQLAlchemy Session

Example

```python
SessionLocal = sessionmaker(...)
```

Every API request gets

```python
db = SessionLocal()
```

The Repository uses this Session to execute SQL.

---

# Typical Flow

```python
db.add(customer)

db.commit()

db.refresh(customer)
```

Meaning

```
Add Object

↓

Save Changes

↓

Reload Object
```

---

# Why Close Sessions?

Open Sessions consume resources.

Good Practice

```
Open Session

↓

Work

↓

Close Session
```

Never leave Sessions open.

---

# Session in ShopSphere

Current

```
Customer API

↓

Repository

↓

PostgreSQL Session
```

Future

```
Order Service

↓

Multiple Repositories

↓

Same Session

↓

Commit Once
```

---

# Enterprise Perspective

Large applications process thousands of requests.

Each request gets

```
New Session

↓

Business Logic

↓

Commit

↓

Close
```

This keeps requests isolated.

---

# Best Practices

- One Session per request
- Commit only after success
- Rollback on failure
- Always close Sessions
- Don't share Sessions between requests

---

# Common Mistakes

❌ Forgetting commit()

❌ Forgetting rollback()

❌ Forgetting close()

❌ Sharing one Session across users

❌ Opening unnecessary Sessions

---

# Comparison

| Connection | Session |
|------------|---------|
| Physical connection | Logical conversation |
| Created by Engine | Created from Connection |
| Expensive | Lightweight |
| Reused | Short-lived |

---

# Interview Questions

### What is a Database Session?

A Database Session represents a conversation between the application and the database, allowing multiple operations to be executed as a single unit of work.

---

### Why do we need Sessions?

Sessions provide transaction management, consistency, rollback support, and efficient resource management.

---

### What is Commit?

Commit permanently saves all changes made during the current transaction.

---

### What is Rollback?

Rollback undoes all uncommitted changes in the current transaction.

---

### Why should Sessions be short-lived?

Long-lived Sessions consume resources, increase the risk of stale data, and can lead to locking and performance issues.

---

# Where We Will Use This in ShopSphere

Customer Registration

```
Open Session

↓

Check Email

↓

Insert Customer

↓

Commit

↓

Close Session
```

Future

Order Creation

```
Open Session

↓

Insert Order

↓

Insert Items

↓

Reduce Inventory

↓

Create Payment

↓

Commit

↓

Close Session
```

---

# Revision Notes

✅ Session = Conversation

✅ Commit = Save

✅ Rollback = Undo

✅ One Session per Request

✅ Always Close Sessions

---

# Exercises

1. Explain the difference between a Session and a Connection.

2. Why is commit() required?

3. What happens if commit() is never called?

4. Why do we call rollback() after an error?

5. Draw the complete Session lifecycle.

---

# Prerequisites

- PostgreSQL
- Repository Pattern

---

# Next Chapter

➡️ 011-sqlalchemy.md