from fastapi import FastAPI

from app.database.database import engine
from app.models.user import User
from app.routers.auth import router as auth_router

User.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "SecureVault API Running"}