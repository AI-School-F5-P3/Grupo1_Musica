from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from database import Base

class Alumno(Base):
    __tablename__ = 'alumno'
    __table_args__ = {'schema': 'armonia'}
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    edad = Column(Integer)
    telefono = Column(String)
    correo = Column(String)
    familiar = Column(Boolean)
    total_mes = Column(Float)
    inscripciones = relationship("Inscripcion", back_populates="alumno", cascade = "all, delete")

class Inscripcion(Base):
    __tablename__ = 'inscripcion'
    __table_args__ = {'schema': 'armonia'}
    id = Column(Integer, primary_key=True, index=True)
    alumno_id = Column(Integer, ForeignKey('armonia.alumno.id', ondelete="CASCADE"), nullable=False)
    clase_id = Column(Integer, ForeignKey('armonia.clase.id'))
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    descuento_id = Column(Integer, ForeignKey('armonia.descuento.id'))
    alumno = relationship("Alumno", back_populates="inscripciones")
    clase = relationship("Clase", back_populates="inscripciones")
    descuento = relationship("Descuento", back_populates="inscripciones")

class Clase(Base):
    __tablename__ = 'clase'
    __table_args__ = {'schema': 'armonia'}
    id = Column(Integer, primary_key=True, index=True)
    instrumento_nivel_id = Column(Integer, ForeignKey('armonia.instrumento_nivel.id'))
    profesor_instrumento_id = Column(Integer, ForeignKey('armonia.profesor_instrumento.id'))
    inscripciones = relationship("Inscripcion", back_populates="clase")
    instrumento_nivel = relationship("Instrumento_Nivel", back_populates="clases")
    profesor_instrumento = relationship("Profesor_Instrumento", back_populates="clases")

class Descuento(Base):
    __tablename__ = 'descuento'
    __table_args__ = {'schema': 'armonia'}
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)
    porcentaje = Column(Float)
    inscripciones = relationship("Inscripcion", back_populates="descuento")

class Profesor(Base):
    __tablename__ = 'profesor'
    __table_args__ = {'schema': 'armonia'}
    id = Column(Integer, primary_key=True, index=True)
    profesor = Column(String, index=True)
    profesor_instrumentos = relationship("Profesor_Instrumento", back_populates="profesor")

class Profesor_Instrumento(Base):
    __tablename__ = 'profesor_instrumento'
    __table_args__ = {'schema': 'armonia'}
    id = Column(Integer, primary_key=True, index=True)
    profesor_id = Column(Integer, ForeignKey('armonia.profesor.id'))
    instrumento_id = Column(Integer, ForeignKey('armonia.instrumento.id'))
    profesor = relationship("Profesor", back_populates="profesor_instrumentos")
    instrumento = relationship("Instrumento", back_populates="profesor_instrumentos")
    clases = relationship("Clase", back_populates="profesor_instrumento")

class Instrumento(Base):
    __tablename__ = 'instrumento'
    __table_args__ = {'schema': 'armonia'}
    id = Column(Integer, primary_key=True, index=True)
    instrumento = Column(String, index=True)
    pack_id = Column(Integer, ForeignKey('armonia.pack.id'))
    profesor_instrumentos = relationship("Profesor_Instrumento", back_populates="instrumento")
    instrumento_niveles = relationship("Instrumento_Nivel", back_populates="instrumento")
    pack = relationship("Pack", back_populates="instrumentos")

class Instrumento_Nivel(Base):
    __tablename__ = 'instrumento_nivel'
    __table_args__ = {'schema': 'armonia'}
    id = Column(Integer, primary_key=True, index=True)
    instrumento_id = Column(Integer, ForeignKey('armonia.instrumento.id'))
    nivel_id = Column(Integer, ForeignKey('armonia.nivel.id'))
    instrumento = relationship("Instrumento", back_populates="instrumento_niveles")
    nivel = relationship("Nivel", back_populates="instrumento_niveles")
    clases = relationship("Clase", back_populates="instrumento_nivel")

class Nivel(Base):
    __tablename__ = 'nivel'
    __table_args__ = {'schema': 'armonia'}
    id = Column(Integer, primary_key=True, index=True)
    nivel = Column(String, index=True)
    instrumento_niveles = relationship("Instrumento_Nivel", back_populates="nivel")

class Pack(Base):
    __tablename__ = 'pack'
    __table_args__ = {'schema': 'armonia'}
    id = Column(Integer, primary_key=True, index=True)
    pack = Column(String, index=True)
    precio = Column(Float)
    instrumentos = relationship("Instrumento", back_populates="pack")