from fastapi import FastAPI

from routes.router import register_routes
from database.initializer import initialize_database

app = FastAPI()

initialize_database()
register_routes(app)
