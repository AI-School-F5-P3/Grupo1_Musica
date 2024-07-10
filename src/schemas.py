from typing import List
from pydantic import BaseModel


class ClasePorAlumnoBase(BaseModel):
    intrumento_nivel: int
    profesor_intrumento: int
    alumno_id: int


class ClasePorAlumnoCreate(ClasePorAlumnoBase):
    pass


class ClasePorAlumno(ClasePorAlumnoBase):
    id: int

    class Config:
        orm_mode = True


class AlumnoBase(BaseModel):
    nombre: str
    apellido: str
    edad: int
    telefono: str
    correro: str
    familiar: bool
    descuento: int


class AlumnoCreate(AlumnoBase):
    pass


class Alumno(AlumnoBase):
    id: int
    clases: List[ClasePorAlumno] = []

    class Config:
        orm_mode = True


class NivelBase(BaseModel):
    nivel: str


class NivelCreate(NivelBase):
    pass


class Nivel(NivelBase):
    id: int

    class Config:
        orm_mode = True


class ProfesorBase(BaseModel):
    profesor: str


class ProfresorCreate(ProfesorBase):
    pass


class Profesor(ProfesorBase):
    id: int

    class Config:
        orm_mode = True


class InstrumentoNivelBase(BaseModel):
    instrumento_id: int
    nivel_id: int


class InstrumentoNivelCreate(InstrumentoNivelBase):
    pass


class InstrumentoNivel(InstrumentoNivelBase):
    id: int

    class Config:
        orm_mode = True


class ProfesorInstrumentoBase(BaseModel):
    profesor_id: int
    instrumento_id: int


class ProfesorInstrumentoCreate(ProfesorInstrumentoBase):
    pass


class ProfesorInstrumento(ProfesorInstrumentoBase):
    id: int

    class Config:
        orm_mode = True


class PackBase(BaseModel):
    pack: str
    precio: int


class PackCreate(PackBase):
    pass


class Pack(PackBase):
    id: int

    class Config:
        orm_mode = True
