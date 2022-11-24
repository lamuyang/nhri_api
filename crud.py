
from typing import List
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session, session
from model import LatestNews

def get_all_article(boxSession: Session):
    print(boxSession.query(LatestNews).filter().first())
    return boxSession.query(LatestNews).filter().first()

# def get_users(boxSession: Session, _skip: int=0, _limit: int=100) -> List[LatestNews]:
#     return boxSession.query(LatestNews).offset(_skip).limit(_limit).all()

# def create_user(boxSession: Session, _createData: PeopleUpdate) -> LatestNews :
#     peopleDetail = boxSession.query(LatestNews).filter(LatestNews.name == _createData.name,
#                                                         LatestNews.height == _createData.height,
#                                                         LatestNews.weight == _createData.weight,
#                                                         LatestNews.habbit == _createData.habbit).first()
#     if peopleDetail is not None:
#         raise HTTPException(status_code=409, detail="People already exist.")
    
#     newLatestNews = LatestNews(**_createData.dict())
#     boxSession.add(newLatestNews)
#     boxSession.commit()
#     boxSession.refresh(newLatestNews)
#     return newLatestNews

# def update_user(boxSession: Session, _id: int , infoUpdate: PeopleUpdate) -> LatestNews:
#     orignalInfo = get_user_by_id(boxSession, _id)

#     if orignalInfo is None:
#         raise HTTPException(status_code=404 , detail="404 Not Found.")
    
#     orignalInfo.name = infoUpdate.name
#     orignalInfo.height = infoUpdate.height
#     orignalInfo.weight = infoUpdate.weight
#     orignalInfo.habbit = infoUpdate.habbit
#     boxSession.commit()
#     boxSession.refresh(orignalInfo)

#     return orignalInfo


# def delete_user(boxSession: Session, _id: int):
#     res = get_user_by_id(boxSession, _id)
#     if res is None:
#         raise HTTPException(status_code=404, detail="404 Not Found.")
#     boxSession.delete(res)
#     boxSession.commit()
#     return { "code": 0 }