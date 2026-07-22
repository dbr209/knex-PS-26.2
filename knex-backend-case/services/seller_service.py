from repository.order_repository import get_all_orders, get_sales_by_product_id
from repository.product_repository import get_product_by_id
from services.order_mapper import group_orders
from exceptions import not_found

def list_all_orders():
    rows = get_all_orders()

    if not rows:
        return []

    return group_orders(rows)

def list_sales_by_product_id(product_id):
    product = get_product_by_id(product_id)

    if product is None:
        not_found("Produto não encontrado.")

    rows = get_sales_by_product_id(product_id)

    if not rows:
        return {"message": "Este produto ainda não foi vendido."}

    sales = []

    for row in rows:
        sales.append({
            "order_id": row["order_id"],
            "product_id": row["product_id"],
            "product_name": row["product_name"],
            "created_at": row["created_at"],
            "quantity": row["quantity"],
            "unit_price": row["unit_price_in_cents"] / 100
        })

    return sales