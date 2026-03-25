from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    email = Column(String(100))
    password = Column(String(200))

    accounts = relationship("Account", back_populates="owner")

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Float, default=0)

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="accounts")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)

    type = Column(String(20))

    amount = Column(Float)

    account_id = Column(Integer)

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)

    amount = Column(Float)

    interest = Column(Float)

    user_id = Column(Integer)
