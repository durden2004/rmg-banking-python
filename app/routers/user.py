from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, crud
from app.auth import create_access_token, authenticate_user

router = APIRouter()


# -------------------
# CREATE USER
# -------------------

@router.post("/users")

def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    return crud.create_user(db, user)


# -------------------
# LOGIN
# -------------------

@router.post("/login")

def login(
    user: schemas.Login,
    db: Session = Depends(get_db)
):

    db_user = authenticate_user(
        db,
        user.email,
        user.password
    )

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="invalid credentials"
        )

    token = create_access_token(

        {"sub": db_user.email}

    )

    return {

        "access_token": token,

        "token_type": "bearer"

    }
