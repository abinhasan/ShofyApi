from pydantic import BaseModel

class OrderCreate(BaseModel):
    description: str

class OrderOut(BaseModel):
    id: int
    description: str
    user_id: int

    class Config:
        from_attributes = True
