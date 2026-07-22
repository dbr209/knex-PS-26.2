from database.database_schema import (
    create_users_table,
    create_products_table,
    create_orders_table,
    create_order_items_table
)

def initialize_database():
    create_users_table()
    create_products_table()
    create_orders_table()
    create_order_items_table()