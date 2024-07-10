from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config.config import database_url


SQLALCHEMY_DATABASE_URL = database_url


engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base