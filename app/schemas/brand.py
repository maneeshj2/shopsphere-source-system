from pydantic import BaseModel, Field


# =====================================
# Create Brand
# =====================================

class BrandCreateRequest(BaseModel):
    brand_name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=255)


class BrandCreateResponse(BaseModel):
    brand_id: str
    message: str


# =====================================
# Update Brand
# =====================================

class BrandUpdateRequest(BaseModel):
    brand_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    description: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )


# =====================================
# Brand Response
# =====================================

class BrandResponse(BaseModel):
    brand_id: str
    brand_name: str
    description: str


# =====================================
# Brand List Response
# =====================================

class BrandListResponse(BaseModel):
    brands: list[BrandResponse]
    total_records: int
    page: int
    size: int


# =====================================
# Delete Brand
# =====================================

class BrandDeleteResponse(BaseModel):
    message: str