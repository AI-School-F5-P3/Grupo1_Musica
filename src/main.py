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

descripcion_API = '''
La API para la escuela Armonía va a permitir realizar diferentes peticiones a la base de datos de la escuela, 
permitiendo controlar el flujo de datos, y llevar al día todos los registros del alumnado y profesorado, además de permitir
un mayor control sobre precios y descuentos.

Las funiones a destacar son

* **Crear nuevos alumnos.**
* **Crear nuevas inscripciones.**
* **Registrar nuevos profesores.**
* **Actualizar datos de profesorado, alumnado, precios y descuentos.**
* **Eliminar registros de todas las tablas cuando sea necesario.**
* **Recuperar en diferentes formatos (JSON y CSV) los datos de todas las tablas.**
'''


tags_metadata = [
    {
        "name": "Alumnos",
        "description": "Operaciones con datos de alumnado. Añadir, actualizar, borrar y recuperar.",
    },
    {
        "name": "Profesores",
        "description": "Operaciones con datos de Profesorado. Añadir, actualizar, borrar y recuperar.",
        },
    {
        "name": "Finanzas",
        "description": "Operaciones de finanzas, actualizar precios, actualizar descuentos, recuperar datos."
    }
]

app = FastAPI(
    title = 'Base de datos Escuela Armonia',
    description=descripcion_API,
    summary = 'API para control de bases de datos postgres en Escuela Armonía',
    version = 'Very early access',
    terms_of_service= 'Usadla con moderación',
    contact ={'name': 'Javier', 'puesto': 'Product Owner'},
    openapi_tags=tags_metadata,
    lifespan=lifespan) # Inicio de la API

async def get_db(): # Iniciar sesión asincrona
    async with SessionLocal() as session:
        yield session

async def on_startup(): # Esperar a que se inicie la base de datos al comienzo de la API
    await init_db()

# Asignar la función de inicialización a los eventos de startup
app.add_event_handler("startup", on_startup)

# Endpoint POST para crear un alumno nuevo

@app.post("/alumnos/crear_nuevo", response_model=schemas.AlumnoResponse, tags = ['Alumnos']) # Response model, forma en la que devuelva la información del enpoint
async def crear_alumno_route(
    alumno: schemas.Crear_Alumno, # Esquema de entrada de datos que la API espera
    nombre_instrumento: str,
    nombre_profesor: str,
    nombre_nivel: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.crear_alumno(db, alumno, nombre_instrumento, nombre_profesor, nombre_nivel)

# Endpoint POST para crear una inscripción con alumno existente
@app.post("/alumnos/crear_inscripcion", tags = ['Alumnos'])
async def crear_inscripcion_route(
    alumno: schemas.Crear_Inscripcion,
    nombre_instrumento: str,
    nombre_profesor:str,
    nombre_nivel: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.crear_inscripcion(db, alumno, nombre_instrumento, nombre_profesor, nombre_nivel)


# Endpoint PUT para actualizar datos del alumno por nombre y apellido

@app.put("/alumnos/update", response_model=schemas.AlumnoResponse, tags = ['Alumnos'])
async def actualizar_alumno_route(
    alumno_nombre: str,
    alumno_apellidos: str,
    alumno: schemas.ActualizarAlumno,
    db: AsyncSession = Depends(get_db)
):
    return await crud.actualizar_alumno(db, alumno_nombre, alumno_apellidos, alumno)

# Endpoint GET para recuperar datos de un alumno por nombre y apellidos

@app.get("/alumnos/get/", tags = ['Alumnos'])
async def ver_alumno_route(
    nombre: str, 
    apellido: str, 
    db: AsyncSession = Depends(get_db)
):
    return await crud.ver_alumno(db, nombre, apellido)

# Endpoint DELETE para borrar una entrada de un alumno por nombre y apellidos

@app.delete("/alumnos/delete/{alumno_nombre}/{alumno_apellidos}", tags = ['Alumnos'])
async def borrar_alumno_route(
    alumno_nombre: str,
    alumno_apellidos: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.borrar_alumno(db, alumno_nombre, alumno_apellidos)


# Endpoint POST para crear un profesor nuevo

@app.post("/profesores/crear", response_model=schemas.ProfesorResponse, tags = ['Profesores'])
async def crear_profesor_route(
    profesor: schemas.ProfesorCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.crear_profesor(db, profesor)

# Endpoint PUT para actualizar datos de un profesor

@app.put("/profesores/update", tags = ["Profesores"])
async def update_profesor_route(
    profesor_nombre: str,
    profesor: schemas.ActualizarProfesor,
    db: AsyncSession = Depends(get_db)
):
    return await crud.update_profesor(db, profesor_nombre, profesor)

# Endpoint DELETE para borrar datos de un profesor por nombre

@app.delete("/profesores/delete/{profesor_name}", response_model=schemas.ProfesorDeleteResponse, tags = ['Profesores'])
async def borrar_profesor_route(
    profesor_name: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.borrar_profesor(db, profesor_name)


# Endpoint GET para recuperar datos de un profesor por nombre

@app.get("/profesores/get", tags = ['Profesores'])
async def buscar_profesor_route(
    nombre: str, 
    db: AsyncSession = Depends(get_db)
):
    return await crud.buscar_profesor(db, nombre)

# Endpoint PUT para actualizar precios de los packs

@app.put("/precios/update", tags = ['Finanzas'])
async def actualizar_precios_route(
    pack_name: str,
    pack: schemas.ActualizarPrecio,
    db: AsyncSession = Depends(get_db)
):
    return await crud.actualizar_precios(db, pack_name, pack)

# Endpoint PUT para actualizar los descuentos que pueden aplicarse

@app.put("/descuentos/update", tags = ['Finanzas'])
async def actualizar_descuentos_route(
    descuento_desc: str,
    descuento: schemas.ActualizarDescuento,
    db: AsyncSession = Depends(get_db)
):
    return await crud.actualizar_descuentos(db, descuento_desc, descuento)

# Endpoint GET para recuperar los precios de los packs

@app.get("/precios/get/", tags = ['Finanzas'])
async def ver_precios_route(
    pack: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.ver_precios(db, pack)
# Endpoint GET para recuperar los descuentos que pueden aplicarse

@app.get("/descuentos/get/", tags = ['Finanzas'])
async def ver_descuentos_route(
    descuento: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.ver_descuentos(db, descuento)

# Inicio de la APP

if __name__ == "__main__":
    logger.info("incio de la aplicacion")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)