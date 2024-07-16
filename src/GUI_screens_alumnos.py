import streamlit as st
import pandas as pd
from GUI_screens import change_screen
from API_calls_get import get_alumnos, get_all_alumnos
from API_calls_put import update_alumno
from API_calls_delete import borrar_alumno
from API_calls_post import create_alumno, create_inscripcion
from logger import logger

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

    instrumento = st.selectbox("Clase", options = ["Piano", "Guitarra", "Batería", "Violín", "Canto", "Flauta", "Saxofón", "Clarinete", "Percusión", "Bajo"])
    
    if instrumento == 'Piano':
        options = ["Mar", "Flor", "Álvaro", "Marifé", "Nayara"]
    elif instrumento == 'Guitarra':
        options = ["Mar", "Flor"]
    elif instrumento == 'Batería':
        options = ["Mar"]
    elif instrumento == 'Violin':
        options = ["Nayara"]
    elif instrumento == 'Canto':
        options = ["Marifé"]
    elif instrumento == 'Flauta':
        options = ["Mar"]
    elif instrumento == 'Saxofón':
        options = ["Nieves"]
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
    elif instrumento == 'Batería':
        options = ["Iniciación", "Medio", "Avanzado"]
    elif instrumento == 'Flauta':
        options = ["Iniciación", "Medio"]
    elif instrumento == 'Bajo':
        options = ["Iniciación", "Medio"]
    else:
        options = ["Iniciación"]

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
            logger.info(f'Alumno {nombre} registrado correctamente a través de Streamlit')
        else:
            st.error("Hubo un error registrando los datos.")
            logger.error(f'Error registrando Alumno {nombre} a través de Streamlit')
    
    if st.button("Atras", type = "primary"):
        change_screen('screen_alumnos')
        st.rerun()

def screen_nueva_inscripcion():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Nueva inscripción de alumno</h2>""", unsafe_allow_html=True)

    nombre = st.text_input("Nombre del alumno")
    apellido = st.text_input("Apellido del alumno")

    instrumento = st.selectbox("Instrumento", options=["Flauta", "Piano", "Guitarra", "Saxofón", "Canto"])
    
    if instrumento == 'Piano':
        options = ["Mar", "Flor", "Álvaro", "Marifé", "Nayara"]
    elif instrumento == 'Guitarra':
        options = ["Mar", "Flor"]
    elif instrumento == 'Batería':
        options = ["Mar"]
    elif instrumento == 'Violín':
        options = ["Nayara"]
    elif instrumento == 'Canto':
        options = ["Marifé"]
    elif instrumento == 'Flauta':
        options = ["Mar"]
    elif instrumento == 'Saxofón':
        options = ["Nieves"]
    elif instrumento == 'Clarinete':
        options = ['Nieves']
    elif instrumento == 'Percusión':
        options = ['Sofía']
    else:
        options = ["Nayara"]

    profesor = st.selectbox("Profesor", options=options)

    if instrumento == 'Piano':
        options = ["Cero", "Iniciación", "Medio", "Avanzado"]
    elif instrumento == 'Guitarra':
        options = ["Iniciación", "Medio"]
    elif instrumento == 'Batería':
        options = ["Iniciación", "Medio", "Avanzado"]
    elif instrumento == 'Flauta':
        options = ["Iniciación", "Medio"]
    elif instrumento == 'Bajo':
        options = ["Iniciación", "Medio"]
    else:
        options = ["Iniciación"]

    nivel = st.selectbox("Nivel", options=options)

    if nombre and apellido:  # Verificar que se haya ingresado nombre y apellido
        data = {
            "nombre": nombre,
            "apellido": apellido
        }
        if st.button("Mostrar datos", type = "primary"):
            st.write(data)

        if st.button("Registrar", type="primary"):
            result = create_inscripcion(instrumento, profesor, nivel, data)
            if result:
                st.success("Alumno registrado correctamente.")
                logger.info(f'Alumno {nombre} inscrito correctamente a través de Streamlit')
            else:
                st.error("Hubo un error registrando los datos.")
                logger.error(f'Error registrando nueva inscsripción de {nombre} a través de Streamlit')
    else:
        st.warning("Por favor, ingresa el nombre y apellido del alumno.")


def screen_actualizar_alumno():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Actualización de alumno</h2>""", unsafe_allow_html=True)

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
            st.success("Datos actualizados correctamente")
            logger.info(f'Datos de Alumno {nombre} actualizados correctamente a través de Streamlit')
        else:
            st.error("Hubo un error actualizando los datos.")
            logger.error(f'Error actualizando datos de Alumno {nombre} a través de Streamlit')


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
            logger.info(f'Alumno {nombre} eliminado correctamente a través de Streamlit')
        else:
            st.error("Hubo un error eliminando los datos")
            logger.error(f'Error eliminando Alumno {nombre} a través de Streamlit')

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
        logger.info(f'Obtenidos datos de Alumno {nombre} en CSV a través de Streamlit')
        st.write(df)
    
    if st.button("Get JSON", type = "primary"):
        data, df = get_alumnos(nombre, apellidos)
        logger.info(f'Obtenidos datos de Alumno {nombre} en JSON a través de Streamlit')
        st.write(data)
    

    if st.button("Atras", type = "primary"):
        change_screen('screen_alumnos')
        st.rerun()

def screen_get_all_alumnos():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Consultar todos los registros de alumnos</h2>""", unsafe_allow_html=True)

    if st.button("Get CSV"):
        data, df = get_all_alumnos()
        logger.info(f'Obtenidos datos de Alumnos en CSV a través de Streamlit')
        st.write(df)
    
    if st.button("Get JSON"):
        data, df = get_all_alumnos()
        logger.info(f'Obtenidos datos de Alumnos en JSON a través de Streamlit')
        st.write(data)
    

    if st.button("Atras"):
        change_screen('screen_alumnos')
        st.rerun()
