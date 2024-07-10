# Escuela de música Armonía

### Introducción

...

### 1. Instalación

### Windows

Clonamos el repositorio

    git clone https://github.com/AI-School-F5-P3/Grupo1_Musica.git

Navegamos hasta el directorio principal y creamos un entorno virtual
    
    uv venv

Lo activamos

    .venv\Scripts\activate


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

    ```bash
    cd Grupo1_Musica
    python3 -m venv venv

Activar el entorno virtual:

    source venv/bin/activate

Activar el entorno virtual:

    source venv/bin/activate

Configurar las variables de entorno en el archivo .env en el directorio raíz del proyecto (Grupo1_Musica):

    DB_USER=tu_usuario
    DB_PASSWORD=tu_contraseña
    DB_NAME=nombre_basedatos

Ejecutar el script SQL:

    psql -U $DB_USER -d $DB_NAME -f db/init.sql
