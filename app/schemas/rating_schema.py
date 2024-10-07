from pydantic import BaseModel

class RatingCreate(BaseModel):
    score: int
    kitten_id: int

class RatingResponse(BaseModel):
    id: int
    score: int
    user_id: int
    kitten_id: int

    class Config:
        from_attributes = True
