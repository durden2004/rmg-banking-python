from sqlalchemy.orm import Session
from . import models
from .auth import hash_password, verify_password


def create_user(db: Session, user):

    db_user = models.User(

        username=user.username,

        email=user.email,

        password=hash_password(user.password)
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user


def authenticate_user(db: Session, email, password):

    user = db.query(models.User).filter(
        models.User.email == email
    ).first()

    if not user:

        return None

    if not verify_password(password, user.password):

        return None

    return user


def create_account(db: Session, user_id):

    account = models.Account(
        user_id=user_id,
        balance=0
    )

    db.add(account)

    db.commit()

    db.refresh(account)

    return account


def deposit(db: Session, account_id, amount):

    account = db.query(models.Account).filter(
        models.Account.id == account_id
    ).first()

    account.balance += amount

    transaction = models.Transaction(

        type="deposit",

        amount=amount,

        account_id=account_id
    )

    db.add(transaction)

    db.commit()

    return account


def withdraw(db: Session, account_id, amount):

    account = db.query(models.Account).filter(
        models.Account.id == account_id
    ).first()

    if account.balance < amount:

        return {"error": "insufficient balance"}

    account.balance -= amount

    transaction = models.Transaction(

        type="withdraw",

        amount=amount,

        account_id=account_id
    )

    db.add(transaction)

    db.commit()

    return account


def create_loan(db: Session, loan):

    db_loan = models.Loan(

        user_id=loan.user_id,

        amount=loan.amount,

        interest=loan.interest
    )

    db.add(db_loan)

    db.commit()

    db.refresh(db_loan)

    return db_loan


def get_transactions(db: Session, account_id):

    return db.query(models.Transaction).filter(
        models.Transaction.account_id == account_id
    ).all()

def get_account(db, account_id):

    return db.query(models.Account).filter(
        models.Account.id == account_id
    ).first()