from fastapi import APIRouter, HTTPException
from typing import List
from schemas.breed_schema import BreedCreate, BreedResponse
from services.breed_service import BreedService

router = APIRouter()


@router.get("/breeds/", response_model=List[BreedResponse])
async def get_all_breeds():
    return await BreedService.get_all_breeds()

@router.post("/breeds/", response_model=BreedResponse)
async def create_breed(breed_data: BreedCreate):
    return await BreedService.create_breed(breed_data)

@router.put("/breeds/{breed_id}", response_model=BreedResponse)
async def update_breed(breed_id: int, breed_data: BreedCreate):
    breed = await BreedService.get_breed_by_id(breed_id)
    if not breed:
        raise HTTPException(status_code=404, detail="Breed not found")
    
    updated_breed = await BreedService.update_breed(breed_id, breed_data)
    return updated_breed

@router.delete("/breeds/{breed_id}")
async def delete_breed(breed_id: int):
    breed = await BreedService.get_breed_by_id(breed_id)
    if not breed:
        raise HTTPException(status_code=404, detail="Breed not found")

    await BreedService.delete_breed(breed_id)
    return {"message": "Breed deleted successfully"}