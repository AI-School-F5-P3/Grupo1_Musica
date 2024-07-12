from sqlalchemy.orm import Session
from models import Alumno
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

def insert_data():
    db = SessionLocal()
    try:
        alumno1 = Alumno(
            nombre="Juan",
            apellido="Perez",
            edad=20,
            telefono="123456789",
            correo="juan.perez@example.com",
            familiar=False,
            descuento=0
        )
        db.add(alumno1)
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    insert_data()
