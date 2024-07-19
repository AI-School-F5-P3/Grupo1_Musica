import streamlit as st
import pandas as pd
from GUI_screens import change_screen
from API_calls_get import get_precios, get_descuentos
from API_calls_put import update_precios, update_descuentos
from logger import logger

def screen_actualizar_precios():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)
    st.markdown("""<h2 style="text-align: center;">Actualizar precios por pack de instrumentos</h2>""", unsafe_allow_html=True)
    instrumentos = ['Canto, Percusión', 'Piano, Guitarra, Batería y Flauta', 'Violín y Bajo', 'Clarinete y Saxofón']
    pack = st.selectbox("Instrumentos", options = instrumentos)
    precio = st.number_input("Precio de la clase", value = 0.00, min_value = 0.00, max_value = 10000.00, step = 0.01)
    data = {
        "precio": precio
    }
    if st.button('Actualizar'):
        result = update_precios(pack, data)
        if result:
            st.success("Datos actualizados correctamente")
            logger.info(f'Precios de {pack} actualizados correctamente a través de Streamlit')
        else:
            st.error("Hubo un error actualizando los datos.")
            logger.error(f'Error actualizando precios de {pack} a través de Streamlit')
    if st.button('Atrás'):
        change_screen('screen_precios')
        st.rerun()

def screen_actualizar_descuentos():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)
    st.markdown("""<h2 style="text-align: center;">Actualizar descuentos</h2>""", unsafe_allow_html=True)
    descuentos = ["Familiar en la escuela", "Segundo curso del mismo instrumento", "Tercer curso del mismo instrumento", "Sin descuento"]
    descripcion = st.selectbox("Tipo de descuentos", options = descuentos)
    porcentaje = st.number_input("Descuento a aplicar", value = 0.0, min_value = 0.0, max_value = 100.0, step = 0.1)
    data = {
        "porcentaje": porcentaje
    }
    if st.button('Actualizar'):
        result = update_descuentos(descripcion, data)
        if result:
            st.success("Datos actualizados correctamente")
            logger.info(f'Descuentos de {descripcion} actualizados correctamente a través de Streamlit')
        else:
            st.error("Hubo un error actualizando los datos.")
            logger.error(f'Error actualizando descuentos de {descripcion} a través de Streamlit')
    if st.button('Atrás'):
        change_screen('screen_precios')
        st.rerun()

def screen_consultar_precios():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"
    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía {sax}{trumpet} </h1>""", unsafe_allow_html=True)
    st.markdown("""<h2 style="text-align: center;">Consultar precios</h2>""", unsafe_allow_html=True)
    packs = ['Canto, Percusión', 'Piano, Guitarra, Batería y Flauta', 'Violín y Bajo', 'Clarinete y Saxofón']
    id_pack = st.selectbox("Instrumento a consultar precio", options = packs)
    if st.button('Get CSV', type = 'primary'):
        data, df = get_precios(id_pack)
        logger.info(f'Obtenidos datos de precios {id_pack} en CSV a través de Streamlit')
        st.write(df)
    if st.button('Get JSON'):
        data, df = get_precios(id_pack)
        logger.info(f'Obtenidos datos de precios {id_pack} en JSON a través de Streamlit')
        st.write(data)
    if st.button('Atrás'):
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
        data, df = get_descuentos(id_descuentos)
        logger.info(f'Obtenidos datos de Descuentos {id_descuentos} en CSV a través de Streamlit')
        st.write(df)
    if st.button('Get JSON', type = 'primary'):
        logger.info(f'Obtenidos datos de Descuentos {id_descuentos} en JSON a través de Streamlit')
        data, df = get_descuentos(id_descuentos)
        st.write(data)
    if st.button('Atrás'):
        change_screen('screen_precios')
        st.rerun()