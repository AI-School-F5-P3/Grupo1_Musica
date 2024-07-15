import requests

def get_alumnos(nombre, apellidos):
    base_url = 'http://127.0.0.1:8000/alumnos/get/'

    # Nombre del alumno y parámetros adicionales
    alumno_nombre = nombre
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
        return(data)
    else:
        # Ocurrió un error
        print(f'Error al hacer la solicitud: {response.status_code}')