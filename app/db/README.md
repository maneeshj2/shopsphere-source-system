# 🛢️ Database Layer (Infrastructure)

The `db` folder contains the database infrastructure required for the application to communicate with PostgreSQL.

Unlike the Repository Layer, this folder does **not** contain business-specific SQL queries.

It is responsible for establishing and managing database connectivity.

---

# 📌 Responsibilities

The Database Layer is responsible for:

- Creating Database Connections
- Managing Database Sessions
- Configuring SQLAlchemy Engine
- Managing Transactions
- Providing reusable database infrastructure

---

# ❌ The Database Layer SHOULD NOT

- Execute business SQL queries
- Contain business logic
- Validate business rules
- Handle HTTP requests
- Return HTTP responses

Those responsibilities belong to other layers.

---

# 📁 Current Files

```
db/

└── database.py
```

Future structure:

```
db/

├── database.py
├── session.py
├── base.py
└── migrations.py
```

As the project grows, more database infrastructure files may be added.

---

# 🔄 Position in the Architecture

```
Browser

    │

    ▼

API Layer

    │

    ▼

Service Layer

    │

    ▼

Repository Layer

    │

    ▼

Database Layer

    │

    ▼

PostgreSQL
```

Notice that the Repository Layer uses the Database Layer.

The Database Layer never calls the Repository Layer.

---

# 🏗️ Why Do We Need This Layer?

Imagine every Repository created its own database connection.

```
Customer Repository

↓

Create Connection

↓

Execute SQL

↓

Close Connection
```

Now imagine 50 repositories doing the same thing.

Lots of duplicate code.

Instead, we centralize all connection management.

```
Customer Repository

↓

Database Layer

↓

PostgreSQL
```

Now every repository shares the same infrastructure.

---

# 💻 Example

The Database Layer creates:

```python
engine = create_engine(DATABASE_URL)
```

and

```python
SessionLocal = sessionmaker(...)
```

The Repository Layer simply uses them.

It doesn't care how the connection was created.

---

# 📦 Components

### Engine

The Engine is responsible for communicating with PostgreSQL.

Think of it as the application's permanent connection manager.

---

### Session

A Session represents a conversation with the database.

Every API request usually gets its own Session.

Example:

```
Request Starts

↓

Open Session

↓

Execute SQL

↓

Commit / Rollback

↓

Close Session
```

---

# 🛍️ Real-World Analogy

Imagine a city.

```
People

↓

Road

↓

Office
```

The road connects people to the office.

It doesn't decide what work people do.

Similarly,

The Database Layer only provides the path to PostgreSQL.

Repositories decide what queries to execute.

---

# 🔄 Difference Between DB Layer and Repository

| Database Layer | Repository Layer |
|---------------|------------------|
| Creates Connection | Executes SQL |
| Creates Session | Reads/Writes Data |
| Infrastructure | Business Data Access |
| Generic | Business Specific |
| Used by all Repositories | Used by Services |

---

# 📖 Naming Convention

Typical files:

```
database.py

session.py

base.py
```

Avoid putting repository code here.

---

# ✅ Best Practices

- Keep connection code centralized
- Reuse Sessions
- Use configuration from `core/`
- Keep this layer independent of business logic

---

# ❌ Common Mistakes

- Writing SQL queries here
- Adding business logic
- Importing API routers
- Creating multiple engines unnecessarily

---

# 🔗 Related Layers

### ⬆ Used By

- Customer Repository
- Product Repository
- Order Repository
- Inventory Repository

### ⬇ Uses

- PostgreSQL
- SQLAlchemy
- Application Configuration

---

# 💼 Interview Questions

### What is the purpose of the Database Layer?

It provides the infrastructure required to connect and communicate with the database.

---

### Why don't we execute SQL here?

Because this layer is responsible only for connection management.

Business-specific SQL belongs in the Repository Layer.

---

### What is SQLAlchemy Engine?

The Engine manages communication between the application and the database.

---

### What is a Session?

A Session is a unit of work used to execute SQL operations within a transaction.

---

# 🛍️ ShopSphere Example

```
Customer Repository

↓

Get Session

↓

Execute INSERT

↓

Commit Transaction

↓

Return Customer ID
```

Notice that the Repository performs the SQL.

The Database Layer only provides the Session.

---

# 🎯 Key Takeaway

The Database Layer is the infrastructure that allows the application to communicate with PostgreSQL.

It does not know anything about Customers, Products, or Orders.

Its responsibility is simply to provide reliable database connectivity that every Repository can reuse.