import streamlit as st
import pandas as pd

def change_screen(new_screen):
    st.session_state.screen = new_screen

def home_screen():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Bienvenido/a a la página de gestión de su base de datos.</h2>""", unsafe_allow_html=True)

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

        if st.button("Nueva inscripción de alumno existente", type = "primary"):
            change_screen('screen_nueva_inscripcion')
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






