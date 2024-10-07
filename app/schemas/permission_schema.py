from pydantic import BaseModel

class PermissionResponse(BaseModel):
    can_read: bool
    can_write: bool
    can_delete: bool
    can_update: bool
    

    class Config:
        from_attributes = True
