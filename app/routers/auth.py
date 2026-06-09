from fastapi import APIRouter
from app.schemas.user import UserCreate

router =APIRouter()

@router.post("/register")
def register(user: UserCreate):
    return{
        "message": "User registered successfully",
        "username": user.username,
        "email": user.email
    }