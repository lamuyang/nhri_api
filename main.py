from fastapi import FastAPI, Depends
from typing import List
import crud, model, schemas
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

@app.post("/LatestNews",response_model=List[schemas.LatestNewBase])
async def get_Latest_news(db:Session = Depends(get_db)):
    res = crud.get_all_article(db)
    return res

@app.post("/LatestNews/{article_id}")
async def get_article(article_id: int, db:Session = Depends(get_db)):
    res = crud.get_article(db, article_id)
    return res