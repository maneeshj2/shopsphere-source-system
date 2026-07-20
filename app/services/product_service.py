from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.product import Product
from app.repositories.brand_repository import BrandRepository
from app.repositories.category_repository import CategoryRepository
from app.repositories.product_repository import ProductRepository
from app.schemas.product import (
    ProductCreateRequest,
    ProductCreateResponse,
    ProductDeleteResponse,
    ProductListResponse,
    ProductResponse,
    ProductUpdateRequest,
)


def _build_product_response(
    product: Product,
) -> ProductResponse:
    return ProductResponse(
        product_id=str(product.product_id),
        product_name=product.product_name,
        description=product.description,
        category_id=str(product.category_id),
        brand_id=str(product.brand_id),
        sku=product.sku,
        price=product.price,
        stock_quantity=product.stock_quantity,
        weight=product.weight,
        is_active=product.is_active,
    )


# =====================================
# Create Product
# =====================================

def create_product(
    db: Session,
    request: ProductCreateRequest,
) -> ProductCreateResponse:

    existing_product = ProductRepository.get_product_by_sku(
        db=db,
        sku=request.sku,
    )

    if existing_product:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Product with this SKU already exists.",
        )

    category = CategoryRepository.get_category_by_id(
        db=db,
        category_id=UUID(request.category_id),
    )

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found.",
        )

    brand = BrandRepository.get_brand_by_id(
        db=db,
        brand_id=UUID(request.brand_id),
    )

    if brand is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Brand not found.",
        )

    product = Product(
        product_name=request.product_name,
        description=request.description,
        category_id=UUID(request.category_id),
        brand_id=UUID(request.brand_id),
        sku=request.sku,
        price=request.price,
        stock_quantity=request.stock_quantity,
        weight=request.weight,
        is_active=request.is_active,
    )

    saved = ProductRepository.create_product(
        db=db,
        product=product,
    )

    return ProductCreateResponse(
        product_id=str(saved.product_id),
        message="Product created successfully.",
    )


# =====================================
# Get Product By ID
# =====================================

def get_product_by_id(
    db: Session,
    product_id: UUID,
) -> ProductResponse:

    product = ProductRepository.get_product_by_id(
        db=db,
        product_id=product_id,
    )

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found.",
        )

    return _build_product_response(product)


# =====================================
# Get Products
# =====================================

def get_products(
    db: Session,
    page: int,
    size: int,
) -> ProductListResponse:

    products = ProductRepository.get_products(
        db=db,
        limit=size,
        offset=(page - 1) * size,
    )

    total = ProductRepository.get_total_products(
        db=db,
    )

    return ProductListResponse(
        products=[
            _build_product_response(product)
            for product in products
        ],
        total_records=total,
        page=page,
        size=size,
    )


# =====================================
# Update Product
# =====================================

def update_product(
    db: Session,
    product_id: UUID,
    request: ProductUpdateRequest,
) -> ProductResponse:

    product = ProductRepository.get_product_by_id(
        db=db,
        product_id=product_id,
    )

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found.",
        )

    if request.product_name is not None:
        product.product_name = request.product_name

    if request.description is not None:
        product.description = request.description

    if request.category_id is not None:

        category = CategoryRepository.get_category_by_id(
            db=db,
            category_id=UUID(request.category_id),
        )

        if category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found.",
            )

        product.category_id = UUID(request.category_id)

    if request.brand_id is not None:

        brand = BrandRepository.get_brand_by_id(
            db=db,
            brand_id=UUID(request.brand_id),
        )

        if brand is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Brand not found.",
            )

        product.brand_id = UUID(request.brand_id)

    if request.sku is not None:
        product.sku = request.sku

    if request.price is not None:
        product.price = request.price

    if request.stock_quantity is not None:
        product.stock_quantity = request.stock_quantity

    if request.weight is not None:
        product.weight = request.weight

    if request.is_active is not None:
        product.is_active = request.is_active

    updated = ProductRepository.update_product(
        db=db,
        product=product,
    )

    return _build_product_response(updated)


# =====================================
# Delete Product
# =====================================

def delete_product(
    db: Session,
    product_id: UUID,
) -> ProductDeleteResponse:

    product = ProductRepository.get_product_by_id(
        db=db,
        product_id=product_id,
    )

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found.",
        )

    ProductRepository.delete_product(
        db=db,
        product=product,
    )

    return ProductDeleteResponse(
        message="Product deleted successfully.",
    )