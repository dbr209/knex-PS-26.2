from database.connection import get_connection

def create_order_repository(conn, user_id, total_price_in_cents):
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO orders (user_id, total_price_in_cents)
        VALUES (?, ?)
        """,
        (user_id, total_price_in_cents)
    )

    return cur.lastrowid

def get_orders_by_user_id(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            ord.id AS order_id,
            ord.created_at,
            ord.total_price_in_cents,
            prod.id AS product_id,
            prod.name AS product_name,
            item.quantity,
            item.unit_price_in_cents
        FROM orders AS ord
        JOIN order_items AS item
            ON ord.id = item.order_id
        JOIN products AS prod
            ON item.product_id = prod.id
        WHERE ord.user_id = ?
        ORDER BY ord.created_at DESC, ord.id;
    """, (user_id,))

    rows = cur.fetchall()
    conn.close()

    return rows

def get_all_orders():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            ord.id AS order_id,
            ord.created_at,
            ord.total_price_in_cents,
            prod.id AS product_id,
            prod.name AS product_name,
            item.quantity,
            item.unit_price_in_cents
        FROM orders AS ord
        JOIN order_items AS item
            ON ord.id = item.order_id
        JOIN products AS prod
            ON item.product_id = prod.id
        ORDER BY ord.created_at DESC, ord.id;
    """)

    rows = cur.fetchall()
    conn.close()

    return rows


def get_sales_by_product_id(product_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            prod.id AS product_id,
            prod.name AS product_name,
            ord.id AS order_id,
            ord.created_at,
            item.quantity,
            item.unit_price_in_cents
        FROM orders AS ord
        JOIN order_items AS item
            ON ord.id = item.order_id
        JOIN products AS prod
            ON item.product_id = prod.id
        WHERE prod.id = ?
        ORDER BY ord.created_at DESC;
    """, (product_id,))

    rows = cur.fetchall()
    conn.close()

    return rows