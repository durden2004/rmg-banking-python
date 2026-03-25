# app/routers/account.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud
from ..auth import get_current_user

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/account")
def create_account(

    user_id: int,

    db: Session = Depends(get_db),

    user = Depends(get_current_user)

):

    return crud.create_account(db, user_id)