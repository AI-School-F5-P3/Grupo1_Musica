from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import database_url
import app


Base = declarative_base()
engine = create_engine(database_url)

sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
