import streamlit as st
import pandas as pd
from GUI_screens import change_screen
from API_calls_get import get_profesores

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
