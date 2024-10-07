from typing import List
from fastapi import APIRouter, Depends, HTTPException
from core.security import get_current_user
from models.user_model import User
from schemas.user_schema import UserWithPermissionsResponse, UserResponse
from services.user_service import UserService, UserUpdate

router = APIRouter()

@router.get("/users", response_model=List[UserWithPermissionsResponse])
async def get_all_users(admin_user: User = Depends(get_current_user)):
    if not admin_user.is_admin:
         raise HTTPException(status_code=403, detail="Admin access required")

    users = await UserService.get_all_users()

    return users

@router.get("/users/{user_id}", response_model=UserWithPermissionsResponse)
async def get_user(user_id: int, admin_user: User = Depends(get_current_user)):
    if not admin_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")

    user = await UserService.get_user_by_id(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_data: UserUpdate, admin_user: User = Depends(get_current_user)):
    if not admin_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")

    user = await UserService.get_user_by_id(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = await UserService.update_user(user=user, user_data=user_data)
    return updated_user

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, admin_user: User = Depends(get_current_user)):
    if not admin_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")

    user = await UserService.get_user_by_id(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    deleted = await UserService.delete_user(user=user)
    if not deleted:
        raise HTTPException(status_code=500, detail="Failed to delete user")

    return {"message": "User deleted successfully"}


