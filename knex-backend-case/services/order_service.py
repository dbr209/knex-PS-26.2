from database.connection import get_connection
from exceptions import bad_request, not_found

from repository.product_repository import get_product_by_id, mark_product_as_sold, decrease_stock
from repository.order_repository import create_order_repository, get_orders_by_user_id, get_all_orders
from repository.order_item_repository import create_order_item
from services.order_mapper import group_orders

def create_order_service(order, user):
    user_id = user["id"]

    products, total_price = validate_order_products(order.items)

    conn = get_connection()

    try:
        order_id = create_order_repository(conn, user_id, total_price)

        for product, item in zip(products, order.items):

            create_order_item(
                conn,
                order_id,
                product["id"],
                item.quantity,
                product["price_in_cents"]
            )

            decrease_stock(conn, product["id"], item.quantity)
            mark_product_as_sold(conn, product["id"])

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()

    return {
        "message": "Compra realizada com sucesso"
    }

def validate_order_products(items):
    if not items:
        bad_request("O pedido deve possuir pelo menos um produto")
    
    total_price = 0
    products = []

    for item in items:
        product = get_product_by_id(item.product_id)

        if product is None:
            not_found(f"Produto {item.product_id} não encontrado")

        if product["stock"] == 0:
            bad_request(f"O produto '{product['name']}' está sem estoque")

        if item.quantity > product["stock"]:
            bad_request(f"Estoque insuficiente para o produto '{product['name']}'")

        total_price += product["price_in_cents"] * item.quantity
        products.append(product)

    return products, total_price

def list_orders_by_user_id(user_id):
    rows = get_orders_by_user_id(user_id)

    if not rows:
        return []

    return group_orders(rows)
