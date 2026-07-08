# Project Background

## Project Name

**ShopSphere Retail Source System**

---

## Company Overview

ShopSphere Retail is a multinational retail company that sells products through multiple channels:

- E-commerce Website
- Mobile Application
- Physical Retail Stores

The company operates multiple warehouses and retail stores across different regions.

---

## Business Problem

The organization currently operates multiple operational systems such as:

- Customer Management
- Product Management
- Inventory Management
- Warehouse Management
- Order Management
- Shipment Management
- Payment Management

Although these systems successfully support day-to-day business operations, the company lacks a centralized enterprise analytics platform.

Business users currently generate reports manually by combining data from multiple systems, resulting in:

- Data silos
- Inconsistent KPIs
- Duplicate reporting
- Poor historical analysis
- Slow report generation
- Limited business visibility

---

## Business Objectives

The organization wants to build a modern analytics platform capable of:

- Creating a Single Source of Truth
- Preserving historical data
- Supporting executive dashboards
- Enabling self-service analytics
- Scaling to millions of transactions
- Supporting near real-time reporting

---

## Proposed Architecture

The operational systems will expose REST APIs.

The Data Engineering platform will consume these APIs to build the enterprise analytics platform.

```

Operational System (PostgreSQL)
        │
        ▼
REST APIs (FastAPI)
        │
        ▼
Python Consumer
        │
        ▼
AWS S3 Landing Zone
        │
        ▼
Snowflake RAW Layer
        │
        ▼
dbt Transformations
        │
        ▼
Business Dashboards

```

---

## Project Goal

This repository represents the **Operational Source System**.

The objective is to build a realistic enterprise retail application that exposes production-style REST APIs for downstream analytics systems.

The operational system is intentionally separated from the analytics platform to simulate real enterprise architecture.