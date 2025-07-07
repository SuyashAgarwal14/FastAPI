import uuid
from fastapi import HTTPException, Header

USERS = {
    "alice": "password123",
    "bob": "secret",
    "suyash": "Gennovation@123"
}

TOKENS = {}

def authenticate_user(username: str, password: str) -> bool:
    return USERS.get(username) == password

def create_token(username: str) -> str:
    token = f"{username}-{uuid.uuid4()}"
    TOKENS[token] = username
    return token

def get_user_from_token(token: str) -> str | None:
    return TOKENS.get(token)

def get_current_user(authorization: str = Header(None)) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    token = authorization.split(" ")[1]
    user = get_user_from_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user
