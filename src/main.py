from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn
from database import SessionLocal, engine, Base
import schemas
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

# Crear alumno / alumno nuevo

@app.post("/alumnos/crear_nuevo", response_model=schemas.AlumnoResponse)
async def crear_alumno_route(
    alumno: schemas.Crear_Alumno,
    nombre_instrumento: str,
    nombre_profesor: str,
    nombre_nivel: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.crear_alumno(db, alumno, nombre_instrumento, nombre_profesor, nombre_nivel)

# Crear alumno / alumno existente

# Actualizar datos de alumno

@app.put("/alumnos/update", response_model=schemas.AlumnoResponse)
async def actualizar_alumno_route(
    alumno_nombre: str,
    alumno_apellidos:str, 
    alumno: schemas.ActualizarAlumno, 
    db: AsyncSession = Depends(get_db)
):
    return await crud.actualizar_alumno(alumno_nombre, alumno_apellidos, alumno, db)

# Get alumno por nombre y apellidos

@app.get("/alumnos/get")
async def ver_alumno_route(
    nombre: str, 
    apellido: str, 
    db: AsyncSession = Depends(get_db)
):
    return await crud.ver_alumno(nombre, apellido, db)

# Borrar alumno

@app.delete("alumnos/borrar")
async def borrar_alumno_route(
    alumno_nombre: str,
    alumno_apellidos: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.borrar_alumno(alumno_nombre, alumno_apellidos, db)


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


@app.delete("/profesores/delete/{profesor_id}", response_model=schemas.Profesor)
async def borrar_profesor_route(
    profesor_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.borrar_profesor(db, profesor_id)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)