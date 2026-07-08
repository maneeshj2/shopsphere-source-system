# 🏗️ Object-Oriented Programming (OOP)

## Goal

Understand Object-Oriented Programming concepts required for backend development.

This guide focuses on practical OOP concepts used in FastAPI, SQLAlchemy, and enterprise Python applications.

---

# What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm where code is organized around **objects** instead of just functions.

Objects combine:

- Data (Attributes)
- Behavior (Methods)

Example

```
Customer

↓

Name

Email

Phone

Register()

Login()

Update()
```

---

# Why OOP?

Without OOP

```
customer.py

↓

100 Functions

↓

Global Variables
```

As the application grows,

the code becomes difficult to manage.

With OOP

```
Customer

↓

Attributes

↓

Methods
```

Everything related to a Customer stays together.

---

# Real World Analogy

Imagine a Car.

A car has

Attributes

```
Color

Brand

Speed
```

Behavior

```
Start()

Stop()

Accelerate()
```

Similarly,

A Customer object has

Attributes

```
customer_id

email

phone_number
```

Methods

```
register()

update()

delete()
```

---

# Class

A Class is a blueprint.

Example

```python
class Customer:

    pass
```

Nothing is created yet.

---

# Object

An Object is an instance of a class.

```python
customer = Customer()
```

Now memory is allocated.

---

# Attributes

Attributes store information.

```python
class Customer:

    first_name = "Maneesh"
```

---

# Methods

Methods define behavior.

```python
class Customer:

    def greet(self):

        print("Hello")
```

Calling

```python
customer.greet()
```

---

# Constructor

The constructor initializes an object.

```python
class Customer:

    def __init__(self, name):

        self.name = name
```

Creating

```python
customer = Customer("Maneesh")
```

---

# self

self refers to the current object.

Example

```python
self.name
```

means

"This object's name."

Without self,

Python wouldn't know which object you're referring to.

---

# Encapsulation

Keep data and behavior together.

```
Customer

↓

Data

↓

Methods
```

Instead of

```
Customer Data

↓

Different File

↓

Different Functions
```

---

# Inheritance

Reuse an existing class.

Example

```python
class User:

    ...

class Customer(User):

    ...
```

Customer automatically inherits User's behavior.

---

# Polymorphism

Different objects respond to the same method differently.

Example

```python
customer.pay()

supplier.pay()
```

Same method name.

Different implementation.

---

# Abstraction

Hide unnecessary complexity.

Example

```
customer.register()
```

The caller doesn't know

- SQL
- Password Hashing
- Email Sending

Everything happens internally.

---

# Composition

Objects can contain other objects.

Example

```
Order

↓

Customer

↓

Products

↓

Payment
```

Composition is used more often than inheritance in modern applications.

---

# OOP in ShopSphere

Current

```
FastAPI()

↓

APIRouter()

↓

BaseModel()

↓

Settings()
```

Notice something?

Everything is an object.

---

# OOP in FastAPI

Example

```python
app = FastAPI()

router = APIRouter()
```

FastAPI and APIRouter are classes.

We create objects from them.

---

# OOP in Pydantic

```python
class CustomerCreateRequest(BaseModel):
```

BaseModel is a class.

CustomerCreateRequest inherits from it.

---

# OOP in SQLAlchemy

Future

```python
class Customer(Base):
```

Customer inherits from SQLAlchemy's Base class.

---

# OOP in Our Project

Examples

```
FastAPI()

↓

Application Object
```

```
Settings()

↓

Configuration Object
```

```
CustomerCreateRequest()

↓

Schema Object
```

Everything follows OOP.

---

# Why OOP Matters

As applications grow,

OOP provides

- Better Organization
- Code Reuse
- Easier Maintenance
- Better Testing
- Cleaner Architecture

---

# Best Practices

- Keep classes focused
- Prefer composition over inheritance
- Hide implementation details
- Keep methods small
- Use meaningful class names

---

# Common Mistakes

❌ Very large classes

❌ Deep inheritance chains

❌ Global variables

❌ Classes with too many responsibilities

---

# Interview Questions

### What is OOP?

A programming paradigm that organizes code around objects containing data and behavior.

---

### Difference between Class and Object?

Class = Blueprint

Object = Instance

---

### What is Inheritance?

Reusing an existing class.

---

### What is Encapsulation?

Keeping data and methods together inside one class.

---

### What is Polymorphism?

Different objects responding differently to the same method.

---

### Why does Python use self?

To refer to the current object instance.

---

# Where We Used This in ShopSphere

FastAPI

```python
app = FastAPI()
```

APIRouter

```python
router = APIRouter()
```

Pydantic

```python
class CustomerCreateRequest(BaseModel)
```

Settings

```python
settings = Settings()
```

Future

```python
class Customer(Base)
```

---

# Revision Notes

✅ Class

✅ Object

✅ self

✅ Constructor

✅ Inheritance

✅ Composition

---

# Exercises

1. Create a Car class with brand and model attributes.

2. Add a start() method.

3. Create two objects from the same class.

4. Create a User class and inherit Customer from it.

5. Explain why FastAPI() is an object.

---

# Prerequisites

- 003-python-fundamentals.md

---

# Next Chapter

➡️ 005-rest-api.md