import streamlit as st
import pandas as pd
from API_calls import get_alumnos, get_profesores, get_precios, get_descuentos

def change_screen(new_screen):
    st.session_state.screen = new_screen

def change_subscreen(new_subscreen):
    return new_subscreen

def home_screen():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Bienenido/a a la página de gestión de su base de datos.</h2>""", unsafe_allow_html=True)

def screen_alumnos():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Gestión de alumnos</h2>""", unsafe_allow_html=True)

    col1, col2, col3 , col4, col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3:
        if st.button("Nuevo Alumno", type = "primary"):
            change_screen('screen_nuevo_alumno')
            st.rerun()

        if st.button("Actualizar datos de alumno", type = "primary"):
            change_screen('screen_actualizar_alumno')
            st.rerun()

        if st.button("Eliminar alumno de la base de datos", type = "primary"):
            change_screen('screen_borrar_alumno')
            st.rerun()

        if st.button("Consultar datos de un alumno", type = "primary"):
            change_screen('screen_get_alumno')
            st.rerun()

def screen_profesores():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Gestión de profesores</h2>""", unsafe_allow_html=True)

    col1, col2, col3 , col4, col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3:
        if st.button("Nuevo Profesor", type = "primary"):
            change_screen('screen_nuevo_profesor')
            st.rerun()

        if st.button("Actualizar datos de profesor", type = "primary"):
            change_screen('screen_actualizar_profesor')
            st.rerun()

        if st.button("Eliminar profesor de la base de datos", type = "primary"):
            change_screen('screen_borrar_profesor')
            st.rerun()

        if st.button("Consultar datos de un profesor", type = "primary"):
            change_screen('screen_get_profesor')
            st.rerun()
    
def screen_precios():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Gestión de finanzas</h2>""", unsafe_allow_html=True)

    col1, col2, col3 , col4, col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3:
        if st.button("Actualizar precios de pack de instrumentos", type = "primary"):
            change_screen('screen_actualizar_precios')
            st.rerun()

        if st.button("Actualizar porcentaje de descuentos", type = "primary"):
            change_screen('screen_actualizar_descuentos')
            st.rerun()

        if st.button("Consultar precios por pack de instrumentos", type = "primary"):
            change_screen('screen_consultar_precios')
            st.rerun()

        if st.button("Consultar tipos de descuentos", type = "primary"):
            change_screen('screen_consultar_descuentos')
            st.rerun()

def screen_nuevo_alumno():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Nuevo registro de alumno</h2>""", unsafe_allow_html=True)

    st.text_input("Nombre del alumno")

    st.text_input("Apellidos del alumno")

    age = st.number_input("Edad del alumno", value = 6, min_value = 6, max_value = 100, step = 1)

    tfn_number = st.text_input("Número de teléfono")

    email = st.text_input("Correo electrónico")

    familiy = st.selectbox(label = "¿Tiene un familiar inscrito en nuestro centro?", options = ["Si", "No"])

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

    enviar = st.button("Registrar", type = "primary")

    if st.button("Atras", type = "primary"):
        change_screen('screen_alumnos')
        st.rerun()


def screen_actualizar_alumno():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Nueva inscripcion de alumno</h2>""", unsafe_allow_html=True)

    st.text_input("Nombre del alumno")

    st.text_input("Apellidos del alumno")

    age = st.number_input("Edad del alumno", value = 6, min_value = 6, max_value = 100, step = 1)

    tfn_number = st.text_input("Número de teléfono")

    email = st.text_input("Correo electrónico")

    familiy = st.selectbox(label = "¿Tiene un familiar inscrito en nuestro centro?", options = ["Si", "No"])

    enviar = st.button("Registrar", type = "primary")

    if st.button("Atras", type = "primary"):
        change_screen('screen_alumnos')
        st.rerun()


def screen_borrar_alumno():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Eliminar alumno de nuestros registros</h2>""", unsafe_allow_html=True)

    st.text_input("Nombre del alumno")

    st.text_input("Apellidos del alumno")

    st.button("DELETE", type = "primary")

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


def screen_nuevo_profesor():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Registrar nuevo profesor</h2>""", unsafe_allow_html=True)

    nombre = st.text_input("Nombre del profesor")

    instrumento = st.selectbox("Clase", options = ["Flauta", "Piano", "Guitarra", "Saxo", "Canto"])

    st.button('Enviar', type = "primary")
    if st.button('Atrás', type = "primary"):
        change_screen('screen_profesores')
        st.rerun()


def screen_actualizar_profesor():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Modificar datos de profesor</h2>""", unsafe_allow_html=True)

    nombre = st.text_input("Nombre del profesor")

    instrumento = st.selectbox("Clase", options = ["Flauta", "Piano", "Guitarra", "Saxo", "Canto"])

    st.button('Enviar', type = "primary")
    if st.button('Atrás', type = "primary"):
        change_screen('screen_profesores')
        st.rerun()

def screen_borrar_profesor():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Borrar registros de profesor</h2>""", unsafe_allow_html=True)

    nombre = st.text_input("Nombre del profesor")

    st.button('DELETE', type = "primary")
    if st.button('Atrás', type = "primary"):
        change_screen('screen_profesores')
        st.rerun()

def screen_get_profesor():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Consultar registros de profesor</h2>""", unsafe_allow_html=True)

    nombre = st.text_input("Nombre del profesor")

    if st.button("Get CSV", type = "primary"):
        data, df = get_profesores(nombre)
        st.write(df)
    
    if st.button("Get JSON", type = "primary"):
        data, df = get_profesores(nombre)
        st.write(data)

    if st.button('Atrás', type = "primary"):
        change_screen('screen_profesores')
        st.rerun()


def screen_actualizar_precios():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)
    st.markdown("""<h2 style="text-align: center;">Actualizar precios por pack de instrumentos</h2>""", unsafe_allow_html=True)
    instrumentos = ['Canto, Percusión', 'Piano, Guitarra, Batería y Flauta', 'Violin y Bajo', 'Clarinete y Saxofón']
    pack = st.selectbox("Instrumentos", options = instrumentos)
    precio = st.number_input("Precio de la clase", value = 0.00, min_value = 0.00, max_value = 10000.00, step = 0.01)
    st.button('Actualizar', type = 'primary')
    if st.button('Atrás', type = "primary"):
        change_screen('screen_precios')
        st.rerun()

def screen_actualizar_descuentos():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)
    st.markdown("""<h2 style="text-align: center;">Actualizar descuentos</h2>""", unsafe_allow_html=True)
    descuentos = ["Familiar en la escuela", "Segundo curso del mismo instrumento", "Tercer curso del mismo instrumento", "Sin descuento"]
    instrumento = st.selectbox("Tipo de descuentos", options = descuentos)
    id_descuentos = st.number_input("Descuento a aplicar", value = 0.1, min_value = 0.1, max_value = 100.0, step = 0.1)
    st.button('Actualizar', type = 'primary')
    if st.button('Atrás', type = "primary"):
        change_screen('screen_precios')
        st.rerun()

def screen_consultar_precios():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)
    st.markdown("""<h2 style="text-align: center;">Consultar precios</h2>""", unsafe_allow_html=True)
    packs = ['Canto, Percusión', 'Piano, Guitarra, Batería y Flauta', 'Violin y Bajo', 'Clarinete y Saxofón']
    id_pack = st.selectbox("Instrumento a consultar precio", options = packs)
    if st.button('Get CSV', type = 'primary'):
        data = get_precios(id_pack)
        st.write(pd.DataFrame(data))
    if st.button('Get JSON'):
        data = get_precios(id_pack)
        st.write(data)
    if st.button('Atrás', type = "primary"):
        change_screen('screen_precios')
        st.rerun()
    
def screen_consultar_descuentos():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)
    st.markdown("""<h2 style="text-align: center;">Consultar descuentos</h2>""", unsafe_allow_html=True)
    descuentos = ["Familiar en la escuela", "Segundo curso del mismo instrumento", "Tercer curso del mismo instrumento", "Sin descuento"]
    id_descuentos = st.selectbox("Id para consultar descuentos", options = descuentos)
    if st.button('Get CSV', type = 'primary'):
        data = get_descuentos(id_descuentos)
        st.write(pd.DataFrame(data))
    if st.button('Get JSON', type = 'primary'):
        data = get_descuentos(id_descuentos)
        st.write(data)
    if st.button('Atrás', type = "primary"):
        change_screen('screen_precios')
        st.rerun()
