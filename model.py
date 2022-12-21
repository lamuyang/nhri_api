# create model attribute/column
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float

# relationship with ORM
#from sqlalchemy.orm import relationship

from database import Base

class LatestNews(Base):
    __tablename__ = "Latest_News"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    subtitle = Column(String)
    abstract = Column(String)
    content = Column(String)