# Business Process

## Customer Purchase Journey

1. Customer opens Website or Mobile App.
2. Customer browses products.
3. Customer searches products.
4. Customer views product details.
5. Customer adds products to cart.
6. Customer updates cart quantity.
7. Customer proceeds to checkout.
8. Customer logs in or registers.
9. Customer selects delivery address.
10. Customer applies coupon (optional).
11. Customer selects payment method.
12. Payment is initiated.
13. Payment succeeds.
14. Inventory is reserved.
15. Order is created.
16. Invoice is generated.
17. Warehouse is allocated.
18. Pick list is generated.
19. Warehouse picks products.
20. Warehouse packs products.
21. Shipment is created.
22. Courier is assigned.
23. Shipment is dispatched.
24. Order is delivered.
25. Customer submits product review.

---

## Alternate Flows

### Payment Failure

- Retry Payment
- Cancel Payment

### Out of Stock

- Notify Customer
- Refund Payment

### Order Cancellation

Before Shipment

- Release Inventory
- Refund Customer

After Shipment

- Customer creates Return Request

### Return Process

Return Requested

↓

Pickup Scheduled

↓

Warehouse Inspection

↓

Refund

↓

Inventory Updated