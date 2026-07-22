from fastapi import APIRouter

from services.seller_service import get_all_orders, list_sales_by_product_id

router = APIRouter(
    prefix="/seller",
    tags=["Seller"]
)

@router.get("/sales")
def list_sales():
    return get_all_orders()

@router.get("/sales/{product_id}")
def list_product_sales(product_id: str):
    return list_sales_by_product_id(product_id)