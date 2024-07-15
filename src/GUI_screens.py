import streamlit as st

def home_screen():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía{sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Bienenido/a a la página de gestión de su base de datos.</h2>""", unsafe_allow_html=True)

def screen_alumnos():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía{sax}{trumpet} </h1>""", unsafe_allow_html=True)

    st.markdown("""<h2 style="text-align: center;">Gestion de alumnos</h2>""", unsafe_allow_html=True)


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
        st.button("Nuevo Alumno", type = "primary")

        actualizar_alumno = st.button("Actualizar datos de alumno", type = "primary")

        borrar_alumno = st.button("Eliminar alumno de la base de datos", type = "primary")

        consultar_alumno = st.button("Consultar datos de un alumno", type = "primary")

def screen_profesores():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía{sax}{trumpet} </h1>""", unsafe_allow_html=True)

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
        st.button("Nuevo Profesor", type = "primary")

        actualizar_alumno = st.button("Actualizar datos de profesor", type = "primary")

        borrar_alumno = st.button("Eliminar profesor de la base de datos", type = "primary")

        consultar_alumno = st.button("Consultar datos de un profesor", type = "primary")

def screen_precios():
    trumpet = "\U0001f3ba"
    sax = "\U0001f3b7"

    st.markdown(f"""<h1 style="text-align: center;"> {trumpet} {sax} Escuela Armonía{sax}{trumpet} </h1>""", unsafe_allow_html=True)

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
        nuevo_alumno = st.button("Actualizar precios de pack de instrumentos", type = "primary")

        actualizar_alumno = st.button("Actualizar porcentaje de descuentos", type = "primary")

        borrar_alumno = st.button("Consultar precios por pack de instrumentos", type = "primary")

        consultar_alumno = st.button("Consultar tipos de descuentos", type = "primary")