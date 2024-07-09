# Importamos biblioteca dotenv.
from dotenv import load_dotenv
import os

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Acceder a las variables de entorno
database_url = os.getenv('DATABASE_URL')
db_host = os.getenv ('DB_HOST')
secret_key = os.getenv('SECRET_KEY')
db_user = os.getenv ('DB_USER')
db_pass= os.getenv ('DB_PASS')
debug_mode = os.getenv('DEBUG')


print(f"Database URL: {database_url}")
print(f"Database Host: {db_host}")
print(f"Secret Key: {secret_key}")
print(f"User: {db_user}")
print(f"Secret password: {db_pass}")
print(f"Debug Mode: {debug_mode}")

