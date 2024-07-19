import streamlit as st
import pandas as pd
from GUI_screens import change_screen
from API_calls_get import get_profesores, get_all_profesores
from API_calls_put import update_profesor
from API_calls_delete import borrar_profesor
from API_calls_post import create_profesor
from logger import logger

def validate_data(data):
    missing_fields = [field for field, value in data.items() if not value]
    return missing_fields

def screen_nuevo_profesor():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Registrar nuevo profesor</h2>""", unsafe_allow_html=True)

    nombre = st.text_input("Nombre del profesor")

    # Lista de opciones inicial
    opciones_iniciales = ["Piano", "Guitarra", "Batería", "Violín", "Canto", "Flauta", "Saxofón", "Clarinete", "Percusión", "Bajo"]

    # Incluir None en las opciones iniciales
    opciones_iniciales_con_none = ["None"] + opciones_iniciales

    # Selectbox para el primer instrumento
    instrumento1 = st.selectbox("Clase 1", options=opciones_iniciales_con_none)

    # Filtrar opciones para el segundo selectbox
    opciones2 = [opcion for opcion in opciones_iniciales if opcion != instrumento1]
    opciones2 = ["None"] + opciones2
    instrumento2 = st.selectbox("Clase 2", options=opciones2)

    # Filtrar opciones para el tercer selectbox
    opciones3 = [opcion for opcion in opciones2 if opcion != instrumento2 and opcion != "None"]
    opciones3 = ["None"] + opciones3
    instrumento3 = st.selectbox("Clase 3", options=opciones3)

    # Filtrar opciones para el cuarto selectbox
    opciones4 = [opcion for opcion in opciones3 if opcion != instrumento3 and opcion != "None"]
    opciones4 = ["None"] + opciones4
    instrumento4 = st.selectbox("Clase 4", options=opciones4)

    # Filtrar opciones para el quinto selectbox
    opciones5 = [opcion for opcion in opciones4 if opcion != instrumento4 and opcion != "None"]
    opciones5 = ["None"] + opciones5
    instrumento5 = st.selectbox("Clase 5", options=opciones5)

    if nombre:

        if st.button("Registro"):
            result = create_profesor(nombre, instrumento1, instrumento2, instrumento3, instrumento4, instrumento5)
            if result:
                st.success("Profesor registrado correctamente")
                logger.info(f'Profesor {nombre} registrado correctamente a través de Streamlit')
            else:
                st.error("Hubo un error registrando los datos.")
                logger.error(f'Error registrando profesor {nombre} a través de Streamlit')
    else:
        st.warning("Por favor, ingrese el nombre del profesor")

    if st.button('Atrás'):
        change_screen('screen_profesores')
        st.rerun()


def screen_actualizar_profesor():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Modificar datos de profesor</h2>""", unsafe_allow_html=True)

    nombre = st.text_input("Nombre del profesor")

    nuevo_nombre = st.text_input("Nuevo nombre del profesor")

    data = {
        "profesor": nuevo_nombre
    }

    if nombre:
            
        if st.button('Actualizar', type = "primary"):
            result = update_profesor(nombre, data)
            if result:
                st.success("Datos actualizados correctamente")
                logger.info(f'Datos de Profesor {nombre} actualizados correctamente a través de Streamlit')
            else:
                st.error("Hubo un error actualizando los datos.")
                logger.error(f'Error actualizando datos de profesor {nombre} a través de Streamlit')
    
    else:
        
        st.warning("Por favor, ingerese el nombre del profesor")
                
    if st.button('Atrás'):
        change_screen('screen_profesores')
        st.rerun()

def screen_borrar_profesor():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Borrar registros de profesor</h2>""", unsafe_allow_html=True)

    nombre = st.text_input("Nombre del profesor")
    
    if nombre:

        if st.button("DELETE"):
            result = borrar_profesor(nombre)
            if result:
                st.success("Profesor eliminado correctamente")
                logger.info(f'Profesor {nombre} eliminado correctamente a través de Streamlit')
            else:
                st.error("Hubo un error eliminando los datos")
                logger.error(f'Error eliminando Profesor {nombre} a través de Streamlit')
    else:
        st.warning('Por favor, ingrese el nombre del profesor')

    if st.button('Atrás'):
        change_screen('screen_profesores')
        st.rerun()

def screen_get_profesor():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Consultar registros de profesor</h2>""", unsafe_allow_html=True)

    nombre = st.text_input("Nombre del profesor")

    if nombre:

        if st.button("Get CSV"):
            data, df = get_profesores(nombre)
            logger.info(f'Obtenidos datos de Profesor {nombre} en CSV a través de Streamlit')
            st.write(df)
        
        if st.button("Get JSON"):
            data, df = get_profesores(nombre)
            logger.info(f'Obtenidos datos de Profesor {nombre} en JSON a través de Streamlit')
            st.write(data)

    else:
        st.warning('Por favor, ingrese el nombre del profesor')

    if st.button('Atrás'):
        change_screen('screen_profesores')
        st.rerun()

def screen_get_all_profesores():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Consultar todos los registros de profesores</h2>""", unsafe_allow_html=True)

    if st.button("Get CSV"):
        data, df = get_all_profesores()
        logger.info(f'Obtenidos datos de Profesores en CSV a través de Streamlit')
        st.write(df)
    
    if st.button("Get JSON"):
        data, df = get_all_profesores()
        logger.info(f'Obtenidos datos de Profesores en JSON a través de Streamlit')
        st.write(data)
    

    if st.button("Atras"):
        change_screen('screen_profesores')
        st.rerun()