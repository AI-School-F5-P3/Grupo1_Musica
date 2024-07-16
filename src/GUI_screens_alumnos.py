import streamlit as st
import pandas as pd
from GUI_screens import change_screen
from API_calls_get import get_alumnos
from API_calls_put import update_alumno
from API_calls_delete import borrar_alumno
from API_calls_post import create_alumno

def screen_nuevo_alumno():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Nuevo registro de alumno</h2>""", unsafe_allow_html=True)

    nombre = st.text_input("Nombre del alumno")

    apellidos = st.text_input("Apellidos del alumno")

    age = st.number_input("Edad del alumno", value = 6, min_value = 6, max_value = 100, step = 1)

    tfn_number = st.text_input("Número de teléfono")

    email = st.text_input("Correo electrónico")

    family = st.selectbox(label = "¿Tiene un familiar inscrito en nuestro centro?", options = ["Si", "No"])

    family_bool = True if family == 'Si' else False

    instrumento = st.selectbox("Clase", options = ["Flauta", "Piano", "Guitarra", "Saxo", "Canto"])
    
    if instrumento == 'Piano':
        options = ["Mar", "Flor", "Álvaro", "Marifé", "Nayara"]
    elif instrumento == 'Guitarra':
        options = ["Mar", "Flor"]
    elif instrumento == 'Bateria':
        options = ["Mar"]
    elif instrumento == 'Violin':
        options = ["Nayara"]
    elif instrumento == 'Canto':
        options = ["Marifé"]
    elif instrumento == 'Flauta':
        options = ["Mar"]
    elif instrumento == 'Saxofón':
        options = ["Nives"]
    elif instrumento == 'Clarinete':
        options = ['Nieves']
    elif instrumento == 'Percusion':
        options = ['Sofía']
    else:
        options = ["Nayara"]


    profesor = st.selectbox("Clase", options = options)

    if instrumento == 'Piano':
        options = ["Cero", "Iniciación", "Medio", "Avanzado"]
    elif instrumento == 'Guitarra':
        options = ["Iniciación", "Medio"]
    elif instrumento == 'Bateria':
        options = ["Iniciación", "Medio", "Avanzado"]
    elif instrumento == 'Flauta':
        options = ["Iniciación", "Medio"]
    elif instrumento == 'Bajo':
        options = ["Iniciación", "Medio"]
    else:
        options = ["No aplica"]

    nivel = st.selectbox("Nivel: ", options = options)

    data = {
        "nombre": nombre,
        "apellido": apellidos,
        "edad": age,
        "telefono": tfn_number,
        "correo": email,
        "familiar": family_bool,
        "total_mes": 0
    }

    if st.button("Registro", type = "primary"):
        result = create_alumno(instrumento, profesor, nivel, data)
        if result:
            st.success("Alumno registrado correctamente")
        else:
            st.error("Hubo un error registrando los datos.")
    
    if st.button("Atras", type = "primary"):
        change_screen('screen_alumnos')
        st.rerun()


def screen_actualizar_alumno():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Nueva inscripcion de alumno</h2>""", unsafe_allow_html=True)

    nombre = st.text_input("Nombre del alumno")

    apellidos = st.text_input("Apellidos del alumno")

    nuevo_nombre = st.text_input("Nuevo nombre del alumno")

    nuevos_apellidos = st.text_input("Nuevos apellidos del alumno")

    age = st.number_input("Edad del alumno", max_value = 100, step = 1)

    tfn_number = st.text_input("Número de teléfono")

    email = st.text_input("Correo electrónico")

    family = st.selectbox(label = "¿Tiene un familiar inscrito en nuestro centro?", options = ["Si", "No"])

    family_bool = True if family == 'Si' else False

    data = {}

    if nuevo_nombre:
        data["nombre"] = nuevo_nombre
    if nuevos_apellidos:
        data["apellido"] = nuevos_apellidos
    if age and age >= 0:
        data["edad"] = age
    if tfn_number:
        data["telefono"] = tfn_number
    if email:
        data["correo"] = email
    if family:
        data["familiar"] = family_bool
    data["total_mes"] = 0

    if  st.button("Actualizar datos", type = "primary"):
        result = update_alumno(nombre, apellidos, data)
        if result:
            st.success("Datos actaulizados correctamente")
        else:
            st.error("Hubo un error actualizando los datos.")


    if st.button("Atras", type = "primary"):
        change_screen('screen_alumnos')
        st.rerun()


def screen_borrar_alumno():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Eliminar alumno de nuestros registros</h2>""", unsafe_allow_html=True)

    nombre = st.text_input("Nombre del alumno")

    apellido = st.text_input("Apellidos del alumno")

    if st.button("DELETE", type = "primary"):
        result = borrar_alumno(nombre, apellido)
        if result:
            st.success("Alumno eliminado correctamente")
        else:
            st.error("Hubo un error eliminando los datos")

    if st.button("Atras", type = "primary"):
        change_screen('screen_alumnos')
        st.rerun()

def screen_get_alumno():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Consultar registro de alumno</h2>""", unsafe_allow_html=True)

    nombre = st.text_input("Nombre del alumno")

    apellidos = st.text_input("Apellidos del alumno")

    if st.button("Get CSV", type = "primary"):
        data, df = get_alumnos(nombre, apellidos)
        st.write(df)
    
    if st.button("Get JSON", type = "primary"):
        data, df = get_alumnos(nombre, apellidos)
        st.write(data)
    

    if st.button("Atras", type = "primary"):
        change_screen('screen_alumnos')
        st.rerun()

