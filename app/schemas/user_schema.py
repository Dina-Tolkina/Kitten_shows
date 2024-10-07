from typing import List, Optional
from pydantic import BaseModel, EmailStr

from schemas.permission_schema import PermissionResponse

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool
    is_admin: bool

    class Config:
        from_attributes = True
        
class UserWithPermissionsResponse(BaseModel):
    id: int
    email: str
    is_active: bool
    is_admin: bool
    permissions: List[PermissionResponse]  

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None
