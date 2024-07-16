from pydantic import BaseModel
from typing import List, Optional

'''
Se incluyen en este archivo los esquemas que representan como se deben formatear las peticiones y las respuestas de los diferentes endpoints de la API.
Response define las respuestas. Delete define endpoints de DELETE, Create define las creaciones con POST, etc.
'''


class ProfesorCreate(BaseModel):
    profesor: str
    instrumento1: str
    instrumento2: Optional[str] = None
    instrumento3: Optional[str] = None
    instrumento4: Optional[str] = None
    instrumento5: Optional[str] = None

class ProfesorResponse(BaseModel):
    id: int
    profesor: str
    instrumento1: str
    instrumento2: Optional[str] = None
    instrumento3: Optional[str] = None
    instrumento4: Optional[str] = None
    instrumento5: Optional[str] = None

class ProfesorDelete(BaseModel):
    profesor_name: str

class ProfesorDeleteResponse(BaseModel):
    profesor_name: str

class ProfesorDeleteRequest(BaseModel):
    profesor_name: str

class ProfesorDeleteResponse(BaseModel):
    mensaje: str

class Crear_Alumno(BaseModel):
    nombre: str
    apellido: str
    edad: int
    telefono: str
    correo: str
    familiar: bool
    total_mes: int

class AlumnoResponse(BaseModel):
    id: int
    nombre: str
    apellido: str
    edad: int
    telefono: str
    correo: str
    familiar: bool
    total_mes: int

    class Config:
        orm_mode = True
        from_attributes = True

class Crear_Inscripcion(BaseModel):
    nombre:str
    apellido:str

class InscripcionResponse(BaseModel):
    id:int
    nombre:str
    apellidos:str

class ActualizarAlumno(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    edad: Optional[int] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    familiar: Optional[bool] = None
    total_mes: Optional[int] = None

class ClaseCreate(BaseModel):
    instrumento_nivel_id: int
    profesor_instrumento_id: int

class Clase(ClaseCreate):
    id: int

    class Config:
        orm_mode = True

class Profesor_InstrumentoBase(BaseModel):
    profesor_id: int
    instrumento_id: int

class Profesor_InstrumentoCreate(Profesor_InstrumentoBase):
    pass

class Profesor_Instrumento(Profesor_InstrumentoBase):
    id: int
    clases: List[Clase] = []

    class Config:
        orm_mode = True

class ProfesorBase(BaseModel):
    profesor: str

class ActualizarProfesor(BaseModel):
    profesor: Optional[str] = None

class ActualizarPrecio(BaseModel):
    precio: Optional[float] = None

class ActualizarDescuento(BaseModel):
    porcentaje: Optional[float] = None

