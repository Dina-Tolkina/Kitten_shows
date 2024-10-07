from models.rating_model import Rating
from schemas.rating_schema import RatingCreate
from models.kitten_model import Kitten
from tortoise.exceptions import DoesNotExist
from fastapi import HTTPException

class RatingService:

    @staticmethod
    async def get_ratings_for_kitten(kitten_id: int):
        return await Rating.filter(kitten_id=kitten_id)

    @staticmethod
    async def create_rating(rating_data: RatingCreate, user):
        try:
            kitten = await Kitten.get(id=rating_data.kitten_id)
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Kitten not found")
        
        rating = Rating(**rating_data.dict(), user=user)
        await rating.save()
        return rating
