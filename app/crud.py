from sqlalchemy.orm import Session
from app import models
from app.auth import hash_password


# -------------------
# USER
# -------------------

def create_user(db: Session, user):

    hashed_password = hash_password(user.password)

    db_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user


def get_user_by_email(db: Session, email: str):

    return db.query(models.User).filter(
        models.User.email == email
    ).first()


# -------------------
# ACCOUNT
# -------------------

def create_account(db: Session, user_id: int):

    account = models.Account(
        balance=0,
        user_id=user_id
    )

    db.add(account)

    db.commit()

    db.refresh(account)

    return {
        "message": "Account created",
        "account_id": account.id
    }
