# Entity Catalogue

| Entity | Domain | Type | Description |
|----------|----------|----------|----------------|
| CUSTOMER | Customer | Master | Customer profile |
| CUSTOMER_ADDRESS | Customer | Master | Customer addresses |
| CUSTOMER_WISHLIST | Customer | Transaction | Wishlist |
| CUSTOMER_REVIEW | Customer | Transaction | Product Reviews |
| PRODUCT | Product | Master | Product catalogue |
| CATEGORY | Product | Reference | Product categories |
| BRAND | Product | Reference | Product brands |
| PRODUCT_PRICE_HISTORY | Product | Transaction | Historical pricing |
| SUPPLIER | Supplier | Master | Vendor information |
| PURCHASE_ORDER | Supplier | Transaction | Purchase orders |
| PURCHASE_ORDER_ITEM | Supplier | Transaction | Purchase order items |
| STORE | Employee | Master | Physical stores |
| EMPLOYEE | Employee | Master | Employees |
| ROLE | Employee | Reference | Employee Roles |
| WAREHOUSE | Warehouse | Master | Warehouse information |
| WAREHOUSE_ZONE | Warehouse | Reference | Warehouse zones |
| BIN_LOCATION | Warehouse | Reference | Shelf/Bin locations |
| INVENTORY | Inventory | Master | Current inventory |
| INVENTORY_MOVEMENT | Inventory | Transaction | Inventory history |
| INVENTORY_RESERVATION | Inventory | Transaction | Reserved stock |
| SHOPPING_CART | Order | Transaction | Shopping cart |
| SHOPPING_CART_ITEM | Order | Transaction | Cart items |
| ORDER | Order | Transaction | Customer order |
| ORDER_ITEM | Order | Transaction | Order products |
| ORDER_STATUS_HISTORY | Order | Transaction | Order lifecycle |
| PAYMENT | Payment | Transaction | Payment details |
| PAYMENT_TRANSACTION | Payment | Transaction | Gateway transaction |
| REFUND | Payment | Transaction | Refund details |
| SHIPMENT | Shipment | Transaction | Shipment |
| SHIPMENT_ITEM | Shipment | Transaction | Shipment products |
| TRACKING_EVENT | Shipment | Transaction | Shipment tracking |
| PROMOTION | Promotion | Master | Promotional campaign |
| COUPON | Promotion | Master | Discount coupon |
| COUPON_USAGE | Promotion | Transaction | Coupon redemption |