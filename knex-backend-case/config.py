import os
from dotenv import load_dotenv

load_dotenv()

SECRET_PEPPER = os.getenv("SECRET_PEPPER")
SECRET_KEY_JWT = os.getenv("SECRET_KEY_JWT")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

if SECRET_PEPPER is None:
    raise RuntimeError("SECRET_PEPPER não foi definida.")

if SECRET_KEY_JWT is None:
    raise RuntimeError("SECRET_KEY_JWT não foi definida.")