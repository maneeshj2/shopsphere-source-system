# 🐍 Python Fundamentals for Backend Development

## Goal

Understand the Python concepts required to build backend applications with FastAPI.

This guide focuses only on the Python features used in ShopSphere.

---

# Why Python?

Python is one of the most popular programming languages for:

- Backend Development
- Data Engineering
- Data Science
- Machine Learning
- Automation
- DevOps

Its simplicity and rich ecosystem make it an excellent choice for enterprise applications.

---

# Variables

Variables store values.

Example

```python
name = "Maneesh"

age = 32

salary = 4000000
```

Python automatically determines the data type.

---

# Data Types

```
int

float

str

bool

list

tuple

dict

set

None
```

Example

```python
customer = {
    "first_name": "Maneesh",
    "age": 32
}
```

---

# Functions

Functions group reusable logic.

Example

```python
def greet():

    print("Hello")
```

Calling

```python
greet()
```

---

# Function Parameters

```python
def greet(name):

    print(f"Hello {name}")
```

Calling

```python
greet("Maneesh")
```

---

# Return Statement

Functions may return values.

```python
def add(a, b):

    return a + b
```

Example

```python
result = add(10,20)
```

---

# Scope

Variables defined inside a function are local.

```python
def demo():

    age = 20
```

Outside the function,

```
age
```

does not exist.

---

# Lists

Ordered collection.

```python
customers = [

    "John",

    "Maneesh",

    "Divya"
]
```

---

# Dictionaries

Key-value pairs.

```python
customer = {

    "first_name":"Maneesh",

    "city":"Haldwani"
}
```

Access

```python
customer["city"]
```

---

# Loops

For Loop

```python
for customer in customers:

    print(customer)
```

While Loop

```python
while condition:

    ...
```

---

# Conditions

```python
if age >= 18:

    print("Adult")

else:

    print("Minor")
```

---

# Modules

Python files are modules.

Example

```
customer_service.py
```

Import

```python
from app.services import customer_service
```

---

# Packages

Folders containing Python modules.

Example

```
services/

customer_service.py
```

Python treats this folder as a package.

---

# __init__.py

Marks a folder as a Python package.

Example

```
services/

__init__.py
```

---

# Classes

Classes define blueprints.

Example

```python
class Customer:

    pass
```

Objects are created from classes.

We'll study this in detail in

```
004-oops.md
```

---

# Decorators

Decorators modify the behavior of functions.

Example

```python
@router.post("/")
```

Equivalent to

```python
create_customer = router.post("/")(create_customer)
```

We studied this while learning FastAPI.

---

# Type Hints

Example

```python
def add(a: int, b: int) -> int:

    return a+b
```

Benefits

- Better readability

- Better IDE support

- Static type checking

---

# Imports

Example

```python
from app.schemas.customer import CustomerCreateRequest
```

Avoid

```python
import *
```

---

# Exceptions

Example

```python
try:

    ...

except Exception:

    ...
```

Used to handle runtime errors.

---

# Virtual Environment

Each project should have its own environment.

Example

```
.venv
```

Benefits

- Dependency isolation

- Version management

- Reproducible projects

---

# Requirements

Store dependencies in

```
requirements.txt
```

Generate

```bash
pip freeze > requirements.txt
```

Install

```bash
pip install -r requirements.txt
```

---

# Python Features Used in ShopSphere

✔ Functions

✔ Modules

✔ Packages

✔ Imports

✔ Decorators

✔ Type Hints

✔ Classes

✔ Virtual Environment

✔ Exception Handling

---

# Best Practices

- Use meaningful variable names

- Keep functions small

- Use type hints

- Avoid duplicate code

- Organize code into modules

- Follow PEP 8

---

# Common Mistakes

❌ Very large functions

❌ Global variables

❌ Circular imports

❌ Ignoring exceptions

❌ No type hints

---

# Interview Questions

### Why Python for Backend?

Simple syntax, rich ecosystem, high productivity, and excellent framework support.

---

### What is a Module?

A Python file containing code.

---

### What is a Package?

A folder containing Python modules.

---

### What is __init__.py?

Marks a directory as a Python package.

---

### Why use Type Hints?

Better readability, IDE support, and maintainability.

---

### What is a Decorator?

A function that modifies another function without changing its source code.

---

# Where We Used This in ShopSphere

Functions

```
create_customer()
```

Modules

```
customer_service.py
```

Packages

```
services/

schemas/

repositories/
```

Decorators

```python
@router.post("/")
```

Type Hints

```python
customer: CustomerCreateRequest
```

Imports

```python
from app.schemas.customer import ...
```

---

# Revision Notes

✅ Functions

✅ Modules

✅ Packages

✅ Decorators

✅ Imports

✅ Type Hints

---

# Prerequisites

- Basic Programming

---

# Next Chapter

➡️ 004-oops.md