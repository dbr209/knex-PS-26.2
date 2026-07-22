from fastapi import APIRouter, Depends

from schemas.product_schemas import ProductCreate, ProductUpdate
from security.dependencies import require_seller
from services.product_service import register_product, list_products, get_product, update_product_service, delete_product_service

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("")
def get_products():
    return list_products()

@router.get("/{id}")
def get_product_route(id: int):
    return get_product(id)

@router.post("")
def create_product(product: ProductCreate, user_is_seller=Depends(require_seller)):
    return register_product(product)

@router.put("/{id}")
def update_product(id: int, product: ProductUpdate, user_is_seller=Depends(require_seller)):
    return update_product_service(id, product)

@router.delete("/{id}")
def delete_product(id: int, user_is_seller=Depends(require_seller)):
    return delete_product_service(id)