from sqlite3 import IntegrityError

from database.connection import get_connection

def create_product(name, description, price, stock):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO products (name, description, price_in_cents, stock, has_been_sold)
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, description, price, stock, 0)
        )

        conn.commit()
        return True

    except IntegrityError:
        return False

    finally:
        conn.close()

def get_all_products():
    conn = get_connection()
    cur = conn.cursor()

    try:
        products = cur.execute(
            """
            SELECT * FROM products
            """
        ).fetchall()

        return [dict(product) for product in products]

    finally:
        conn.close()

def get_product_by_id(product_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM products WHERE id = ?",
        (product_id,)
    )

    product = cur.fetchone()

    conn.close()

    if product:
        return dict(product)
    return product

def update_product_repository(product_id, data):
    conn = get_connection()

    lista_fields = []

    for key in data.keys():
        lista_fields.append(f"{key} = ?")

    fields = ", ".join(lista_fields)

    values = list(data.values())
    values.append(product_id)

    conn.execute(f"""UPDATE products 
                 SET {fields}, updated_at = CURRENT_TIMESTAMP 
                 WHERE id = ?""", 
                 values)
    
    conn.commit()
    conn.close()

def delete_product_repository(product_id):
    conn = get_connection()

    conn.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )

    conn.commit()
    conn.close()

def mark_product_as_sold(conn, product_id):
    conn.execute(
        """
        UPDATE products
        SET has_been_sold = 1
        WHERE id = ?
        """,
        (product_id,)
    )

def decrease_stock(conn, product_id, quantity):
    conn.execute(
        """
        UPDATE products
        SET stock = stock - ?
        WHERE id = ?
        """,
        (quantity, product_id)
    )