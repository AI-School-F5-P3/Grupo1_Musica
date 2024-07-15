import streamlit as st
from GUI_screens import home_screen, screen_alumnos, screen_precios, screen_profesores

if 'screen' not in st.session_state:
    st.session_state.screen = 'home'

def change_screen(new_screen):
    st.session_state.screen = new_screen

st.set_page_config(layout="wide")

opciones = ["Home", "Alumnos", "Profesores", "Precios"]
st.sidebar.header("Menu")
seleccion = st.sidebar.selectbox("Navegación", opciones)

# Custom HTML/CSS for the banner
custom_html = """
<div class="banner">
    <img src="https://www.mtgpics.com/pics/art/sld/605.jpg" alt="Banner Image" height = 500 width = 1000>
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

# Selección menu lateral
if seleccion == 'Home':
    change_screen('home')

elif seleccion == "Alumnos":
    change_screen('screen_alumnos')

elif seleccion == "Profesores":
    change_screen('screen_profesores')

elif seleccion == 'Precios':
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



if seleccion == "Registrar nuevo alumno":
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía{sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Nuevo registro de alumno</h2>""", unsafe_allow_html=True)

    name = st.text_input("Nombre del alumno")

    surname = st.text_input("Apellidos")

    age = st.number_input("Edad del alumno", value = 6, min_value = 6, max_value = 100, placeholder = "Edad..", step = 1)

    prefix = st.number_input("Prefijo telefono", value = 34, max_value = 99, placeholder = "Prefijo", step = 1)

    tfn_number = st.text_input("Número de teléfono")

    email = st.text_input("Correo electrónico")

    familiy = st.selectbox(label = "¿Tiene un familiar inscrito en nuestro centro?", options = ["Si", "No"])

    instrumento = st.selectbox("Clase", options = ["Flauta", "Piano", "Guitarra", "Saxo", "Canto"])

    nivel = st.selectbox("Nivel: ", options = ["Cero", "Inicio", "Medio", "Avanzado", "No aplica"])

    enviar = st.button("Registrar", type = "primary")

if seleccion == "Consultas BBDD":
    computer = "\U0001f4bb"
    st.markdown(f"""<h1 style="text-align: center;"> {computer} Consulta base de datos {computer} </h1>""", unsafe_allow_html=True)

    name = st.text_input("Nombre del alumno")

    surname = st.text_input("Apellidos")
    
    instrumento = st.selectbox("Clase", options = ["Flauta", "Piano", "Guitarra", "Saxo", "Canto"])

    nivel = st.selectbox("Nivel: ", options = ["Cero", "Inicio", "Medio", "Avanzado", "No aplica"])

    enviar = st.button("Consultar", type = "primary")

if seleccion == "Editar precios":
    money = "\U0001f4b0"
    st.markdown(f"""<h1 style="text-align: center;"> {money} Modificar precios {money} </h1>""", unsafe_allow_html=True)
    instrumento = st.selectbox("Clase", options = ["Flauta", "Piano", "Guitarra", "Saxo", "Canto"])
    precio = st.number_input(label = "Precio de la clase", value = 0.00 , min_value = 0.00, step = 0.01)
    enviar = st.button("Editar", type = "primary")

