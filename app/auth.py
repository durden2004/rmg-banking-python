# app/auth.py

from jose import jwt
from passlib.context import CryptContext
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from datetime import datetime, timedelta

SECRET_KEY = "secret123"

ALGORITHM = "HS256"

pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"
)

security = HTTPBearer()


def hash_password(password: str):

    return pwd_context.hash(password)


def verify_password(plain, hashed):

    return pwd_context.verify(plain, hashed)


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=10)

    to_encode.update({"exp": expire})

    return jwt.encode(

        to_encode,

        SECRET_KEY,

        algorithm=ALGORITHM
    )


def get_current_user(

    credentials: HTTPAuthorizationCredentials = Depends(security)

):

    token = credentials.credentials

    payload = jwt.decode(

        token,

        SECRET_KEY,

        algorithms=[ALGORITHM]
    )

    return payload