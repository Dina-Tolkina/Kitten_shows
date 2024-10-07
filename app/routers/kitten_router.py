from models.kitten_model import Kitten
from schemas.kitten_schema import KittenCreate, KittenUpdate
from fastapi import APIRouter, Depends, HTTPException
from services.permission_service import PermissionService
from core.security import get_current_user
from models.user_model import User
from typing import List
from services.kitten_service import KittenService
import logging


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/kittens/")
async def get_all_kittens():
    return await KittenService.get_all_kittens()


@router.get("/kittens/breed/{breed_id}")
async def get_kittens_by_breed(breed_id: int):
    return await KittenService.get_kittens_by_breed(breed_id)


@router.get("/kittens/{kitten_id}")
async def get_kitten(kitten_id: int):
    kitten = await KittenService.get_kitten_by_id(kitten_id)
    if not kitten:
        raise HTTPException(status_code=404, detail="Kitten not found")
    return kitten


@router.post("/kittens/")
async def create_kitten(kitten_data: KittenCreate, user: User = Depends(get_current_user)):
    has_permission = await PermissionService.has_access(user, "write")
    if not has_permission:
        raise HTTPException(status_code=403, detail="You do not have permission to perform this action.")

    kitten = await KittenService.create_kitten(kitten_data, user)
    await kitten.save()  
    return kitten


@router.put("/kittens/{kitten_id}")
async def update_kitten(kitten_id: int, kitten_data: KittenUpdate, user: User = Depends(get_current_user)):
    kitten = await Kitten.get_or_none(id=kitten_id)
    if kitten is None:
        raise HTTPException(status_code=404, detail="The kitten has not been found.")
    
    has_permission = await PermissionService.has_access(user, "update", kitten)
    if not has_permission:
        raise HTTPException(status_code=403, detail="You do not have permission to edit this kitten.")
    
    await Kitten.filter(id=kitten_id).update(**kitten_data.dict(exclude_unset=True))
    
    return await Kitten.get(id=kitten_id)


@router.delete("/kittens/{kitten_id}")
async def delete_kitten(kitten_id: int, user: User = Depends(get_current_user)):
    kitten = await Kitten.get_or_none(id=kitten_id)
    if kitten is None:
        raise HTTPException(status_code=404, detail="The kitten has not been found.")
    
    has_permission = await PermissionService.has_access(user, "delete", kitten)
    if not has_permission:
        raise HTTPException(status_code=403, detail="You do not have permission to delete this kitten.")
    
    await kitten.delete()
    
    return kitten
