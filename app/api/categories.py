from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.category import (
    CategoryCreateRequest,
    CategoryCreateResponse,
    CategoryDeleteResponse,
    CategoryListResponse,
    CategoryResponse,
    CategoryUpdateRequest,
)
from app.services.category_service import (
    create_category,
    delete_category,
    get_categories,
    get_category_by_id,
    update_category,
)

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


# =====================================
# Create Category
# =====================================

@router.post(
    "",
    response_model=CategoryCreateResponse,
    status_code=201,
)
def register_category(
    request: CategoryCreateRequest,
    db: Session = Depends(get_db),
):
    return create_category(
        db=db,
        request=request,
    )


# =====================================
# Get Category By ID
# =====================================

@router.get(
    "/{category_id}",
    response_model=CategoryResponse,
)
def fetch_category_by_id(
    category_id: UUID,
    db: Session = Depends(get_db),
):
    return get_category_by_id(
        db=db,
        category_id=category_id,
    )


# =====================================
# Get Categories
# =====================================

@router.get(
    "",
    response_model=CategoryListResponse,
)
def fetch_categories(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db),
):
    return get_categories(
        db=db,
        page=page,
        size=size,
    )


# =====================================
# Update Category
# =====================================

@router.put(
    "/{category_id}",
    response_model=CategoryResponse,
)
def update_category_by_id(
    category_id: UUID,
    request: CategoryUpdateRequest,
    db: Session = Depends(get_db),
):
    return update_category(
        db=db,
        category_id=category_id,
        request=request,
    )


# =====================================
# Delete Category
# =====================================

@router.delete(
    "/{category_id}",
    response_model=CategoryDeleteResponse,
)
def delete_category_by_id(
    category_id: UUID,
    db: Session = Depends(get_db),
):
    return delete_category(
        db=db,
        category_id=category_id,
    )