from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import SessionLocal, engine, Base, init_db
from logger import logger
import uvicorn
import schemas
import crud
import sys

def handle_exception(exc_type, exc_value, exc_traceback): 
    logger.error("excepcion no recogida", exc_info=(exc_type, exc_value, exc_traceback))
sys.excepthook = handle_exception

async def lifespan(app: FastAPI):
    # Evento de inicio de la base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        yield
    finally:
        # Evento de apagado de la base
        await engine.dispose()

app = FastAPI(lifespan=lifespan) # Inicio de la API

async def get_db(): # Iniciar sesión asincrona
    async with SessionLocal() as session:
        yield session

async def on_startup(): # Esperar a que se inicie la base de datos al comienzo de la API
    await init_db()

# Asignar la función de inicialización a los eventos de startup
app.add_event_handler("startup", on_startup)

# Endpoint POST para crear un alumno nuevo

@app.post("/alumnos/crear_nuevo", response_model=schemas.AlumnoResponse) # Response model, forma en la que devuelva la información del enpoint
async def crear_alumno_route(
    alumno: schemas.Crear_Alumno, # Esquema de entrada de datos que la API espera
    nombre_instrumento: str,
    nombre_profesor: str,
    nombre_nivel: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.crear_alumno(db, alumno, nombre_instrumento, nombre_profesor, nombre_nivel)

# Endpoint POST para crear una inscripción con alumno existente
@app.post("/alumnos/crear_inscripcion")
async def crear_inscripcion_route(
    alumno: schemas.Crear_Inscripcion,
    nombre_instrumento: str,
    nombre_profesor:str,
    nombre_nivel: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.crear_inscripcion(db, alumno, nombre_instrumento, nombre_profesor, nombre_nivel)


# Endpoint PUT para actualizar datos del alumno por nombre y apellido

@app.put("/alumnos/update", response_model=schemas.AlumnoResponse)
async def actualizar_alumno_route(
    alumno_nombre: str,
    alumno_apellidos: str,
    alumno: schemas.ActualizarAlumno,
    db: AsyncSession = Depends(get_db)
):
    return await crud.actualizar_alumno(db, alumno_nombre, alumno_apellidos, alumno)

# Endpoint GET para recuperar datos de un alumno por nombre y apellidos

@app.get("/alumnos/get/")
async def ver_alumno_route(
    nombre: str, 
    apellido: str, 
    db: AsyncSession = Depends(get_db)
):
    return await crud.ver_alumno(db, nombre, apellido)

# Endpoint DELETE para borrar una entrada de un alumno por nombre y apellidos

@app.delete("/alumnos/delete/{alumno_nombre}/{alumno_apellidos}")
async def borrar_alumno_route(
    alumno_nombre: str,
    alumno_apellidos: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.borrar_alumno(db, alumno_nombre, alumno_apellidos)


# Endpoint POST para crear un profesor nuevo

@app.post("/profesores/crear", response_model=schemas.ProfesorResponse)
async def crear_profesor_route(
    profesor: schemas.ProfesorCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.crear_profesor(db, profesor)

# Endpoint PUT para actualizar datos de un profesor

@app.put("/profesores/update")
async def update_profesor_route(
    profesor_nombre: str,
    profesor: schemas.ActualizarProfesor,
    db: AsyncSession = Depends(get_db)
):
    return await crud.update_profesor(db, profesor_nombre, profesor)

# Endpoint DELETE para borrar datos de un profesor por nombre

@app.delete("/profesores/delete/{profesor_name}", response_model=schemas.ProfesorDeleteResponse)
async def borrar_profesor_route(
    profesor_name: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.borrar_profesor(db, profesor_name)


# Endpoint GET para recuperar datos de un profesor por nombre

@app.get("/profesores/get")
async def buscar_profesor_route(
    nombre: str, 
    db: AsyncSession = Depends(get_db)
):
    return await crud.buscar_profesor(db, nombre)

# Endpoint PUT para actualizar precios de los packs

@app.put("/precios/update")
async def actualizar_precios_route(
    pack_name: str,
    pack: schemas.ActualizarPrecio,
    db: AsyncSession = Depends(get_db)
):
    return await crud.actualizar_precios(db, pack_name, pack)

# Endpoint PUT para actualizar los descuentos que pueden aplicarse

@app.put("/descuentos/update")
async def actualizar_descuentos_route(
    descuento_desc: str,
    descuento: schemas.ActualizarDescuento,
    db: AsyncSession = Depends(get_db)
):
    return await crud.actualizar_descuentos(db, descuento_desc, descuento)

# Endpoint GET para recuperar los precios de los packs

@app.get("/precios/get/")
async def ver_precios_route(
    pack: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.ver_precios(db, pack)
# Endpoint GET para recuperar los descuentos que pueden aplicarse

@app.get("/descuentos/get/")
async def ver_descuentos_route(
    descuento: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.ver_descuentos(db, descuento)

# Inicio de la APP

if __name__ == "__main__":
    logger.info("incio de la aplicacion")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)