import requests


def borrar_alumno(nombre, apellidos):
    url = 'http://127.0.0.1:8000/alumnos/delete/{nombre}/{apellidos}'.format(
        nombre=nombre,
        apellidos=apellidos
    )

    # Encabezados de la solicitud
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.delete(url, headers=headers)

    # Verificar el estado de la solicitud
    if response.status_code == 200:
        # La solicitud fue exitosa
        return True
    else:
        # Ocurrió un error
        print(f'Error al hacer la solicitud: {response.status_code}')
        return False
    

def borrar_profesor(nombre):
    url = 'http://127.0.0.1:8000/profesores/delete/{nombre}'.format(
        nombre=nombre
    )
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.delete(url, headers=headers)

    # Verificar el estado de la solicitud
    if response.status_code == 200:
        # La solicitud fue exitosa
        return True
    else:
        # Ocurrió un error
        print(f'Error al hacer la solicitud: {response.status_code}')
        return False    