from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.middleware import VoiceMiddleware

from app.routers import users, accounts, transactions


app = FastAPI()

# enable voice middleware
app.add_middleware(VoiceMiddleware)

# serve audio files
app.mount("/audio", StaticFiles(directory="audio"), name="audio")


@app.get("/")
def root():
    return {"message": "API working"}


# include routers
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(transactions.router)
