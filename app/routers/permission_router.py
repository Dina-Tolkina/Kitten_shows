from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from models.permission_model import Permission
from core.security import get_current_user
from models.user_model import User
from schemas.permission_schema import PermissionResponse

router = APIRouter()

# Назначить права пользователю
@router.post("/users/{user_id}/permissions")
async def assign_permissions(
    user_id: int, 
    can_read: bool, 
    can_write: bool, 
    can_delete: bool, 
    can_update: bool, 
    admin_user: User = Depends(get_current_user)
):
    if not admin_user.is_admin:
        return JSONResponse(status_code=403, content="Admin access required")

    try:
        user = await User.get(id=user_id)
    except:
        return JSONResponse(status_code=404, content="User not found")

    permission, created = await Permission.get_or_create(user=user)
    permission.can_read = can_read
    permission.can_write = can_write
    permission.can_delete = can_delete
    permission.can_update = can_update
    await permission.save()

    return {"message": "Permissions assigned successfully"}

# Получить права пользователя
@router.get("/users/{user_id}/permissions", response_model=List[PermissionResponse])
async def get_user_permissions(user_id: int, admin_user: User = Depends(get_current_user)):
    if not admin_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")

    user = await User.get(id=user_id).prefetch_related("permissions")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    permissions = await Permission.filter(user=user)
    
    return permissions

# Обновить права пользователя
@router.put("/users/{user_id}/permissions")
async def update_user_permissions(
    user_id: int, 
    can_read: bool, 
    can_write: bool, 
    can_delete: bool, 
    can_update: bool, 
    admin_user: User = Depends(get_current_user)
):
    if not admin_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")

    user = await User.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    permission, created = await Permission.get_or_create(user=user)
    permission.can_read = can_read
    permission.can_write = can_write
    permission.can_delete = can_delete
    permission.can_update = can_update
    await permission.save()

    return {"message": "Permissions updated successfully"}
