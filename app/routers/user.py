from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas
from ..auth import create_access_token

router = APIRouter()

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/users")
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    return crud.create_user(db, user)


@router.post("/login")
def login(
    login: schemas.Login,
    db: Session = Depends(get_db)
):

    user = crud.authenticate_user(
        db,
        login.email,
        login.password
    )

    if not user:

        return {"error": "invalid credentials"}

    token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }