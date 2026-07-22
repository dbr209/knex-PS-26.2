from decimal import Decimal

from exceptions import not_found, bad_request
from repository.product_repository import (
        create_product, 
        get_all_products,
        get_product_by_id,
        update_product_repository,
        delete_product_repository
)

def register_product(product):
    price_cents = int(product.price * 100)

    success = create_product(
        product.name,
        product.description,
        price_cents,
        product.stock
    )

    if not success:
        bad_request("Não foi possível cadastrar o produto")

    return {
        "message": "Produto cadastrado com sucesso."
    }

def format_product_price(product):
    product["price"] = Decimal(product["price_in_cents"]) / 100
    del product["price_in_cents"]
    return product
    
def list_products():
    products = get_all_products()
    return [format_product_price(product) for product in products]

def get_product(product_id):
    product = get_product_by_id(product_id)

    if product is None:
        not_found("Produto não encontrado")
    
    return format_product_price(product)

def update_product_service(product_id, product):
    product_bd = get_product_by_id(product_id)

    if product_bd is None:
        not_found("Produto não encontrado")

    data = product.model_dump(exclude_unset=True)

    if not data:
        bad_request("Nenhum campo para atualizar")

    if "price" in data:
        data["price_in_cents"] = int(data["price"] * 100)
        del data["price"]

    update_product_repository(product_id, data)

    return {
        "message": "Produto atualizado com sucesso"
    }

def delete_product_service(product_id):
    product = get_product_by_id(product_id)

    if product is None:
        not_found("Produto não encontrado")

    if product["has_been_sold"]:
        bad_request("O produto já foi vendido")

    delete_product_repository(product_id)

    return {
        "message": "Produto removido com sucesso"
    }