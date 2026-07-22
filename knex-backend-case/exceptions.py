from fastapi import HTTPException, status

def not_found(message: str):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=message
    )

def unauthorized(message: str):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=message
    )

def bad_request(message: str):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message
    )

def conflict(message: str):
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=message
    )

def forbidden(message: str):
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=message
    )