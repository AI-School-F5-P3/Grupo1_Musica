from fastapi import FastAPI
from .routers import alumnos

app = FastAPI()

app.include_router(alumnos.router, prefi="/api/vi", tags=["alumnos"])


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de la Escuela de Música"}
