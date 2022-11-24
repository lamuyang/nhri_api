from fastapi import FastAPI, Depends

import crud, model
from model import LatestNews
from crud import  get_all_article
from schemas import LatestNewBase
from database import SessionLocal, engine
from sqlalchemy.orm.session import Session

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/LatestNews",response_model=LatestNewBase)
async def get_Latest_news(db:Session= Depends(get_db)):
    res = get_all_article(db)
    return res