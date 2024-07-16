import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException
import crud
import models
import schemas

# Configuración de la base de datos de prueba
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

@pytest.fixture
async def db():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    
    async with TestingSessionLocal() as session:
        yield session
    
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.drop_all)

@pytest.mark.asyncio
async def test_crear_profesor(db):
    profesor_data = schemas.ProfesorCreate(profesor="Juan Pérez")
    nuevo_profesor = await crud.crear_profesor(db, profesor_data)
    assert nuevo_profesor.profesor == "Juan Pérez"
    assert nuevo_profesor.id is not None

@pytest.mark.asyncio
async def test_buscar_profesor_existente(db):
    # Primero, creamos un profesor
    profesor_data = schemas.ProfesorCreate(profesor="María García")
    await crud.crear_profesor(db, profesor_data)
    
    # Luego, intentamos buscarlo
    profesor = await crud.buscar_profesor(db, "María García")
    assert profesor.profesor == "María García"

@pytest.mark.asyncio
async def test_buscar_profesor_no_existente(db):
    with pytest.raises(HTTPException) as excinfo:
        await crud.buscar_profesor(db, "Profesor Inexistente")
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "Profesor no encontrado"

@pytest.mark.asyncio
async def test_crear_y_buscar_profesor(db):
    profesor_data = schemas.ProfesorCreate(profesor="Laura Martínez")
    nuevo_profesor = await crud.crear_profesor(db, profesor_data)
    assert nuevo_profesor.profesor == "Laura Martínez"

    encontrado_profesor = await crud.buscar_profesor(db, "Laura Martínez")
    assert encontrado_profesor.profesor == "Laura Martínez"

@pytest.mark.asyncio
async def test_crear_multiple_profesores(db):
    profesores = ["Ana Gómez", "Emilio Sánchez", "Lucía Fernández"]
    for nombre in profesores:
        profesor_data = schemas.ProfesorCreate(profesor=nombre)
        await crud.crear_profesor(db, profesor_data)
    
    for nombre in profesores:
        profesor = await crud.buscar_profesor(db, nombre)
        assert profesor.profesor == nombre

# Función auxiliar para crear entidades necesarias
async def crear_entidades_necesarias(db):
    instrumento = models.Instrumento(instrumento="Guitarra")
    profesor = models.Profesor(profesor="Juan Pérez")
    nivel = models.Nivel(nivel="Principiante")
    db.add_all([instrumento, profesor, nivel])
    await db.commit()

# Tests para Alumnos
@pytest.mark.asyncio
async def test_ver_alumno_existente(db):
    alumno = models.Alumno(nombre="Emilio", apellido="Sánchez")
    db.add(alumno)
    await db.commit()

    alumno_visto = await crud.ver_alumno(db, "Emilio", "Sánchez")
    assert alumno_visto.nombre == "Emilio"
    assert alumno_visto.apellido == "Sánchez"
