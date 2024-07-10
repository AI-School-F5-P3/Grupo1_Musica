from fastapi import FastAPI
from routers import router
import uvicorn

app = FastAPI()

app.include_router(router.router, prefix="/api/vi", tags=["alumnos"])


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de la Escuela de Música"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
