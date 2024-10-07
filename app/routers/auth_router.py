from fastapi import APIRouter, HTTPException
from schemas.user_schema import UserCreate, UserLogin, UserResponse
from services.user_service import UserService
from core.security import create_access_token
from datetime import timedelta

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate):
    user = await UserService.get_user_by_email(user_data.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = await UserService.create_user(user_data)
    return user

@router.post("/login", response_model=dict)
async def login_for_access_token(user_data: UserLogin):
    user = await UserService.get_user_by_email(user_data.email)
    if not user or not UserService.verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}