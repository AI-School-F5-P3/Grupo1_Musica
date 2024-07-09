# Escuela de música Armonía

### Introducción

...

### 1. Instalación

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

 Debemos asegurarnos de haber intruducido esta linea al path en variables de entorno:
 
    C:\Program Files\PostgreSQL\16\bin

