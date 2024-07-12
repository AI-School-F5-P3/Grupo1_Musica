from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()


@router.post("/alumnos/", response_model=schemas.Alumno)
def create_alumno(alumno: schemas.AlumnoCreate, db: Session = Depends(get_db)):
    return crud.create_alumno(db=db, alumno=alumno)


@router.get("/alumnos/{alumno_id}", response_model=schemas.Alumno)
def read_alumno(alumno_id: int, db: Session = Depends(get_db)):
    db_alumno = crud.get_alumno(db, alumno_id=alumno_id)
    if db_alumno is None:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return db_alumno


@router.get("/alumnos/", response_model=list[schemas.Alumno])
def read_alumnos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    alumnos = crud.get_alumnos(db, skip=skip, limit=limit)
    return alumnos


@router.get("/alumnos/{alumno_id}/clases", response_model=list[schemas.ClasePorAlumno])
def read_clases_alumno(alumno_id: int, db: Session = Depends(get_db)):
    clases = crud.get_alumno_clases(db, alumno_id)
    return clases


@router.get("/alumnos/{alumno_id}/precio", response_model=int)
def calcular_precio_alumno_endpoint(alumno_id: int, db: Session = Depends(get_db)):
    precio = crud.calcular_precio_alumno(db, alumno_id)
    return precio
