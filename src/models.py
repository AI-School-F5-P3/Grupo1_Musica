from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Alumno(Base):
    __tablename__ = 'alumno'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    edad = Column(Integer, index=True)
    telefono = Column(String, index=True)
    correo = Column(String, index=True)
    familiar = Column(Boolean, default=False)
    total_mes = Column(Integer, index=True)


class Clase(Base):
    __tablename__ = "clase"

    id = Column(Integer, primary_key=True, index=True)
    instrumento_nivel_id = Column(Integer, ForeignKey('instrumento_nivel.id'), index=True)
    profesor_instrumento_id = Column(Integer, ForeignKey('profesor_instrumento.id'), index=True)


class Descuento(Base):
    __tablename__ = 'descuento'

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True)
    porcentaje = Column(Integer, index=True)


class Inscripcion(Base):
    __tablename__ = "inscripcion"

    id = Column(Integer, primary_key=True, index=True)
    alumno_id = Column(Integer, ForeignKey("alumno.id"), index=True)
    clase_id = Column(Integer, ForeignKey("clase.id"), index=True)
    fecha_inicio = Column(Date, index=True, default=datetime.date.today)
    fecha_fin = Column(Date, index=True)
    descuento_id = Column(Integer, ForeignKey("descuento.id"), index=True)


class Instrumento(Base):
    __tablename__ = "instrumento"

    id = Column(Integer, primary_key=True, index=True)
    instrumento = Column(String, index=True)
    pack_id = Column(Integer, ForeignKey("pack.id"), index=True)


class InstrumentoNivel(Base):
    __tablename__ = "instrumento_nivel"

    id = Column(Integer, primary_key=True, index=True)
    instrumento_id = Column(Integer, ForeignKey("instrumento.id"), index=True)
    nivel_id = Column(Integer, ForeignKey("nivel.id"), index=True)


class Nivel(Base):
    __tablename__ = "nivel"

    id = Column(Integer, primary_key=True, index=True)
    nivel = Column(String, index=True)


class Pack(Base):
    __tablename__ = "pack"

    id = Column(Integer, primary_key=True, index=True)
    pack = Column(String, index=True)
    precio = Column(Integer, index=True)


class Profesor(Base):
    __tablename__ = "profesor"

    id = Column(Integer, primary_key=True, index=True)
    profesor = Column(String, index=True)


class ProfesorInstrumento(Base):
    __tablename__ = "profesor_instrumento"

    id = Column(Integer, primary_key=True, index=True)
    profesor_id = Column(Integer, ForeignKey("profesor.id"), index=True)
    instrumento_id = Column(Integer, ForeignKey("instrumento.id"), index=True)