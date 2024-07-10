from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text
from datetime import datetime

app = FastAPI()

posts = []

class Alumno(BaseModel):
    id: str
    nombre: str
    apellidos: str
    edad: int
    telefono: str
    correo: str
    familiar: bool = False
    descuent: int
    created_at: datetime = datetime.now()

@app.get("/")
def read_root():
    return{"message": "this is working"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post: Alumno):
    print(post)
    return "recieved"