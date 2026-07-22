from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from config import SECRET_PEPPER

hasher = PasswordHasher()

def hash_password(password):
    return hasher.hash(password + SECRET_PEPPER)

def verify_password(password, hashed_password):
    try:
        hasher.verify(hashed_password, password + SECRET_PEPPER)
        return True
    except VerifyMismatchError:
        return False