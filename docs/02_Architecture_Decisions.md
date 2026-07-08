# Architecture Decision Records

## ADR-001

### Decision

Use API-First Architecture.

### Reason

The Analytics Platform should consume REST APIs instead of directly connecting to PostgreSQL.

---

## ADR-002

### Decision

Separate Operational System and Analytics Platform into independent repositories.

### Reason

Simulates independent engineering teams.

---

## ADR-003

### Decision

Use PostgreSQL for local development.

### Reason

Represents Amazon Aurora PostgreSQL used in production.

---

## ADR-004

### Decision

Use Docker for local development.

### Reason

Ensures environment consistency across machines.

---

## ADR-005

### Decision

Maintain separate OLTP and OLAP systems.

### Reason

Operational systems support transactions.

Analytics platforms support reporting.

---

## ADR-006

### Decision

Expose Versioned APIs.

Example

/api/v1/products

Reason

Supports backward compatibility.

---

## ADR-007

### Decision

Analytics Platform will never directly access PostgreSQL.

Reason

All integrations occur through REST APIs.

---

## ADR-008

### Decision

Maintain historical tables instead of overwriting important business events.

Reason

Supports auditing and analytics.