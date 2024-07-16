import pytest
from sqlalchemy import inspect
from models import Alumno, Inscripcion, Clase, Profesor, Instrumento, Pack, Profesor_Instrumento, Descuento, Instrumento_Nivel, Nivel
from database import Base

def test_alumno_model():
    assert hasattr(Alumno, '__tablename__')
    assert Alumno.__tablename__ == 'alumno'
    assert hasattr(Alumno, 'id')
    assert hasattr(Alumno, 'nombre')
    assert hasattr(Alumno, 'apellido')
    assert hasattr(Alumno, 'inscripciones')

def test_inscripcion_model():
    assert hasattr(Inscripcion, '__tablename__')
    assert Inscripcion.__tablename__ == 'inscripcion'
    assert hasattr(Inscripcion, 'alumno_id')
    assert hasattr(Inscripcion, 'clase_id')
    assert hasattr(Inscripcion, 'descuento_id')

def test_clase_model():
    assert hasattr(Clase, '__tablename__')
    assert Clase.__tablename__ == 'clase'
    assert hasattr(Clase, 'instrumento_nivel_id')
    assert hasattr(Clase, 'profesor_instrumento_id')
    assert hasattr(Clase, 'inscripciones')

def test_profesor_instrumento_relationship():
    inspector = inspect(Profesor)
    relationship = inspector.relationships.get('profesor_instrumentos')
    assert relationship is not None
    assert relationship.mapper.class_ == Profesor_Instrumento

def test_pack_instrumento_relationship():
    inspector = inspect(Pack)
    relationship = inspector.relationships.get('instrumentos')
    assert relationship is not None
    assert relationship.mapper.class_ == Instrumento

