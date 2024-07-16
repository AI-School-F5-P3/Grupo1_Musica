import requests

def create_alumno(instrumento, profesor, nivel, data):
    base_url = 'http://127.0.0.1:8000/alumnos/crear_nuevo'

    # Construir la URL completa
    full_url = f'{base_url}?nombre_instrumento={instrumento}&nombre_profesor={profesor}&nombre_nivel={nivel}'

    # Nombre del alumno y parámetros adicionales
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }


    try:
        response = requests.post(full_url, headers=headers, json=data)

        # Verificar el estado de la solicitud
        if response.status_code == 200:
            # La solicitud fue exitosa
            data = response.json()  # Convertir la respuesta JSON a un diccionario Python si es necesario
            return True
        else:
            # Ocurrió un error
            print(f'Error al hacer la solicitud: {response.status_code}')
            return False
    except requests.exceptions.RequestException as e:
        # Capturar excepciones de requests
        print(f'Error en la solicitud HTTP: {e}')
        return False

def create_profesor(profesor, instrumento1, instrumento2=None, instrumento3=None, instrumento4=None, instrumento5=None):
    base_url = 'http://127.0.0.1:8000/profesores/crear'
    
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    # Crear el diccionario de datos con los instrumentos opcionales
    data = {
        "profesor": profesor,
        "instrumento1": instrumento1 if instrumento1 != "None" else None
    }
    
    if instrumento2 != "None":
        data["instrumento2"] = instrumento2
    if instrumento3 != "None":
        data["instrumento3"] = instrumento3
    if instrumento4 != "None":
        data["instrumento4"] = instrumento4
    if instrumento5 != "None":
        data["instrumento5"] = instrumento5
    
    # Limpiar el diccionario de datos eliminando las claves con valor None
    data = {k: v for k, v in data.items() if v is not None}
    
    try:
        response = requests.post(base_url, headers=headers, json=data)
        
        built_url = response.url
        print(f'Generated URL: {built_url}')

        if response.status_code == 200:
            # La solicitud fue exitosa
            return response.json()  # Convertir la respuesta JSON a un diccionario Python si es necesario
        else:
            # Ocurrió un error
            print(f'Error al hacer la solicitud: {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        # Capturar excepciones de requests
        print(f'Error en la solicitud HTTP: {e}')
        return None
