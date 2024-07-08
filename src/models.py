from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Alumno(Base):
    __tablename__ = 'alumno'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String)
    edad = Column(Integer)
    telefono = Column(String)
    correo = Column(String)
    familiar = Column(Boolean)
    descuento = Column(Integer)

    clases = relationship("ClasePorAlumno", back_populates="alumno")


class ClasePorAlumno(Base):
    __tablename__ = "clase_por_alumno"

    id = Column(Integer, primary_key=True, index=True)
    instrumento_nivel = Column(Integer, ForeignKey("instrumento_nivel.id"))
    profesor_instrumento = Column(Integer,
                                  ForeignKey("profesor_ionstrumento.id"))
    alumno_id = Column(Integer, ForeignKey("alumno.id"))

    alumno = relationship("Alumno", back_populates="clases")


class Instrumento(Base):
    __tablename__ = 'instrumento'

    id = Column(Integer, primary_key=True, index=True)
    intrumento = Column(String, index=True)
    pack = Column(Integer, ForeignKey("pack.id"))


class Nivel(Base):
    __tablename__ = 'nivel'

    id = Column(Integer, primary_key=True, index=True)
    nivel = Column(String, index=True)


class Profesor(Base):
    __tblename__ = 'profesor'

    id = Column(Integer, primary_key=True, index=True)
    Profesor = Column(String, index=True)


class InstrumentoNivel(Base):
    __tablename__ = 'instrumento_nivel'

    id = Column(Integer, ForeignKey=True, index=True)
    intrumento_id = Column(Integer, ForeignKey("instrumento.id"))
    nivel_id = Column(Integer, ForeignKey("nivel.id"))


class ProfesorInstrumento(Base):
    __tablename__ = 'profesor_instrumento'

    id = Column(Integer, ForeignKey=True, index=True)
    profesor_id = Column(Integer, ForeignKey("profesor.id"))
    instrumento_id = Column(Integer, ForeignKey("instrumento.id"))


class Pack(Base):
    __tablename__ = 'pack'

    id = Column(Integer, primary_key=True, index=True)
    pack = Column(String, index=True)
    precio = Column(Integer)
