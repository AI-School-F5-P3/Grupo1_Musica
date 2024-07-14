from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_
import models
from contextlib import asynccontextmanager
import uvicorn
from database import SessionLocal, engine, Base
import schemas
import datetime
import crud

async def lifespan(app: FastAPI):
    # Evento de inicio
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        yield
    finally:
        # Evento de apagado
        await engine.dispose()

app = FastAPI(lifespan=lifespan)

async def get_db():
    async with SessionLocal() as session:
        yield session

# Get alumno por nombre y apellidos
@app.get("/alumnos/{nombre}")
async def nombre_alumno(
    nombre: str, 
    apellido: str, 
    db: AsyncSession = Depends(get_db)
):
    return await crud.buscar_alumno(nombre, apellido, db)

#Get profesor por nombre
@app.get("/profesores/{nombre}")
async def nombre_profesor(
    nombre: str, 
    db: AsyncSession = Depends(get_db)
):
    return await crud.buscar_profesor(nombre, db)

# Crear profesor
@app.post("/profesores/", response_model=schemas.ProfesorResponse)
async def crear_profesor_route(
    profesor: schemas.ProfesorCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.crear_profesor(db, profesor)

@app.post("/alumnos/", response_model=schemas.AlumnoResponse)
async def crear_alumno_route(
    alumno: schemas.Crear_Alumno,
    nombre_instrumento: str,
    nombre_profesor: str,
    nombre_nivel: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.crear_alumno(db, alumno, nombre_instrumento, nombre_profesor, nombre_nivel)


@app.put("/alumnos/{alumno_id}", response_model=schemas.AlumnoResponse)
async def update_alumno_route(
    alumno_id: int, 
    alumno: schemas.ActualizarAlumno, 
    db: AsyncSession = Depends(get_db)
):
    return await crud.actualizar_alumno(alumno_id, alumno, db)

@app.delete("/profesores/delete/{profesor_id}", response_model=schemas.Profesor)
async def borrar_profesor_route(
    profesor_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.borrar_profesor(db, profesor_id)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)