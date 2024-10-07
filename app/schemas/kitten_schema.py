from pydantic import BaseModel
from typing import Optional

class KittenCreate(BaseModel):
    name: str
    color: str
    age: int
    description: str
    breed_id: int

class KittenUpdate(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None
    age: Optional[int] = None
    description: Optional[str] = None
    breed_id: Optional[int] = None

class KittenResponse(BaseModel):
    id: int
    name: str
    color: str
    age_months: int
    description: str
    breed_id: int
    owner_id: int

    class Config:
        from_attributes = True
