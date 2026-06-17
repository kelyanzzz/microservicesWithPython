from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class GameCreate(BaseModel):
    title: str
    genre: str
    platform: str
    release_year: Optional[int] = None
    cover_url: Optional[str] = None

class GameOut(BaseModel):
    id: str
    title: str
    genre: str
    platform: str
    release_year: Optional[int] = None
    cover_url: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}

class GameList(BaseModel):
    items: List[GameOut]
    total: int
    limit: int
    offset: int
