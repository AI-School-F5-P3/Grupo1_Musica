from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Alumno(Base):
    __tablename__ = 'alumno'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    edad = Column(Integer)
    telefono = Column(String)
    correo = Column(String)
    familiar = Column(Boolean)
    total_mes = Column(Integer)
    inscripciones = relationship("Inscripcion", back_populates="alumno")

class Inscripcion(Base):
    __tablename__ = 'inscripcion'
    id = Column(Integer, primary_key=True, index=True)
    alumno_id = Column(Integer, ForeignKey('alumno.id'))
    clase_id = Column(Integer, ForeignKey('clase.id'))
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    descuento_id = Column(Integer, ForeignKey('descuento.id'))
    alumno = relationship("Alumno", back_populates="inscripciones")
    clase = relationship("Clase", back_populates="inscripciones")
    descuento = relationship("Descuento", back_populates="inscripciones")

class Clase(Base):
    __tablename__ = 'clase'
    id = Column(Integer, primary_key=True, index=True)
    instrumento_nivel_id = Column(Integer, ForeignKey('instrumento_nivel.id'))
    profesor_instrumento_id = Column(Integer, ForeignKey('profesor_instrumento.id'))
    inscripciones = relationship("Inscripcion", back_populates="clase")
    instrumento_nivel = relationship("Instrumento_Nivel", back_populates="clases")
    profesor_instrumento = relationship("Profesor_Instrumento", back_populates="clases")

class Descuento(Base):
    __tablename__ = 'descuento'
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)
    porcentaje = Column(Integer)
    inscripciones = relationship("Inscripcion", back_populates="descuento")

class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, primary_key=True, index=True)
    profesor = Column(String, index=True)
    profesor_instrumentos = relationship("Profesor_Instrumento", back_populates="profesor")

class Profesor_Instrumento(Base):
    __tablename__ = 'profesor_instrumento'
    id = Column(Integer, primary_key=True, index=True)
    profesor_id = Column(Integer, ForeignKey('profesor.id'))
    instrumento_id = Column(Integer, ForeignKey('instrumento.id'))
    profesor = relationship("Profesor", back_populates="profesor_instrumentos")
    instrumento = relationship("Instrumento", back_populates="profesor_instrumentos")
    clases = relationship("Clase", back_populates="profesor_instrumento")

class Instrumento(Base):
    __tablename__ = 'instrumento'
    id = Column(Integer, primary_key=True, index=True)
    instrumento = Column(String, index=True)
    pack_id = Column(Integer, ForeignKey('pack.id'))
    profesor_instrumentos = relationship("Profesor_Instrumento", back_populates="instrumento")
    instrumento_niveles = relationship("Instrumento_Nivel", back_populates="instrumento")

class Instrumento_Nivel(Base):
    __tablename__ = 'instrumento_nivel'
    id = Column(Integer, primary_key=True, index=True)
    instrumento_id = Column(Integer, ForeignKey('instrumento.id'))
    nivel_id = Column(Integer, ForeignKey('nivel.id'))
    instrumento = relationship("Instrumento", back_populates="instrumento_niveles")
    nivel = relationship("Nivel", back_populates="instrumento_niveles")
    clases = relationship("Clase", back_populates="instrumento_nivel")

class Nivel(Base):
    __tablename__ = 'nivel'
    id = Column(Integer, primary_key=True, index=True)
    nivel = Column(String, index=True)
    instrumento_niveles = relationship("Instrumento_Nivel", back_populates="nivel")

class Pack(Base):
    __tablename__ = 'pack'
    id = Column(Integer, primary_key=True, index=True)
    pack = Column(String, index=True)
    precio = Column(Integer)
    instrumentos = relationship("Instrumento", back_populates="pack")