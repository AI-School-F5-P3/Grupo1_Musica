# Escuela de música Armonía

### 1. Instalación

Clonamos el repositorio

    git clone https://github.com/AI-School-F5-P3/Grupo1_Musica.git

Antes de construir el docker se pueden modificar usuarios y contraseñas en streamlit/GUI.py y en las variables locales en los archivos .env.

Con postgreSQL y docker-desktop instalados en el ordenador ejecutamos en la carpeta raiz de la app:

    docker-compose up --build

Una vez terminen de construirse los contenedores ya estará disponible la API, base de datos y GUI.
 - Para acceder a la API: http://localhost:8000
 - Para acceder a la interfaz gráfica Streamlit: http://localhost:8501
     - Password: Admin
     - Contraseña: 1234
  
En el siguiente enlace puede encontrar manuales más desarrollados en niveles usuario y técnico:

https://quasar-shark-5ea.notion.site/Documentaci-n-Escuela-de-m-sica-0c1a40ca41b240f59f93b58ce7cbc4f2

### DEPRECADO AHORA ESTA TODO DOCKERIZADO PERO DEJAMOS LAS INSTRUCCIONES POR SI ALGUIEN QUIERE CONSTRUIRLO LOCAL (REQUIERE CAMBIAR CIERTAS RUTAS EN LOS SCRIPTS)

(Las rutas a cambiar son:
- En las API_Calls de la GUI cambiar en la url api por 127.0.0.1
- En el archivo database.py cambiar en la url @armonia-db2:5432 por @localhost:5433
)

Navegamos hasta el directorio principal y creamos un entorno virtual

### Windows

    uv venv

Lo activamos

    .venv\Scripts\activate

Ejecutamos el siguiente comando para descargar las dependencias

    uv pip install -r requirements.txt   

Configurar las variables de entorno en el archivo .env en el directorio raíz del proyecto (Grupo1_Musica):

    DATABASE_URL=postgres://tu_usuario:tu_contraseña@localhost/nombre_basedatos
    DB_HOST=localhost
    DB_USER=tu_usuario
    DB_PASS=tu_contraseña
    DB_NAME=nombre_basedatos
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
    
    psql -h localhost -p 5433 -U admin_user -a armonia

Cuando esté conectada la base de datos, podemos lanzar la api ejecutando el script 'main.py' dentro de /src/. Para inicar streamlit y disponer de una interfaz gráfica más amigable ejecutar el código:

    streamlit run src/GUI.py

### macOS/Linux

Instalacion para sistemas operativos macOS/linux

Ejecutar el script SQL:

    psql -U $DB_USER -d $DB_NAME -f db/init.sql






