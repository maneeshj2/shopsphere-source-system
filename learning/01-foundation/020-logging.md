# 📝 Logging Fundamentals

## Goal

Understand why logging is essential, how enterprise applications use logs, and how to implement structured logging in FastAPI.

This chapter explains logging using the ShopSphere project.

---

# What is Logging?

Logging is the process of recording important events that happen inside an application.

Logs help developers understand

- What happened?
- When did it happen?
- Who triggered it?
- Why did it fail?

Without logs, debugging production issues becomes extremely difficult.

---

# Why Do We Need Logging?

Imagine a customer reports

> "I couldn't place an order."

Without logs

```
Developer

↓

Guess

↓

Guess Again

↓

Still No Idea
```

With logs

```
09:15:21

POST /orders

Customer ID : 12345

Inventory Check Failed

Product Out of Stock
```

The issue becomes obvious.

---

# Real World Analogy

Imagine an aircraft.

Every important event is recorded in the **Black Box**.

If something goes wrong,

Engineers analyze the logs.

Application logs work exactly the same way.

---

# ShopSphere Logging Flow

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

Logs Written
```

Logs can be written at every layer.

---

# What Should We Log?

Good Examples

- Application Started
- Customer Registered
- Login Successful
- Payment Completed
- Order Created
- Inventory Updated

---

# What Should We NEVER Log?

Never log

- Passwords
- Password Hashes
- Credit Card Numbers
- JWT Tokens
- API Secrets
- Database Passwords

Sensitive information should always be protected.

---

# Log Levels

Python provides different log levels.

---

## DEBUG

Detailed information used during development.

Example

```
Executing SQL Query

Customer Object Created

Calling Payment API
```

---

## INFO

Normal application events.

Example

```
Application Started

Customer Registered

Order Created
```

---

## WARNING

Something unexpected happened, but the application can continue.

Example

```
Product Stock Low

Retrying API Call
```

---

## ERROR

An operation failed.

Example

```
Database Connection Failed

Payment Gateway Timeout
```

---

## CRITICAL

A serious failure that may stop the application.

Example

```
Database Unavailable

Application Cannot Start
```

---

# Logging Example

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Customer created successfully")
```

---

# Logging Flow

```
Application

↓

Logger

↓

Console

↓

Log File

↓

Monitoring Tool
```

---

# ShopSphere Example

Customer Registration

```
INFO

Customer Registration Started

↓

INFO

Email Validation Successful

↓

INFO

Password Hashed

↓

INFO

Customer Created

↓

INFO

Response Returned
```

---

# Logging Errors

Example

```python
try:

    ...

except Exception:

    logger.exception("Customer creation failed")
```

Using

```python
logger.exception()
```

automatically logs the stack trace.

---

# Structured Logging

Instead of

```
Customer Created
```

Prefer

```text
Customer Created

customer_id=12345

email=maneesh@gmail.com
```

Structured logs are easier to search and analyze.

---

# Log Format

A typical log contains

```
Timestamp

Log Level

Module

Message
```

Example

```
2026-07-08 10:35:12

INFO

customer_service

Customer Created
```

---

# Logging in ShopSphere

Future

```
API Request

↓

Request ID

↓

Customer ID

↓

Execution Time

↓

Status Code

↓

Response Time
```

These logs help diagnose performance issues.

---

# Centralized Logging

Enterprise applications often send logs to centralized systems.

Examples

- ELK Stack (Elasticsearch, Logstash, Kibana)
- Splunk
- Datadog
- Grafana Loki
- AWS CloudWatch

Instead of checking multiple servers,

developers search logs from one place.

---

# Correlation IDs

Imagine one request touches

- Customer Service
- Payment Service
- Inventory Service

Every log includes

```
Request ID

ABC123XYZ
```

Now developers can trace the entire request across multiple services.

---

# Logging vs Print()

Never use

```python
print("Customer Created")
```

Instead

```python
logger.info("Customer Created")
```

Why?

Logging provides

- Log Levels
- Timestamps
- Filtering
- File Output
- Integration with Monitoring Tools

---

# Internal Working

```
Application

↓

Logger

↓

Formatter

↓

Console/File

↓

Log Aggregation

↓

Monitoring Dashboard
```

---

# Enterprise Perspective

Large companies generate millions of log entries every day.

Logs help answer questions like

- Why did the payment fail?
- Which API is slow?
- Which customer experienced an error?
- Which database query is taking too long?

Without logs, troubleshooting production systems is almost impossible.

---

# Best Practices

- Log meaningful events
- Use appropriate log levels
- Log exceptions with stack traces
- Include contextual information
- Protect sensitive data

---

# Common Mistakes

❌ Using print() instead of logging

❌ Logging passwords

❌ Logging JWT tokens

❌ Logging too much unnecessary information

❌ Ignoring log levels

---

# Comparison

| print() | logging |
|----------|----------|
| Development only | Production Ready |
| No log levels | Multiple log levels |
| No timestamps | Timestamps |
| Console only | Console, Files, Monitoring Tools |
| Difficult to filter | Easy to search |

---

# Interview Questions

### What is logging?

Logging is the process of recording application events to help monitor, debug, and troubleshoot systems.

---

### Why use logging instead of print()?

Logging provides timestamps, log levels, structured output, and integrates with monitoring systems.

---

### What should never be logged?

Sensitive information such as passwords, API keys, JWT tokens, and credit card details.

---

### What is the difference between INFO and ERROR logs?

INFO records normal application events.

ERROR records failures that require attention.

---

### What is structured logging?

Structured logging records logs in a consistent format with fields like customer_id, request_id, and timestamp, making logs easier to search and analyze.

---

# Where We Will Use This in ShopSphere

```
Application Startup

↓

Customer Registration

↓

Login

↓

Order Creation

↓

Inventory Update

↓

Payment Processing
```

Every important business event will be logged.

---

# Revision Notes

✅ Use logging instead of print().

✅ Choose the correct log level.

✅ Never log sensitive information.

✅ Use structured logs.

✅ Logs are essential for debugging production systems.

---

# Exercises

1. Explain the difference between DEBUG and INFO.

2. Why shouldn't passwords be logged?

3. What information should a production log contain?

4. Explain the benefits of structured logging.

5. Why are correlation IDs useful in microservices?

---

# Prerequisites

- FastAPI
- Project Architecture
- Request Lifecycle

---

# Next Chapter

➡️ 021-exception-handling.md