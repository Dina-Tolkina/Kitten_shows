from pydantic import BaseModel

class BreedCreate(BaseModel):
    name: str

class BreedResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

