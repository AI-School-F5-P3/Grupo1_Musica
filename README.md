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

Cargar las variables de entorno desde el archivo .env:

    $envFilePath = ".env"
    Get-Content $envFilePath | ForEach-Object {
        if ($_ -notmatch '^\s*#' -and $_ -match '^\s*(\w+)\s*=\s*(.*)\s*$') {
            $name = $matches[1]
            $value = $matches[2]
            [System.Environment]::SetEnvironmentVariable($name, $value)
        }
    }

Ejecutar el script

    psql -U $env:DB_USER -d $env:DB_NAME -f "C:\Users\maria\MROSA\BOOTCAMP IA\Proyectos\proyecto_5\Grupo1_Musica\db\init.sql"

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
