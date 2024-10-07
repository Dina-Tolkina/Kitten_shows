from models.breed_model import Breed
from schemas.breed_schema import BreedCreate

class BreedService:

    @staticmethod
    async def get_all_breeds():
        return await Breed.all()

    @staticmethod
    async def create_breed(breed_data: BreedCreate):
        breed = Breed(**breed_data.dict())
        await breed.save()
        return breed

    @staticmethod
    async def get_breed_by_id(breed_id: int):
        return await Breed.get_or_none(id=breed_id)

    @staticmethod
    async def update_breed(breed_id: int, breed_data: BreedCreate):
        breed = await Breed.get(id=breed_id)
        if not breed:
            return None
        breed.name = breed_data.name
        await breed.save()
        return breed

    @staticmethod
    async def delete_breed(breed_id: int):
        breed = await Breed.get(id=breed_id)
        if breed:
            await breed.delete()
            return True
        return False