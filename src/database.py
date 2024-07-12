from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


SQLALCHEMY_DB = 'postgresql+asyncpg://postgres:123456@localhost:5433/armonia'

engine = create_async_engine(SQLALCHEMY_DB, echo = True)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine, class_ = AsyncSession)

Base = declarative_base()
