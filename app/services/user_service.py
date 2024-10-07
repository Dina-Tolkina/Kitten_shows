from passlib.context import CryptContext
from models.user_model import User
from schemas.user_schema import UserCreate, UserUpdate
from models.permission_model import Permission
from schemas.permission_schema import PermissionResponse


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    @staticmethod
    async def get_user_by_email(email: str):
        return await User.get_or_none(email=email)

    @staticmethod
    async def create_user(user_data: UserCreate):
        hashed_password = pwd_context.hash(user_data.password)
        user = await User.create(email=user_data.email, hashed_password=hashed_password)
        return user

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    async def get_all_users():
        return await User.all().prefetch_related("permissions")

    @staticmethod
    async def update_user(user: User, user_data: UserUpdate):
        if user_data.email:
            user.email = user_data.email
        if user_data.is_active is not None:
            user.is_active = user_data.is_active
        if user_data.is_admin is not None:
            user.is_admin = user_data.is_admin
        
        await user.save()
        return user
    
    @staticmethod
    async def get_user_by_id(user_id: int) -> User:
        return await User.get(id=user_id).prefetch_related('permissions')
    
    @staticmethod
    async def delete_user(user: User):
        await user.delete()
        return True

