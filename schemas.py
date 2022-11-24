from typing import List
from pydantic import BaseModel

class LatestNewBase(BaseModel):
    title: str
    subtitle: str
    abstract: str
    content: str
    
    class Config:
        orm_mode = True

# class PeopleUpdate(PeopleBase):
#     id: int

#     class Config:
#         orm_mode = True

# class PeopleType(BaseModel):
#     skip: int
#     limit: int
#     data: List[PeopleUpdate]