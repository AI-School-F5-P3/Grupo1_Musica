import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from src.main import app, get_db
from src.database import Base
import asyncio
from src.models import Instrumento, Profesor, Nivel, Profesor_Instrumento, Instrumento_Nivel, Clase


# Configuración de la base de datos de prueba
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
TestingSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
async def populate_db():
    async with TestingSessionLocal() as session:
        # Crear instrumento
        instrumento = Instrumento(instrumento="Guitarra")
        session.add(instrumento)
        
        # Crear profesor
        profesor = Profesor(profesor="Luis")
        session.add(profesor)
        
        # Crear nivel
        nivel = Nivel(nivel="Principiante")
        session.add(nivel)
        
        await session.flush()
        
        # Crear relaciones
        profesor_instrumento = Profesor_Instrumento(profesor_id=profesor.id, instrumento_id=instrumento.id)
        session.add(profesor_instrumento)
        
        instrumento_nivel = Instrumento_Nivel(instrumento_id=instrumento.id, nivel_id=nivel.id)
        session.add(instrumento_nivel)
        
        # Crear clase
        clase = Clase(instrumento_nivel_id=instrumento_nivel.id, profesor_instrumento_id=profesor_instrumento.id)
        session.add(clase)
        
        await session.commit()

@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="module")
async def test_app(populate_db):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    await populate_db
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        
@pytest.mark.asyncio
async def test_crear_alumno(test_app):
    response = await test_app.post("/alumnos/crear_nuevo", 
        json={
            "nombre": "Juan",
            "apellido": "Pérez",
            "edad": 20,
            "telefono": "123456789",
            "correo": "juan@example.com",
            "familiar": False,
            "total_mes": 100
        }, 
        params={
            "nombre_instrumento": "Guitarra",
            "nombre_profesor": "Luis",
            "nombre_nivel": "Principiante"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Juan"
    assert data["apellido"] == "Pérez"