from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str

class AccountCreate(BaseModel):
    user_id: int

class TransactionCreate(BaseModel):
    account_id: int
    amount: float

class LoanCreate(BaseModel):
    user_id: int
    amount: float
    interest: float
