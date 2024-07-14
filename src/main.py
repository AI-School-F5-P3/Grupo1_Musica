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
async def crear_alumno(
    alumno: schemas.Crear_Alumno,
    nombre_instrumento: str, 
    nombre_profesor: str, 
    nombre_nivel: str, 
    db: AsyncSession = Depends(get_db)):

    try:
        # Verificar que exista el instrumento
        query_instrumento = select(models.Instrumento).where(models.Instrumento.instrumento == nombre_instrumento)
        instrumento_result = await db.execute(query_instrumento)
        instrumento = instrumento_result.scalar_one_or_none()
        
        if not instrumento:
            raise HTTPException(status_code=404, detail="Instrumento no encontrado")
        
        # Verificar que exista el profesor
        query_profesor = select(models.Profesor).where(models.Profesor.profesor == nombre_profesor)
        profesor_result = await db.execute(query_profesor)
        profesor = profesor_result.scalar_one_or_none()
        
        if not profesor:
            raise HTTPException(status_code=404, detail="Profesor no encontrado")
        
        # Verificar que exista el nivel
        query_nivel = select(models.Nivel).where(models.Nivel.nivel == nombre_nivel)
        nivel_result = await db.execute(query_nivel)
        nivel = nivel_result.scalar_one_or_none()
        
        if not nivel:
            raise HTTPException(status_code=404, detail="Nivel no encontrado")
        
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al verificar datos: {str(e)}")
    
    try:
        # Verificar relaciones en Profesor_Instrumento
        query_profesor_instrumento = select(models.Profesor_Instrumento).where(
            models.Profesor_Instrumento.instrumento_id == instrumento.id,
            models.Profesor_Instrumento.profesor_id == profesor.id
        )
        profesor_instrumento_result = await db.execute(query_profesor_instrumento)
        profesor_instrumento = profesor_instrumento_result.scalar_one_or_none()
        
        if not profesor_instrumento:
            raise HTTPException(status_code=404, detail="Relación Profesor-Instrumento no encontrada")
        
        # Verificar relaciones en Instrumento_Nivel
        query_instrumento_nivel = select(models.Instrumento_Nivel).where(
            models.Instrumento_Nivel.instrumento_id == instrumento.id,
            models.Instrumento_Nivel.nivel_id == nivel.id
        )
        instrumento_nivel_result = await db.execute(query_instrumento_nivel)
        instrumento_nivel = instrumento_nivel_result.scalar_one_or_none()
        
        if not instrumento_nivel:
            raise HTTPException(status_code=404, detail="Relación Instrumento-Nivel no encontrada")
        
        # Verificar la existencia de la clase
        query_clase = select(models.Clase).where(
            and_(
                models.Clase.instrumento_nivel_id == instrumento_nivel.id,
                models.Clase.profesor_instrumento_id == profesor_instrumento.id
            )
        )
        clase_result = await db.execute(query_clase)
        clase = clase_result.scalar_one_or_none()
        
        if not clase:
            raise HTTPException(status_code=404, detail="Clase no encontrada")
        
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al verificar relaciones y clase: {str(e)}")
    
    try:
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
        await db.flush()  # Esto asegura que nuevo_alumno obtenga un ID antes de usarlo en la inscripción

        query_descuento = select(models.Descuento).where(models.Descuento.descripcion == 'Sin descuento')
        descuento_result = await db.execute(query_descuento)
        descuento = descuento_result.scalar_one_or_none()

        alumno_inscripcion = models.Inscripcion(
            alumno_id=nuevo_alumno.id,
            clase_id=clase.id,
            fecha_inicio=datetime.date.today(),
            fecha_fin=datetime.date(2025, 1, 1),
            descuento_id=descuento.id
        )

        db.add(alumno_inscripcion)
        await db.commit()
        await db.refresh(nuevo_alumno)

    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"No se pudo crear alumno nuevo: {str(e)}")

    return nuevo_alumno

@app.post("/nivel/", response_model=schemas.AlumnoResponse)
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