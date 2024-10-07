from fastapi import HTTPException
from models.permission_model import Permission
from models.user_model import User
from models.kitten_model import Kitten

class PermissionService:

    @staticmethod
    async def has_access(user: User, permission_type: str, kitten: Kitten = None) -> bool:
        if user.is_admin:
            return True  
        
        permission = await Permission.get_or_none(user=user)

        if not permission:
            return True  

        if permission_type == "read" and permission.can_read:
            return True

        if permission_type == "write" and permission.can_write:
            return True

        if permission_type in ["update", "delete"] and kitten:
            kitten_owner = await kitten.owner

            if kitten_owner.id == user.id:
                return True

        if permission_type == "write" and not permission.can_write:
            return False

        return False


async def permission_required(user: User, permission_type: str, kitten: Kitten = None):
    has_access = await PermissionService.has_access(user, permission_type, kitten)
    if not has_access:
        raise HTTPException(status_code=403, detail="You do not have permission to perform this action.")
