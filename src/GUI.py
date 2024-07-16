import streamlit as st
from logger import logger
from GUI_screens import change_screen, home_screen, screen_alumnos, screen_precios, screen_profesores
from GUI_screens_alumnos import screen_nuevo_alumno, screen_actualizar_alumno, screen_borrar_alumno, screen_get_alumno , screen_nueva_inscripcion
from GUI_screens_profesores import screen_actualizar_profesor, screen_borrar_profesor, screen_get_profesor, screen_nuevo_profesor
from GUI_screens_precios import screen_actualizar_descuentos, screen_actualizar_precios, screen_consultar_descuentos, screen_consultar_precios

# Función para definir una pantalla de login inicial
def login():
    '''
    username se ha dijado como admin y password como 1234 para facilitar las pruebas, pero lo correcto sería externalizar estos datos.
    '''
    st.sidebar.subheader("Login")
    username = st.sidebar.text_input("Usuario")
    password = st.sidebar.text_input("Contraseña", type="password")
    if st.sidebar.button("Iniciar sesión"):
        # Verificar las credenciales (simulado)
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            logger.info(f'Se ha iniciado sesión en streamlit')
            st.success("¡Inicio de sesión exitoso!")
        else:
            logger.error(f'Inicio de sesión en Streamlit fallido')
            st.error("Usuario o contraseña incorrectos.")

# Configuración inicial de la página
if 'screen' not in st.session_state:
    st.session_state.screen = 'home'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

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

def apply_custom_css():
    st.markdown("""
        <style>
        .button-container {
            display: flex;
            justify-content: center;
            margin-bottom: 10px;
        }
        .stButton button {
            width: 220px;
            height: 60px;
            background-color: #6943ff; /* Purple background */
            color: white; /* Text color */
            border: 1px solid #5227ff; /* Border color */
            border-radius: 8px;
            font-size: 18px; /* Font size */
            margin: 5px;
        }
        .stButton button:hover {
            background-color: #5e3fe0; /* Darker purple on hover */
        }
        /* Streamlit dark theme inspired by Shades of Purple */
        body {
            background-color: #2d2a55; /* Dark purple background */
            color: #e0e0e0; /* Light text */
        }
        .stMarkdown {
            color: #e0e0e0; /* Light text */
        }
        .css-18ni7ap, .css-1d391kg {
            background-color: #2d2a55; /* Dark purple background */
            color: #e0e0e0; /* Light text */
        }
        .css-1d391kg p {
            color: #e0e0e0; /* Light text */
        }
        .css-1v0mbdj a {
            color: #ff9d00; /* Link color */
        }
        .css-1v0mbdj a:hover {
            color: #ff9900; /* Link hover color */
        }
        </style>
    """, unsafe_allow_html=True)

# Display the custom HTML
st.components.v1.html(custom_html)
apply_custom_css()

# Renderización del login
if not st.session_state.logged_in:
    login()
else:
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
    elif st.session_state.screen == 'screen_nueva_inscripcion':
        screen_nueva_inscripcion()
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