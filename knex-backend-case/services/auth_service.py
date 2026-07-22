from repository.user_repository import get_user_by_email, create_user
from security.password import hash_password, verify_password
from security.jwt import create_access_token
from exceptions import conflict, unauthorized

def register_user(user):
    if get_user_by_email(user.email):
        conflict("Usuário já existe.")

    hashed_password = hash_password(user.password)

    create_user(user.name, user.email, hashed_password, user.role)

    return {
    "message": "Usuário cadastrado com sucesso."
    }

def login_user(user):
    db_user = get_user_by_email(user.email)

    if(db_user is None):
        unauthorized("Email ou senha invalidos")

    if(not verify_password(user.password, db_user["password_hash"])):
        unauthorized("Email ou senha invalidos")
    
    token = create_access_token(db_user["id"], db_user["role"])

    return {
        "access_token": token,
        "token_type": "bearer"
    }
