import psycopg2

# Datos de conexión
host = "localhost"
database = "armonia"
user = "postgres"
password = "1234"

try:
    # Conectar a la base de datos
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    
    # Crear un cursor
    cur = conn.cursor()
    
    # Ejecutar una consulta para obtener profesores
    cur.execute("SELECT * FROM profesor;")
    resultados_profesores = cur.fetchall()
    
    # Mostrar los resultados de la tabla profesor
    print("Profesores:")
    for fila in resultados_profesores:
        print(fila)
    
    # Ejecutar una consulta para obtener alumnos
    cur.execute("SELECT * FROM alumno;")
    resultados_alumnos = cur.fetchall()
    
    # Mostrar los resultados de la tabla alumno
    print("\nAlumnos:")
    for fila in resultados_alumnos:
        print(fila)
        
    # Cerrar el cursor y la conexión
    cur.close()
    conn.close()

except Exception as error:
    print(f"Error al conectar a la base de datos: {error}")
