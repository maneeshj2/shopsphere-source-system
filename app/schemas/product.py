from decimal import Decimal

from pydantic import BaseModel, Field


# =====================================
# Create Product
# =====================================

class ProductCreateRequest(BaseModel):
    product_name: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)

    category_id: str
    brand_id: str

    sku: str = Field(..., min_length=1, max_length=100)

    price: Decimal = Field(..., gt=0)

    stock_quantity: int = Field(..., ge=0)

    weight: Decimal = Field(..., gt=0)

    is_active: bool = True


class ProductCreateResponse(BaseModel):
    product_id: str
    message: str


# =====================================
# Update Product
# =====================================

class ProductUpdateRequest(BaseModel):
    product_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )

    description: str | None = None

    category_id: str | None = None

    brand_id: str | None = None

    sku: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    price: Decimal | None = Field(
        default=None,
        gt=0,
    )

    stock_quantity: int | None = Field(
        default=None,
        ge=0,
    )

    weight: Decimal | None = Field(
        default=None,
        gt=0,
    )

    is_active: bool | None = None


# =====================================
# Product Response
# =====================================

class ProductResponse(BaseModel):
    product_id: str
    product_name: str
    description: str

    category_id: str
    brand_id: str

    sku: str

    price: Decimal

    stock_quantity: int

    weight: Decimal

    is_active: bool


# =====================================
# Product List Response
# =====================================

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total_records: int
    page: int
    size: int


# =====================================
# Delete Product
# =====================================

class ProductDeleteResponse(BaseModel):
    message: str