import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from database import SessionLocal



# Test para verificar la creación de la sesión local
def test_session_local_creation():
    assert isinstance(SessionLocal, sessionmaker)
    session = SessionLocal()
    assert isinstance(session, AsyncSession)
    session.close()

