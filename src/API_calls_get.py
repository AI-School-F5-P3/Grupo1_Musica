import requests
import pandas as pd

def flatten_json(data, prefix=''):
    result = {}
    for key, value in data.items():
        new_key = f"{prefix}{key}"
        if isinstance(value, dict):
            result.update(flatten_json(value, new_key + '_'))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                result.update(flatten_json(item, f"{new_key}{i}_"))
        else:
            result[new_key] = value
    return result

def get_alumnos(nombre, apellidos):
    base_url = 'http://127.0.0.1:8000/alumnos/get/'

    # Nombre del alumno y parámetros adicionales
    params = {
        'nombre': nombre,
        'apellido': apellidos
    }

    # Construir la URL completa con los parámetros
    url = f'{base_url}'
    query_params = '&'.join([f'{key}={value}' for key, value in params.items()])
    url = f'{url}?{query_params}'

    # Encabezados de la solicitud
    headers = {
        'accept': 'application/json'
    }

    # Realizar la solicitud GET
    response = requests.get(url, headers=headers)

    # Verificar el estado de la solicitud
    if response.status_code == 200:
        # La solicitud fue exitosa
        data = response.json()  # Convertir la respuesta JSON a un diccionario Python
        flattened_data = flatten_json(data)
        df = pd.DataFrame([flattened_data])
        return data, df
    else:
        # Ocurrió un error
        print(f'Error al hacer la solicitud: {response.status_code}')

def get_profesores(nombre):
    base_url = 'http://127.0.0.1:8000/profesores/get'

    # Parámetros de la solicitud
    params = {
        'nombre': nombre
    }

    # Encabezados de la solicitud
    headers = {
        'accept': 'application/json'
    }

    # Realizar la solicitud GET
    response = requests.get(base_url, headers=headers, params=params)

    # Verificar el estado de la solicitud
    if response.status_code == 200:
        # La solicitud fue exitosa
        data = response.json()  # Convertir la respuesta JSON a un diccionario Python

        instrumentos = [instrumento["nombre_instrumento"] for instrumento in data["instrumentos"]]

        # Crear un DataFrame de pandas con los instrumentos
        df = pd.DataFrame(instrumentos, columns=["instrumento"])

        # Agregar la columna del nombre del profesor
        df["nombre_profesor"] = data["nombre_profesor"]

        # Reordenar las columnas según el orden deseado
        df = df[["nombre_profesor", "instrumento"]]

        return data, df
    else:
        # Ocurrió un error
        print(f'Error al hacer la solicitud: {response.status_code}')


def get_precios(pack):
    base_url = 'http://127.0.0.1:8000/precios/get'
    
    params = {
        'pack': pack
    }

    # Encabezados de la solicitud
    headers = {
        'accept': 'application/json'
    }

    # Realizar la solicitud GET
    response = requests.get(base_url, headers=headers, params=params)

    built_url = response.url
    print(f'Generated URL: {built_url}')

    if response.status_code == 200:
        data = response.json()
        data_list = [data]
        return data_list
    else:
        # Ocurrió un error
        print(f'Error al hacer la solicitud: {response.status_code}')


def get_descuentos(descripcion):
    base_url = 'http://127.0.0.1:8000/descuentos/get'

    params = {
        'descuento': descripcion
    }

    # Encabezados de la solicitud
    headers = {
        'accept': 'application/json'
    }

    # Realizar la solicitud GET
    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        data_list = [data]
        return data_list
    else:
        # Ocurrió un error
        print(f'Error al hacer la solicitud: {response.status_code}')