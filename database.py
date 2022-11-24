from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = r"sqlite:///database.db"

# create SQL engine
connect_args = {"check_same_thread": False}
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, encoding='utf-8', echo=True, connect_args = connect_args)

# create SQL communication session and bind
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create SQL mapping table
Base = declarative_base()