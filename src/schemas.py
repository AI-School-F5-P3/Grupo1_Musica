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

class AlumnoResponse(Crear_Alumno):
    id: int

    class Config:
        orm_model = True

class ActualizarAlumno(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    edad: Optional[int] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    familiar: Optional[bool] = None
    total_mes: Optional[int] = None

class ClaseBase(BaseModel):
    instrumento_nivel_id: int
    profesor_instrumento_id: int

class ClaseCreate(ClaseBase):
    pass

class Clase(ClaseBase):
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

class ProfesorCreate(ProfesorBase):
    pass

class Profesor(ProfesorBase):
    id: int
    profesor_instrumentos: List[Profesor_Instrumento] = []

    class Config:
        orm_mode = True

class ActualizarProfesor(BaseModel):
    profesor: Optional[str] = None

class ActualizarPrecio(BaseModel):
    precio: Optional[int] = None

class ActualizarDescuento(BaseModel):
    porcentaje: Optional[int] = None