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