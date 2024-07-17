# Imagen de python
FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos 
COPY requirements.txt /app/requirements.txt
COPY .env /app/.env
COPY main.py /app/main.py
COPY models.py /app/models.py
COPY database.py /app/database.py
COPY crud.py /app/crud.py
COPY schemas.py /app/schemas.py
COPY logger.py /app/logger.py
# Instalar requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto
EXPOSE 8000

# Compando de inicio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]