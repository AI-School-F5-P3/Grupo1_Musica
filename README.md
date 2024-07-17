# Escuela de música Armonía

### 1. Instalación

Clonamos el repositorio

    git clone https://github.com/AI-School-F5-P3/Grupo1_Musica.git

### Windows

Navegamos hasta el directorio principal y creamos un entorno virtual
    
    uv venv

Lo activamos

    .venv\Scripts\activate

Ejecutamos el siguiente comando para descargar las dependencias

    uv pip install -r requirements.txt   

Configurar las variables de entorno en el archivo .env en el directorio raíz del proyecto (Grupo1_Musica):

    DATABASE_URL=postgresql+asyncpg://tu_usuario:tu_contraseña@localhost:5433/nombre_basedatos
    DB_TYPE=postgresql+asyncpg
    DB_HOST=localhost
    DB_PORT=5433
    DB_DB=nombre_basedatos
    DB_SCHEMA=nombre_schema
    DB_USER=tu_usuario
    DB_PASSWORD=tu_contraseña
    SECRET_KEY=password_server
    DEBUG=true

En estas variables de entorno debemos especificar el nombre de usuario que tengamos en postgreSQL y la contraseña, además del nombre de la base de datos, que en nuestro caso hemos optado por llamar "Armonia" pero que también es modificable.

Una vez definimos las variables de entorno, nos movemos a la carpeta Docker. En esta carpeta están las instrucciones para levantar un contenedor docker que construye la base de datos en PostgreSQL que vamos a utilizar. Para construirlo usaremos los comandos en terminal:

    docker-compose build
    docker-compose up

Una vez el docker este configurado y funcionando, debemos conectar la base de datos a nuestro postgres local, para ello podemos añadirlo en PgAdmin, registrando un nuevo servidor, con el nombre que queramos y en la pestaña conexiones los parámetros:
- Host name/address: localhost
- Port: 5433
- username: admin_user (o usuario del archivo .env)
- password: 1234 (o password del archivo .env)

También puede usarse el comando (asumiendo que tenemos psql en las variables de entorno de nuestra máquina):
    
    psql -h localhost -p 5433 -U postgres -a armonia

Cuando esté conectada la base de datos, podemos lanzar la api ejecutando el script 'main.py' dentro de /src/. Para inicar streamlit y disponer de una interfaz gráfica más amigable ejecutar el código:

    streamlit run src/GUI.py


### macOS/Linux

Instalacion para sistemas operativos macOS/linux

Ejecutar el script SQL:

    psql -U $DB_USER -d $DB_NAME -f db/init.sql
