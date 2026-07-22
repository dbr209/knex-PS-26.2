def group_orders(rows):
    orders = {}

    for row in rows:
        order_id = row["order_id"]

        if order_id not in orders:
            orders[order_id] = {
                "id": order_id,
                "created_at": row["created_at"],
                "total": row["total_price_in_cents"] / 100,
                "products": []
            }

        orders[order_id]["products"].append({
            "product_id": row["product_id"],
            "product_name": row["product_name"],
            "quantity": row["quantity"],
            "unit_price": row["unit_price_in_cents"] / 100
        })

    return list(orders.values())