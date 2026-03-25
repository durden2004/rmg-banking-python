from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud

router = APIRouter()

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/transactions/{account_id}")

def transactions(account_id:int,

                 db: Session = Depends(get_db)):

    return crud.get_transactions(db, account_id)
