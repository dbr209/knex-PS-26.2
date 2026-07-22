def create_order_item(conn, order_id, product_id, quantity, unit_price_in_cents):
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO order_items
        (
            order_id,
            product_id,
            quantity,
            unit_price_in_cents
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            order_id,
            product_id,
            quantity,
            unit_price_in_cents
        )
    )
