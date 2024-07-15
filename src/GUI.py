import streamlit as st
from GUI_screens import change_screen, home_screen, screen_alumnos, screen_precios, screen_profesores, screen_nuevo_alumno, screen_actualizar_alumno, screen_borrar_alumno, screen_get_alumno, screen_actualizar_profesor, screen_borrar_profesor, screen_get_profesor, screen_nuevo_profesor, screen_actualizar_descuentos, screen_actualizar_precios, screen_consultar_descuentos, screen_consultar_precios

# Configuración inicial de la página
if 'screen' not in st.session_state:
    st.session_state.screen = 'home'

st.set_page_config(layout="wide")

# Custom HTML/CSS for the banner
custom_html = """
<div class="banner">
    <img src="https://www.mtgpics.com/pics/art/sld/605.jpg" alt="Banner Image" height="500" width="1000">
</div>
<style>
    .banner {
        width: 100%;
        height: 700px;
        overflow: hidden;
    }
    .banner img {
        width: 100%;
        object-fit: cover;
    }
</style>
"""
# Display the custom HTML
st.components.v1.html(custom_html)

# Selección del menú lateral
st.sidebar.header("Menú de Navegación")
if st.sidebar.button("Home"):
    change_screen('home')
if st.sidebar.button("Alumnos"):
    change_screen('screen_alumnos')
if st.sidebar.button("Profesores"):
    change_screen('screen_profesores')
if st.sidebar.button("Precios"):
    change_screen('screen_precios')

# Renderización de las pantallas
if st.session_state.screen == 'home':
    home_screen()
elif st.session_state.screen == 'screen_alumnos':
    screen_alumnos()
elif st.session_state.screen == 'screen_profesores':
    screen_profesores()
elif st.session_state.screen == 'screen_precios':
    screen_precios()
elif st.session_state.screen == 'screen_nuevo_alumno':
    screen_nuevo_alumno()
elif st.session_state.screen == 'screen_actualizar_alumno':
    screen_actualizar_alumno()
elif st.session_state.screen == 'screen_borrar_alumno':
    screen_borrar_alumno()
elif st.session_state.screen == 'screen_get_alumno':
    screen_get_alumno()
elif st.session_state.screen == 'screen_nuevo_profesor':
    screen_nuevo_profesor()
elif st.session_state.screen == 'screen_actualizar_profesor':
    screen_actualizar_profesor()
elif st.session_state.screen == 'screen_borrar_profesor':
    screen_borrar_profesor()
elif st.session_state.screen == 'screen_get_profesor':
    screen_get_profesor()
elif st.session_state.screen == 'screen_actualizar_precios':
    screen_actualizar_precios()
elif st.session_state.screen == 'screen_actualizar_descuentos':
    screen_actualizar_descuentos()
elif st.session_state.screen == 'screen_consultar_precios':
    screen_consultar_precios()
elif st.session_state.screen == 'screen_consultar_descuentos':
    screen_consultar_descuentos()