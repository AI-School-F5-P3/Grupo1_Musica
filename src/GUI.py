import streamlit as st

st.write("Añadir alumnos a la base de datos")

name = st.text_input("Nombre del alumno")

surname = st.text_input("Apellidos")

age = st.number_input("Edad del alumno", value = 6, min_value = 6, max_value = 100, placeholder = "Edad..", step = 1)

prefix = st.number_input("Prefijo telefono", value = 34, max_value = 99, placeholder = "Prefijo", step = 1)

tfn_number = st.text_input("Número de teléfono")

email = st.text_input("Correo electrónico")

familiy = st.selectbox(label = "¿Tiene un familiar inscrito en nuestro centro?", options = ["Si", "No"])