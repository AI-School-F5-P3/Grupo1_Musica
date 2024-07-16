# Usa la imagen base oficial de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt .

# Instala las dependencias de tu aplicación
RUN pip install -r requirements.txt

# Copia todo el contenido de la carpeta actual al directorio /app en el contenedor
COPY . .

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]