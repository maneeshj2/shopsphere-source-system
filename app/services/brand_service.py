from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.brand import Brand
from app.repositories.brand_repository import BrandRepository
from app.schemas.brand import (
    BrandCreateRequest,
    BrandCreateResponse,
    BrandDeleteResponse,
    BrandListResponse,
    BrandResponse,
    BrandUpdateRequest,
)


def _build_brand_response(
    brand: Brand,
) -> BrandResponse:
    return BrandResponse(
        brand_id=str(brand.brand_id),
        brand_name=brand.brand_name,
        description=brand.description,
    )


# =====================================
# Create Brand
# =====================================

def create_brand(
    db: Session,
    request: BrandCreateRequest,
) -> BrandCreateResponse:

    existing = BrandRepository.get_brand_by_name(
        db=db,
        brand_name=request.brand_name,
    )

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Brand already exists.",
        )

    brand = Brand(
        brand_name=request.brand_name,
        description=request.description,
    )

    saved = BrandRepository.create_brand(
        db=db,
        brand=brand,
    )

    return BrandCreateResponse(
        brand_id=str(saved.brand_id),
        message="Brand created successfully.",
    )


# =====================================
# Get Brand By ID
# =====================================

def get_brand_by_id(
    db: Session,
    brand_id: UUID,
) -> BrandResponse:

    brand = BrandRepository.get_brand_by_id(
        db=db,
        brand_id=brand_id,
    )

    if brand is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Brand not found.",
        )

    return _build_brand_response(brand)


# =====================================
# Get Brands
# =====================================

def get_brands(
    db: Session,
    page: int,
    size: int,
) -> BrandListResponse:

    brands = BrandRepository.get_brands(
        db=db,
        limit=size,
        offset=(page - 1) * size,
    )

    total = BrandRepository.get_total_brands(
        db=db,
    )

    return BrandListResponse(
        brands=[
            _build_brand_response(brand)
            for brand in brands
        ],
        total_records=total,
        page=page,
        size=size,
    )


# =====================================
# Update Brand
# =====================================

def update_brand(
    db: Session,
    brand_id: UUID,
    request: BrandUpdateRequest,
) -> BrandResponse:

    brand = BrandRepository.get_brand_by_id(
        db=db,
        brand_id=brand_id,
    )

    if brand is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Brand not found.",
        )

    if request.brand_name is not None:
        brand.brand_name = request.brand_name

    if request.description is not None:
        brand.description = request.description

    updated = BrandRepository.update_brand(
        db=db,
        brand=brand,
    )

    return _build_brand_response(updated)


# =====================================
# Delete Brand
# =====================================

def delete_brand(
    db: Session,
    brand_id: UUID,
) -> BrandDeleteResponse:

    brand = BrandRepository.get_brand_by_id(
        db=db,
        brand_id=brand_id,
    )

    if brand is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Brand not found.",
        )

    BrandRepository.delete_brand(
        db=db,
        brand=brand,
    )

    return BrandDeleteResponse(
        message="Brand deleted successfully.",
    )