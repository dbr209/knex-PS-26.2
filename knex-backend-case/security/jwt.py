import jwt
from datetime import datetime, timedelta, UTC

from config import SECRET_KEY_JWT, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(user_id, user_role):

    now = datetime.now(UTC)

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }

    return jwt.encode(payload, SECRET_KEY_JWT, algorithm=ALGORITHM,)

def decode_access_token(token):
    payload = jwt.decode(
        token,
        SECRET_KEY_JWT,
        algorithms=[ALGORITHM]
    )

    return payload