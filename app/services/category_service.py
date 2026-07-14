from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.category import Category
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import (
    CategoryCreateRequest,
    CategoryCreateResponse,
    CategoryDeleteResponse,
    CategoryListResponse,
    CategoryResponse,
    CategoryUpdateRequest,
)


def _build_category_response(category: Category) -> CategoryResponse:
    return CategoryResponse(
        category_id=str(category.category_id),
        category_name=category.category_name,
        description=category.description,
    )


def create_category(
    db: Session,
    request: CategoryCreateRequest,
) -> CategoryCreateResponse:

    existing = CategoryRepository.get_category_by_name(
        db=db,
        category_name=request.category_name,
    )

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Category already exists.",
        )

    category = Category(
        category_name=request.category_name,
        description=request.description,
    )

    saved = CategoryRepository.create_category(
        db=db,
        category=category,
    )

    return CategoryCreateResponse(
        category_id=str(saved.category_id),
        message="Category created successfully.",
    )


def get_category_by_id(
    db: Session,
    category_id: UUID,
) -> CategoryResponse:

    category = CategoryRepository.get_category_by_id(
        db=db,
        category_id=category_id,
    )

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found.",
        )

    return _build_category_response(category)


def get_categories(
    db: Session,
    page: int,
    size: int,
) -> CategoryListResponse:

    categories = CategoryRepository.get_categories(
        db=db,
        limit=size,
        offset=(page - 1) * size,
    )

    total = CategoryRepository.get_total_categories(db=db)

    return CategoryListResponse(
        categories=[
            _build_category_response(category)
            for category in categories
        ],
        total_records=total,
        page=page,
        size=size,
    )


def update_category(
    db: Session,
    category_id: UUID,
    request: CategoryUpdateRequest,
) -> CategoryResponse:

    category = CategoryRepository.get_category_by_id(
        db=db,
        category_id=category_id,
    )

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found.",
        )

    if request.category_name is not None:
        category.category_name = request.category_name

    if request.description is not None:
        category.description = request.description

    updated = CategoryRepository.update_category(
        db=db,
        category=category,
    )

    return _build_category_response(updated)


def delete_category(
    db: Session,
    category_id: UUID,
) -> CategoryDeleteResponse:

    category = CategoryRepository.get_category_by_id(
        db=db,
        category_id=category_id,
    )

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found.",
        )

    CategoryRepository.delete_category(
        db=db,
        category=category,
    )

    return CategoryDeleteResponse(
        message="Category deleted successfully.",
    )