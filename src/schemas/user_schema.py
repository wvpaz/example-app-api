from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class UserBase(BaseModel):
    name: str
    surname: str
    age: int
    home_town: Optional[str | None] = None

class UserCreate(UserBase):
    pass

class UserSchema(UserBase):
    id: UUID