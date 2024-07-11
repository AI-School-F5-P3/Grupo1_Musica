from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Alumno, Profesor
import uvicorn
from database import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ejemplo de endpoint
@app.get("/alumnos/")
def get_alumnos(db: Session = Depends(get_db)):
    alumnos = db.query(Alumno).all()
    return alumnos

@app.get("/profesores/")
def get_profesor(db: Session = Depends(get_db)):
    profesores = db.query(Profesor).all()
    return profesores

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)