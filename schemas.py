from typing import List
from pydantic import BaseModel

class LatestNewBase(BaseModel):
    id: int
    title: str
    subtitle: str
    abstract: str
    content: str
    
    class Config:
        orm_mode = True