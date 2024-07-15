import streamlit as st
import pandas as pd
from GUI_screens import change_screen
from API_calls_get import get_precios, get_descuentos

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