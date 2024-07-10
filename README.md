# Escuela de música Armonía

### Introducción

...

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

    DATABASE_URL=postgres://tu_usuario:tu_contraseña@localhost/nombre_basedatos
    DB_HOST=localhost
    DB_USER=tu_usuario
    DB_PASS=tu_contraseña
    DB_NAME=nombre_basedatos
    SECRET_KEY=password_server
    DEBUG=true

En estas variables de entorno debemos especificar el nombre de usuario que tengamos en postgreSQL y la contraseña, además del nombre de la base de datos, que en nuestro caso hemos optado por llamar "Armonia" pero que también es modificable.

Para cargar las variables de entorno desde el archivo load_env.ps1:

En powershell de windows abrir la carpeta config:

    cd "C:\Documentos\Grupo1_Musica\config
    
    .\load_env.ps1

Puede producirse un error de que no tenemos permiso para ejecutar scripts desde powershell, si se quiere modificar ejecutar el comando (Decisión personal):

    Set-ExecutionPolicy Unrestricted

Una vez se han cargado las variables de entorno, generamos la base de datos con el comando:

    createdb -U postgres -W armonia

Y a continuación ejecutar el script

    psql -U $env:DB_USER -d $env:DB_NAME -f "C:\Documentos\Grupo1_Musica\db\init.sql"

IMPORTANTE

Recordad actualizar las rutas de los archivos a las que se correspondan en vuestros ordenadores personales.

### macOS/Linux

Instalacion para sistemas operativos macOS/linux

Navegamos hasta el directorio principal y creamos un entorno virtual

    python3 -m venv venv

Activar el entorno virtual:

    source venv/bin/activate

Ejecutamos el siguiente comando para descargar las dependencias

    pip install -r requirements.txt   

Configurar las variables de entorno en el archivo .env en el directorio raíz del proyecto (Grupo1_Musica):

    DATABASE_URL=postgres://tu_usuario:tu_contraseña@localhost/nombre_basedatos
    DB_HOST=localhost
    DB_USER=tu_usuario
    DB_PASS=tu_contraseña
    DB_NAME=nombre_basedatos
    SECRET_KEY=password_server
    DEBUG=true

Ejecutar el script SQL:

    psql -U $DB_USER -d $DB_NAME -f db/init.sql
