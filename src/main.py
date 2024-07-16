from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn
from database import SessionLocal, engine, Base, init_db
import schemas
import crud
import logging
import sys
import os


# Ruta de la carpeta de logs
src_dir = os.path.dirname(os.path.dirname(__file__))
log_dir = os.path.join(src_dir, 'src', 'logs')

# Crea la carpeta si no existe
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Ruta completa del archivo de log
log_file = os.path.join(log_dir, 'log_escuela.log')

#configuración de log general, dentro de los paréntesis se codifica cómo quiero que me devuelva la información, level = el nivel a partir del cual quiero que me envía los mensajes. 
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    filename = log_file, 
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

async def on_startup():
    await init_db()

# Asignar la función de inicialización a los eventos de startup
app.add_event_handler("startup", on_startup)

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
@app.post("/alumnos/crear_inscripcion")
async def crear_inscripcion_route(
    alumno: schemas.Crear_Inscripcion,
    nombre_instrumento: str,
    nombre_profesor:str,
    nombre_nivel: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.crear_inscripcion(db, alumno, nombre_instrumento, nombre_profesor, nombre_nivel)


# Actulizar alumno

@app.put("/alumnos/update", response_model=schemas.AlumnoResponse)
async def actualizar_alumno_route(
    alumno_nombre: str,
    alumno_apellidos: str,
    alumno: schemas.ActualizarAlumno,
    db: AsyncSession = Depends(get_db)
):
    return await crud.actualizar_alumno(db, alumno_nombre, alumno_apellidos, alumno)

# Get alumno por nombre y apellidos

@app.get("/alumnos/get/")
async def ver_alumno_route(
    nombre: str, 
    apellido: str, 
    db: AsyncSession = Depends(get_db)
):
    return await crud.ver_alumno(db, nombre, apellido)

# Borrar alumno

@app.delete("/alumnos/delete/{alumno_nombre}/{alumno_apellidos}")
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
@app.put("/profesores/update")
async def update_profesor_route(
    profesor_nombre: str,
    profesor: schemas.ActualizarProfesor,
    db: AsyncSession = Depends(get_db)
):
    return await crud.update_profesor(db, profesor_nombre, profesor)

# Borrar profesor

@app.delete("/profesores/delete/{profesor_name}", response_model=schemas.ProfesorDeleteResponse)
async def borrar_profesor_route(
    profesor_name: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.borrar_profesor(db, profesor_name)


# Get profesor por nombre

@app.get("/profesores/get")
async def buscar_profesor_route(
    nombre: str, 
    db: AsyncSession = Depends(get_db)
):
    return await crud.buscar_profesor(db, nombre)

# Actualizar precios

@app.put("/precios/update")
async def actualizar_precios_route(
    pack_name: str,
    pack: schemas.ActualizarPrecio,
    db: AsyncSession = Depends(get_db)
):
    return await crud.actualizar_precios(db, pack_name, pack)

# Actualizar descuentos

@app.put("/descuentos/update")
async def actualizar_descuentos_route(
    descuento_desc: str,
    descuento: schemas.ActualizarDescuento,
    db: AsyncSession = Depends(get_db)
):
    return await crud.actualizar_descuentos(db, descuento_desc, descuento)

# Ver precios

@app.get("/precios/get/")
async def ver_precios_route(
    pack: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.ver_precios(db, pack)

@app.get("/descuentos/get/")
async def ver_descuentos_route(
    descuento: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.ver_descuentos(db, descuento)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)