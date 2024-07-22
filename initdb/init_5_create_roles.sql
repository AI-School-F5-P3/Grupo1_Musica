
-- ----------------------------- Creamos Roles y Usuarios -- ----------------------------- --

-- Crear un rol llamado administrator
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'administrator') THEN
        CREATE ROLE administrator;
    END IF;
END $$;


-- Conceder permiso de conexión a la base de datos 'armonia' para el rol administrator
GRANT CONNECT ON DATABASE armonia TO administrator;

-- Conceder uso del esquema 'armonia' al rol administrator
GRANT USAGE ON SCHEMA armonia TO administrator;

-- Conceder permisos de SELECT, INSERT, UPDATE y DELETE en todas las tablas del esquema 'armonia' al rol administrator
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA armonia TO administrator;

-- Alterar los privilegios predeterminados para que el rol administrator tenga permisos de SELECT, INSERT, UPDATE y DELETE en nuevas tablas
ALTER DEFAULT PRIVILEGES IN SCHEMA armonia GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO administrator;

-- Conceder uso de todas las secuencias en el esquema 'armonia' al rol administrator
GRANT USAGE ON ALL SEQUENCES IN SCHEMA armonia TO administrator; -- Las secuencias en bases de datos son objetos que generan números únicos y secuenciales. Se utilizan comúnmente para crear identificadores únicos para filas en tablas, especialmente para columnas de tipo clave primaria.

-- Alterar los privilegios predeterminados para que el rol administrator tenga permisos de USAGE en nuevas secuencias
ALTER DEFAULT PRIVILEGES IN SCHEMA armonia GRANT USAGE ON SEQUENCES TO administrator;

-- Crear un usuario llamado admin_user con una contraseña
CREATE USER admin_user WITH LOGIN PASSWORD '1234';

-- Conceder el rol administrator al usuario admin_user
GRANT administrator TO admin_user;

-- Consultar los roles existentes y sus miembros, excluyendo roles del sistema
SELECT
    r.rolname,  -- Nombre del rol
    ARRAY(SELECT b.rolname  -- Array de nombres de roles a los que pertenece
          FROM pg_catalog.pg_auth_members m
          JOIN pg_catalog.pg_roles b ON (m.roleid = b.oid)
          WHERE m.member = r.oid) as memberof
FROM pg_catalog.pg_roles r
WHERE r.rolname NOT IN ('pg_signal_backend','rds_iam',
                         'rds_replication','rds_superuser',
                         'rdsadmin','rdsrepladmin')  -- Excluir roles del sistema
ORDER BY 1;  -- Ordenar por el nombre del rol
