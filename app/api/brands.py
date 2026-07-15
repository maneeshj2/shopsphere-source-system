from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.brand import (
    BrandCreateRequest,
    BrandCreateResponse,
    BrandDeleteResponse,
    BrandListResponse,
    BrandResponse,
    BrandUpdateRequest,
)
from app.services.brand_service import (
    create_brand,
    delete_brand,
    get_brand_by_id,
    get_brands,
    update_brand,
)

router = APIRouter(
    prefix="/brands",
    tags=["Brands"],
)


# =====================================
# Create Brand
# =====================================

@router.post(
    "",
    response_model=BrandCreateResponse,
    status_code=201,
)
def register_brand(
    request: BrandCreateRequest,
    db: Session = Depends(get_db),
):
    return create_brand(
        db=db,
        request=request,
    )


# =====================================
# Get Brand By ID
# =====================================

@router.get(
    "/{brand_id}",
    response_model=BrandResponse,
)
def fetch_brand_by_id(
    brand_id: UUID,
    db: Session = Depends(get_db),
):
    return get_brand_by_id(
        db=db,
        brand_id=brand_id,
    )


# =====================================
# Get Brands
# =====================================

@router.get(
    "",
    response_model=BrandListResponse,
)
def fetch_brands(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db),
):
    return get_brands(
        db=db,
        page=page,
        size=size,
    )


# =====================================
# Update Brand
# =====================================

@router.put(
    "/{brand_id}",
    response_model=BrandResponse,
)
def update_brand_by_id(
    brand_id: UUID,
    request: BrandUpdateRequest,
    db: Session = Depends(get_db),
):
    return update_brand(
        db=db,
        brand_id=brand_id,
        request=request,
    )


# =====================================
# Delete Brand
# =====================================

@router.delete(
    "/{brand_id}",
    response_model=BrandDeleteResponse,
)
def delete_brand_by_id(
    brand_id: UUID,
    db: Session = Depends(get_db),
):
    return delete_brand(
        db=db,
        brand_id=brand_id,
    )