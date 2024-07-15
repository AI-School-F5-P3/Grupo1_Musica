from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn
from database import SessionLocal, engine, Base
import schemas
import crud
import logging
import sys

#configuración de log general, dentro de los paréntesis se codifica cómo quiero que me devuelva la información, level = el nivel a partir del cual quiero que me envía los mensajes. 
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    filename = 'log_escuela.log', 
                    filemode = 'a')
#esta configuración es para que detecte y registre en el archivo log todos los posibles errores que no se registran a mano a lo largo del código con logging.debug o logging.error (por ejemplo)
def handle_exception(exc_type, exc_value, exc_traceback): 
    logging.error("excepcion no recogida", exc_info=(exc_type, exc_value, exc_traceback))
sys.excepthook = handle_exception

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
    return await crud.actualizar_alumno(db, alumno_nombre, alumno_apellidos, alumno)

# Get alumno por nombre y apellidos

@app.get("/alumnos/get/{alumno_nombre}")
async def ver_alumno_route(
    nombre: str, 
    apellido: str, 
    db: AsyncSession = Depends(get_db)
):
    return await crud.ver_alumno(db, nombre, apellido)

# Borrar alumno

@app.delete("alumnos/borrar")
async def borrar_alumno_route(
    alumno_nombre: str,
    alumno_apellidos: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.borrar_alumno(db, alumno_nombre, alumno_apellidos)


# Crear profesor
@app.post("/profesores/crear", response_model=schemas.ProfesorResponse)
async def crear_profesor_route(
    profesor: schemas.ProfesorCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.crear_profesor(db, profesor)

# Actualizar datos de profesor
@app.put("profesores/update", response_model=schemas.ProfesorResponse)
async def update_profesor_route(
    profesor_nombre: str,
    profesor: schemas.ActualizarProfesor,
    db: AsyncSession = Depends(get_db)
):
    return await crud.update_profesor(db, profesor_nombre, profesor)

# Borrar profesor

@app.delete("/profesores/delete/{profesor_id}", response_model=schemas.Profesor)
async def borrar_profesor_route(
    profesor_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.borrar_profesor(db, profesor_id)

# Get profesor por nombre

@app.get("/profesores/nombre")
async def buscar_profesor_route(
    nombre: str, 
    db: AsyncSession = Depends(get_db)
):
    return await crud.buscar_profesor(db, nombre)

# Actualizar precios

@app.put("/precios/update")
async def actualizar_precios_route(
    pack_id: int,
    pack: schemas.ActualizarPrecio,
    db: AsyncSession = Depends(get_db)
):
    return await crud.actualizar_precios(db, pack_id, pack)

# Actualizar descuentos

@app.put("/descuentos/update")
async def actualizar_descuentos_route(
    descuento_id: int,
    descuento: schemas.ActualizarDescuento,
    db: AsyncSession = Depends(get_db)
):
    return await crud.actualizar_descuentos(db, descuento_id, descuento)

# Ver precios

@app.get("/precios/get/")
async def ver_precios_route(
    pack_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.ver_precios(db, pack_id)

@app.get("/descuentos/get/")
async def ver_descuentos_route(
    descuento_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.ver_descuentos(db, descuento_id)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)