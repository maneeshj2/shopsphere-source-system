from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.product import (
    ProductCreateRequest,
    ProductCreateResponse,
    ProductDeleteResponse,
    ProductListResponse,
    ProductResponse,
    ProductUpdateRequest,
)
from app.services.product_service import (
    create_product,
    delete_product,
    get_product_by_id,
    get_products,
    update_product,
)

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


# =====================================
# Create Product
# =====================================

@router.post(
    "",
    response_model=ProductCreateResponse,
    status_code=201,
)
def register_product(
    request: ProductCreateRequest,
    db: Session = Depends(get_db),
):
    return create_product(
        db=db,
        request=request,
    )


# =====================================
# Get Product By ID
# =====================================

@router.get(
    "/{product_id}",
    response_model=ProductResponse,
)
def fetch_product_by_id(
    product_id: UUID,
    db: Session = Depends(get_db),
):
    return get_product_by_id(
        db=db,
        product_id=product_id,
    )


# =====================================
# Get Products
# =====================================

@router.get(
    "",
    response_model=ProductListResponse,
)
def fetch_products(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db),
):
    return get_products(
        db=db,
        page=page,
        size=size,
    )


# =====================================
# Update Product
# =====================================

@router.put(
    "/{product_id}",
    response_model=ProductResponse,
)
def update_product_by_id(
    product_id: UUID,
    request: ProductUpdateRequest,
    db: Session = Depends(get_db),
):
    return update_product(
        db=db,
        product_id=product_id,
        request=request,
    )


# =====================================
# Delete Product
# =====================================

@router.delete(
    "/{product_id}",
    response_model=ProductDeleteResponse,
)
def delete_product_by_id(
    product_id: UUID,
    db: Session = Depends(get_db),
):
    return delete_product(
        db=db,
        product_id=product_id,
    )