from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud

router = APIRouter(prefix="/account", tags=["Account"])


@router.post("/")
def create_account(user_id: int, db: Session = Depends(get_db)):

    account = crud.create_account(db, user_id)

    return {
        "message": "Account created",
        "account_id": account.id
    }
