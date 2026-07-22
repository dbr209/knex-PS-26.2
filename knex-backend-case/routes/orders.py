from fastapi import APIRouter, Depends

from security.dependencies import require_client
from schemas.order_schemas import OrderCreate, OrderItemCreate
from services.order_service import create_order_service, list_orders_by_user_id

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("")
def create_order(order: OrderCreate, current_user=Depends(require_client)):
    return create_order_service(order, current_user)

@router.get("")
def list_orders(current_user=Depends(require_client)):
    return list_orders_by_user_id(current_user["id"])
