# Paso 1: Instalar docker desktop

Instalar la aplicación de docker desktop desde la página oficial de docker.

# Paso 2: Instalar postgreSQL en nuestra máquina local

Instalar postgreSQL en nuestro ordenador y añadirlo al path (variables de entorno)

# Paso 3: Construir contendor
Modificar las variables de entorno del archivo .env con los datos que queramos.

Acceder a la carpeta Docker y desde la terminal ejecutar el código:
    docker-compose up --build

Ya podemos acceder a la base de datos utilizando en la terminal:
    psql -h localhost -p 5433 -U postgres -armonia

O a través de pgadmin4 o cualquier GUI para gestión de bases postgreSQL