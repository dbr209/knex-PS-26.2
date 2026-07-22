from routes.auth import router as auth_router
from routes.products import router as products_router
from routes.orders import router as orders_router
from routes.seller import router as seller_router

def register_routes(app):
    app.include_router(auth_router)
    app.include_router(products_router)
    app.include_router(orders_router)
    app.include_router(seller_router)