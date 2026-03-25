from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth import get_current_user
from app import crud

router = APIRouter()


@router.post("/account")

def create_account(

    user_id: int,

    db: Session = Depends(get_db),

    user = Depends(get_current_user)

):

    return crud.create_account(
        db,
        user_id
    )
