-- Establecer la codificación de caracteres a UTF8
\encoding UTF8

-- Conectarse a la base de datos postgres
\c postgres

-- Cerrar todas las conexiones activas a la base de datos 'armonia'
SELECT pg_terminate_backend(pid)  -- Terminar la conexión usando el PID
FROM pg_stat_activity
WHERE datname = 'armonia' AND pid <> pg_backend_pid();  -- Excluir la conexión actual

-- Conectarse a la base de datos 'armonia'
\c armonia

-- Establecer la codificación de cliente a UTF8
SET client_encoding TO 'UTF8';

-- Agregar un comentario descriptivo sobre la base de datos 'armonia'
COMMENT ON DATABASE armonia
    IS 'Base de datos para la escuela de música Armonía';

CREATE SCHEMA IF NOT EXISTS armonia;
