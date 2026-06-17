from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserCreate(BaseModel):
    username: str
    email: str
    hashed_password: str

class UserOut(BaseModel):
    id: str
    username: str
    email: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}

class UserList(BaseModel):
    items: List[UserOut]
    total: int
    limit: int
    offset: int
