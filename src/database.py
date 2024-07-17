from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import text
import os
from dotenv import main

main.load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Crea una instancia de declarative_base
Base = declarative_base()

# Cadena de conexión 
# Acceder a las variables de entorno

db_type = os.getenv('DB_TYPE')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_DB')
db_schema = os.getenv('DB_SCHEMA')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASSWORD')

database_url = f"{db_type}://{db_user}:{db_pass}@armonia-db2:5432/{db_name}"

print(database_url)

SQLALCHEMY_DB = database_url

# Crea el motor asíncrono
engine = create_async_engine(SQLALCHEMY_DB, echo=True)

# Crea una clase de sesión asíncrona
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def init_db():
    async with engine.begin() as conn:
        try:
            # Establecer el search_path al esquema deseado usando SQL raw
            await conn.execute(text(f'SET search_path TO {db_schema}'))
            # Crear todas las tablas definidas por Base.metadata en el esquema
            await conn.run_sync(Base.metadata.create_all)
            print("Base de datos inicializada correctamente.")
        except Exception as e:
            print(f"Error al inicializar la base de datos: {e}")
            raise

async def shutdown_db():
    await SessionLocal.close()