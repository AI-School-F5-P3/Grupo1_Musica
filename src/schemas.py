from pydantic import BaseModel
from typing import List, Optional

class ProfesorCreate(BaseModel):
    profesor: str

class ProfesorResponse(ProfesorCreate):
    id: int

    class Config:
        orm_mode = True

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