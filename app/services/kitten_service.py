from models.kitten_model import Kitten
from schemas.kitten_schema import KittenCreate, KittenUpdate, KittenResponse
from models.user_model import User
from tortoise.exceptions import DoesNotExist

class KittenService:

    @staticmethod
    async def get_all_kittens():
        return await Kitten.all()

    @staticmethod
    async def get_kittens_by_breed(breed_id: int):
        return await Kitten.filter(breed_id=breed_id)

    @staticmethod
    async def get_kitten_by_id(kitten_id: int):
        try:
            return await Kitten.get(id=kitten_id)
        except DoesNotExist:
            return None

    @staticmethod
    async def create_kitten(kitten_data: KittenCreate, user: User):
        kitten = Kitten(**kitten_data.dict(), owner=user)
        return kitten

    @staticmethod
    async def update_kitten(kitten_id: int, kitten_data: KittenUpdate):
        await Kitten.filter(id=kitten_id).update(**kitten_data.dict(exclude_unset=True))
        return await Kitten.get(id=kitten_id)

    @staticmethod
    async def delete_kitten(kitten_id: int):
        await Kitten.filter(id=kitten_id).delete()
