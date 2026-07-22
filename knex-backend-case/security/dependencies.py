from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from security.jwt import decode_access_token
from repository.user_repository import get_user_by_id
from exceptions import unauthorized, forbidden

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = decode_access_token(token)
    except (ExpiredSignatureError, InvalidTokenError):
        unauthorized("Token inválido ou expirado")

    user_id = payload.get("sub")

    if user_id is None:
        unauthorized("Token inválido")

    user = get_user_by_id(user_id)

    if user is None:
        unauthorized("Token inválido")

    user.pop("password_hash", None)
    
    return user


def require_seller(user=Depends(get_current_user)):
    if user["role"] != "seller":
        forbidden("Apenas vendedores podem realizar essa ação")
    
    return user

def require_client(user=Depends(get_current_user)):
    if user["role"] != "client":
        forbidden("Apenas clientes podem realizar essa ação")
    
    return user