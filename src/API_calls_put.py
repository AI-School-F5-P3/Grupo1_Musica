import requests
from logger import logger

def update_alumno(nombre, apellidos, data):
    url = 'http://127.0.0.1:8000/alumnos/update'

    # Encabezados de la solicitud
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    # Construir la URL completa
    full_url = f'{url}?alumno_nombre={nombre}&alumno_apellidos={apellidos}'

    response = requests.put(full_url, headers=headers, json=data)

    # Verificar el estado de la solicitud
    if response.status_code == 200:
        # La solicitud fue exitosa
        data = response.json()  # Convertir la respuesta JSON a un diccionario Python
        return True
    else:
        # Ocurrió un error
        logger.error(f'Error al hacer la solicitud: {response.status_code}')
        print(f'Error al hacer la solicitud: {response.status_code}')

def update_profesor(nombre, data):
    url = 'http://127.0.0.1:8000/profesores/update'

    full_url = f'{url}?profesor_nombre={nombre}'

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.put(full_url, headers=headers, json = data)

    #built_url = response.url
    #print(f'Generated URL: {built_url}')

    if response.status_code == 200:
        # La solicitud fue exitosa
        data = response.json()  # Convertir la respuesta JSON a un diccionario Python
        return True
    else:
        # Ocurrió un error
        logger.error(f'Error al hacer la solicitud: {response.status_code}')
        print(f'Error al hacer la solicitud: {response.status_code}')


def update_precios(pack, data):
    url = 'http://127.0.0.1:8000/precios/update'

    full_url = f'{url}?pack_name={pack}'

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.put(full_url, headers=headers, json = data)

    #built_url = response.url
    #print(f'Generated URL: {built_url}')

    if response.status_code == 200:
        # La solicitud fue exitosa
        data = response.json()  # Convertir la respuesta JSON a un diccionario Python
        return True
    else:
        # Ocurrió un error
        logger.error(f'Error al hacer la solicitud: {response.status_code}')
        print(f'Error al hacer la solicitud: {response.status_code}')

def update_descuentos(descripcion, data):
    url = 'http://127.0.0.1:8000/descuentos/update'

    full_url = f'{url}?descuento_desc={descripcion}'

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.put(full_url, headers=headers, json = data)

    built_url = response.url
    print(f'Generated URL: {built_url}')

    if response.status_code == 200:
        # La solicitud fue exitosa
        data = response.json()  # Convertir la respuesta JSON a un diccionario Python
        return True
    else:
        # Ocurrió un error
        logger.error(f'Error al hacer la solicitud: {response.status_code}')
        print(f'Error al hacer la solicitud: {response.status_code}')