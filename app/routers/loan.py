# app/routers/loan.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas
from ..auth import get_current_user

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/loan")
def create_loan(

    loan: schemas.LoanCreate,

    db: Session = Depends(get_db),

    user = Depends(get_current_user)

):

    return crud.create_loan(db, loan)