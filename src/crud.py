from sqlalchemy.orm import Session
from . import models, schemas


def get_alumno(db: Session, alumno_id: int):
    return db.query(models.Alumno).filter(models.Alumno.id == alumno_id).first()


def get_alumnos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Alumno).offset(skip).limit(limit).all()


def create_alumno(db: Session, alumno: schemas.AlumnoCreate):
    db_alumno = models.Alumno(**alumno.model_dump())
    db.add(db_alumno)
    db.commit()
    db.refresh(db_alumno)
    return db_alumno


def get_alumno_clases(db: Session, alumno_id: int):
    return db.query(models.
                    ClasePorAlumno).filter(models.ClasePorAlumno.alumno_id == alumno_id).all()


def clacular_precio_alumno(db: Session, alumno_id: int):
    clases = get_alumno_clases(db, alumno_id)
    total = 0
    for clase in clases:
        instrumento_nivel = db.query(models.InstrumentoNivel).filter(models.InstrumentoNivel.id == clase.instrumento_nivel).first()
        instrumento = db.query(models.Instrumento).filter(models.Instrumento.id == instrumento_nivel.instrumento_id).first()
        pack = db.query(models.Pack).filter(models.Pack.id == instrumento.pack).first()
        total += pack.precio
    return total
