from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
import models
from contextlib import asynccontextmanager
import uvicorn
from database import SessionLocal, engine, Base
import schemas

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

@app.get("/alumnos/{item_id}")
async def nombre_alumno(item_id: str, db: AsyncSession = Depends(get_db)):
    alumnos = await db.execute(select(models.Alumno).filter(models.Alumno.nombre == item_id))
    item = alumnos.scalars().first()
    if item is None:
       raise HTTPException(status_code=404, detail = "Item not found")
    return item


@app.get("/alumnos/id/{item_id}")
async def id_alumnos(item_id: int, db: AsyncSession = Depends(get_db)):
    alumnos = await db.execute(select(models.Alumno).filter(models.Alumno.id == item_id))
    item = alumnos.scalars().first()
    if item is None:
       raise HTTPException(status_code=404, detail = "Item not found")
    return item



@app.get("/profesores/{item_id}")
async def id_profesor(item_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Profesor).filter(models.Profesor.id == item_id))
    item = result.scalars().first()

    if item is None:
        raise HTTPException(status_code=404, detail = "Item not found")
    return item

@app.post("/profesores/", response_model=schemas.ProfesorResponse)
async def crear_profesor(profesor: schemas.ProfesorCreate, db: AsyncSession = Depends(get_db)):
    nuevo_profesor = models.Profesor(profesor=profesor.profesor)
    db.add(nuevo_profesor)
    try:
        await db.commit()
        await db.refresh(nuevo_profesor)
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="No se pudo crear profesor nuevo")
    return nuevo_profesor

@app.post("/alumnos/", response_model=schemas.AlumnoResponse)
async def crear_alumno(alumno: schemas.Crear_Alumno, db: AsyncSession = Depends(get_db)):
    nuevo_alumno = models.Alumno(
        nombre=alumno.nombre,
        apellido=alumno.apellido,
        edad=alumno.edad,
        telefono=alumno.telefono,
        correo=alumno.correo,
        familiar=alumno.familiar,
        total_mes=alumno.total_mes
    ) 
    db.add(nuevo_alumno)
    try:
        await db.commit()
        await db.refresh(nuevo_alumno)
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="No se pudo crear alumno nuevo")
    return nuevo_alumno

@app.put("/alumnos/{alumno_id}", response_model=schemas.AlumnoResponse)
async def update_alumno(alumno_id: int, alumno: schemas.ActualizarAlumno, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Alumno).where(models.Alumno.id == alumno_id))
    existing_alumno = result.scalars().first()

    if not existing_alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

    # Actualizar los campos del alumno
    update_data = alumno.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(existing_alumno, key, value)

    try:
        await db.commit()
        await db.refresh(existing_alumno)
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="No se pudo actualizar el alumno")
    
    return existing_alumno

@app.delete("/profesores/delete/{profesor_id}", response_model=schemas.Profesor)
async def borrar_profesor(profesor_id: int, db: AsyncSession = Depends(get_db)):
    async with db.begin():
        result = await db.execute(select(models.Profesor).filter(models.Profesor.id == profesor_id))
        profesor = result.scalars().first()
        
        if not profesor:
            raise HTTPException(status_code=404, detail="Profesor no encontrado")
        
        await db.delete(profesor)
        
        try:
            await db.commit()
        except SQLAlchemyError:
            await db.rollback()
            raise HTTPException(status_code=500, detail="No se pudo borrar el profesor")
    
    return profesor

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)