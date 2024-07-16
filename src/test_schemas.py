import pytest
from pydantic import ValidationError
from schemas import ProfesorCreate, Crear_Alumno, ActualizarAlumno, ClaseCreate, Profesor_InstrumentoCreate, ActualizarPrecio

def test_profesor_create():
    profesor = ProfesorCreate(profesor="Juan Pérez")
    assert profesor.profesor == "Juan Pérez"

def test_crear_alumno():
    alumno = Crear_Alumno(
        nombre="Ana",
        apellido="García",
        edad=20,
        telefono="123456789",
        correo="ana@example.com",
        familiar=True,
        total_mes=100
    )
    assert alumno.nombre == "Ana"
    assert alumno.edad == 20
    assert alumno.familiar == True

def test_actualizar_alumno():
    alumno_update = ActualizarAlumno(nombre="Carlos", edad=25)
    assert alumno_update.nombre == "Carlos"
    assert alumno_update.edad == 25
    assert alumno_update.apellido is None

def test_clase_create():
    clase = ClaseCreate(instrumento_nivel_id=1, profesor_instrumento_id=2)
    assert clase.instrumento_nivel_id == 1
    assert clase.profesor_instrumento_id == 2

def test_profesor_instrumento_create():
    prof_inst = Profesor_InstrumentoCreate(profesor_id=1, instrumento_id=2)
    assert prof_inst.profesor_id == 1
    assert prof_inst.instrumento_id == 2

def test_actualizar_precio():
    precio_update = ActualizarPrecio(precio=150)
    assert precio_update.precio == 150

def test_crear_alumno_invalid_data():
    with pytest.raises(ValidationError):
        Crear_Alumno(
            nombre="Ana",
            apellido="García",
            edad="veinte",  # Esto debería ser un int, no un string
            telefono="123456789",
            correo="ana@example.com",
            familiar=True,
            total_mes=100
        )

def test_actualizar_alumno_partial():
    alumno_update = ActualizarAlumno(nombre="Carlos")
    assert alumno_update.nombre == "Carlos"
    assert alumno_update.edad is None
    assert alumno_update.apellido is None