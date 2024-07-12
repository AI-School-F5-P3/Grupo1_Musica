from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from database import Base


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
    profesor_instrumento = Column(Integer, ForeignKey("profesor_ionstrumento.id"))
    alumno_id = Column(Integer, ForeignKey("alumno.id"))

    alumno = relationship("Alumno", back_populates="clases")
    instrumento_nivel = relationship("InstrumentoNivel")
    profesor_instrumento = relationship("ProfesorInstrumento")


class Instrumento(Base):
    __tablename__ = 'instrumento'

    id = Column(Integer, primary_key=True, index=True)
    intrumento = Column(String, index=True)
    pack = Column(Integer, ForeignKey("pack.id"))

    #niveles = relationship("InstrumentoNivel", back_populates="Instrumento")
    #packs = relationship("Packs", back_populates="Instrumento")


class Nivel(Base):
    __tablename__ = 'nivel'

    id = Column(Integer, primary_key=True, index=True)
    nivel = Column(String, index=True)

    #instrumento = relationship("InstrumentoNivel", back_populates="nivel")


class Profesor(Base):
    __tablename__ = 'profesor'

    id = Column(Integer, primary_key=True, index=True)
    profesor = Column(String, index=True)

    #instrumento = relationship("ProfesorIsntrumento", back_populates="profesor")


class InstrumentoNivel(Base):
    __tablename__ = 'instrumento_nivel'

    id = Column(Integer, primary_key=True, index=True)
    instrumento_id = Column(Integer, ForeignKey("instrumento.id"))
    nivel_id = Column(Integer, ForeignKey("nivel.id"))

    instrumento = relationship("Instrumento", back_populates="niveles")
    nivel = relationship("Nivel", back_populates="instrumentos")
    #clases = relationship("ClasesPorAlumno", back_populates="instrumento_nivel")


class ProfesorInstrumento(Base):
    __tablename__ = 'profesor_instrumento'

    id = Column(Integer, primary_key=True, index=True)
    profesor_id = Column(Integer, ForeignKey("profesor.id"))
    instrumento_id = Column(Integer, ForeignKey("instrumento.id"))

    profesor = relationship("Profesor", back_populates="instrumentos")
    isntrumento = relationship("Isntrumento", back_populates="profesores")
    #clases = relationship("ClasePorAlumno", back_populates="profesor_instrumento")


class Pack(Base):
    __tablename__ = 'pack'

    id = Column(Integer, primary_key=True, index=True)
    pack = Column(String, index=True)
    precio = Column(Integer)

    #instrumentos = relationship("Instrumento", back_populates="pack")


engine = create_engine('sqlite:///escuela.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
