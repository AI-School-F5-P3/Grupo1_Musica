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