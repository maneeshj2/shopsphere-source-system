from pydantic import BaseModel, Field


# =====================================
# Create Category
# =====================================

class CategoryCreateRequest(BaseModel):
    category_name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=255)


class CategoryCreateResponse(BaseModel):
    category_id: str
    message: str


# =====================================
# Update Category
# =====================================

class CategoryUpdateRequest(BaseModel):
    category_name: str | None = Field(
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
# Category Response
# =====================================

class CategoryResponse(BaseModel):
    category_id: str
    category_name: str
    description: str


# =====================================
# Category List Response
# =====================================

class CategoryListResponse(BaseModel):
    categories: list[CategoryResponse]
    total_records: int
    page: int
    size: int


# =====================================
# Delete Category
# =====================================

class CategoryDeleteResponse(BaseModel):
    message: str