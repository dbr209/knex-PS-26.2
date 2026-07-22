from fastapi import APIRouter, status

from schemas.user_schemas import UserCreate, UserLogin
from services.auth_service import register_user, login_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate):
    return register_user(user)

@router.post("/login")
def login(user: UserLogin):
    return login_user(user)