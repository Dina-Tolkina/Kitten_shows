from fastapi import APIRouter, Depends, HTTPException
from typing import List
from schemas.rating_schema import RatingCreate, RatingResponse
from services.rating_service import RatingService
from core.security import get_current_user
from models.user_model import User

router = APIRouter()

@router.get("/kittens/{kitten_id}/ratings/", response_model=List[RatingResponse])
async def get_ratings_for_kitten(kitten_id: int):
    return await RatingService.get_ratings_for_kitten(kitten_id)

@router.post("/ratings/", response_model=RatingResponse)
async def rate_kitten(rating_data: RatingCreate, user: User = Depends(get_current_user)):
    return await RatingService.create_rating(rating_data, user)
