import streamlit as st

st.set_page_config(layout="wide")

opciones = ["Registrar nuevo alumno", "Consultas BBDD", "Editar precios"]
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

if seleccion == "Consultas BBDD":
    st.markdown("# En construcción")


if seleccion == "Editar precios":
    st.markdown("# En construcción")
    