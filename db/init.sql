-- \encoding UTF8

-- \c postgres

-- Eliminar la base de datos si existe
DROP DATABASE IF EXISTS lolo;

-- Creación de la base de datos con template0
CREATE DATABASE lolo
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'es_ES.UTF-8'
    LC_CTYPE = 'es_ES.UTF-8'
    TEMPLATE = template0
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE lolo
    IS 'Base de datos para la escuela de música Armonía';

-- Conectarse a la base de datos
\c lolo

-- Creación de la tabla pack
CREATE TABLE IF NOT EXISTS pack (
    id SERIAL PRIMARY KEY,
    pack VARCHAR(100) NOT NULL,
    precio INTEGER
);

COMMENT ON TABLE pack IS 'Tabla que almacena la información de los paquetes de clases ofrecidos';
COMMENT ON COLUMN pack.id IS 'Identificador único del paquete';
COMMENT ON COLUMN pack.pack IS 'Nombre del paquete de clases';
COMMENT ON COLUMN pack.precio IS 'Precio del paquete de clases';

-- Creación de la tabla instrumento
CREATE TABLE IF NOT EXISTS instrumento (
    id SERIAL PRIMARY KEY,
    instrumento VARCHAR(100) NOT NULL,
    pack_id INTEGER,
    FOREIGN KEY (pack_id) REFERENCES pack(id)
);

COMMENT ON TABLE instrumento IS 'Tabla que almacena los instrumentos musicales';
COMMENT ON COLUMN instrumento.id IS 'Identificador único del instrumento';
COMMENT ON COLUMN instrumento.instrumento IS 'Nombre del instrumento';
COMMENT ON COLUMN instrumento.pack_id IS 'Identificador del pack al que pertenece el instrumento, referencia a pack(id)';

-- Creación de la tabla nivel
CREATE TABLE IF NOT EXISTS nivel (
    id SERIAL PRIMARY KEY,
    nivel VARCHAR(100) NOT NULL
);

COMMENT ON TABLE nivel IS 'Tabla que almacena los niveles de aprendizaje';
COMMENT ON COLUMN nivel.id IS 'Identificador único del nivel';
COMMENT ON COLUMN nivel.nivel IS 'Nombre del nivel de aprendizaje';

-- Creación de la tabla profesor
CREATE TABLE IF NOT EXISTS profesor (
    id SERIAL PRIMARY KEY,
    profesor VARCHAR(100) NOT NULL
);

COMMENT ON TABLE profesor IS 'Tabla que almacena la información de los profesores';
COMMENT ON COLUMN profesor.id IS 'Identificador único del profesor';
COMMENT ON COLUMN profesor.profesor IS 'Nombre del profesor';

-- Creación de la tabla instrumento_nivel
CREATE TABLE IF NOT EXISTS instrumento_nivel (
    id SERIAL PRIMARY KEY,
    instrumento_id INTEGER,
    nivel_id INTEGER,
    FOREIGN KEY (instrumento_id) REFERENCES instrumento(id),
    FOREIGN KEY (nivel_id) REFERENCES nivel(id)
);

COMMENT ON TABLE instrumento_nivel IS 'Tabla que almacena la relación entre instrumentos y niveles';
COMMENT ON COLUMN instrumento_nivel.id IS 'Identificador único de la relación entre instrumento y nivel';
COMMENT ON COLUMN instrumento_nivel.instrumento_id IS 'Identificador del instrumento';
COMMENT ON COLUMN instrumento_nivel.nivel_id IS 'Identificador del nivel';

-- Creación de la tabla profesor_instrumento
CREATE TABLE IF NOT EXISTS profesor_instrumento (
    id SERIAL PRIMARY KEY,
    profesor_id INTEGER,
    instrumento_id INTEGER,
    FOREIGN KEY (profesor_id) REFERENCES profesor(id),
    FOREIGN KEY (instrumento_id) REFERENCES instrumento(id)
);

COMMENT ON TABLE profesor_instrumento IS 'Tabla que almacena la relación entre profesores e instrumentos';
COMMENT ON COLUMN profesor_instrumento.id IS 'Identificador único de la relación entre profesor e instrumento';
COMMENT ON COLUMN profesor_instrumento.profesor_id IS 'Identificador del profesor';
COMMENT ON COLUMN profesor_instrumento.instrumento_id IS 'Identificador del instrumento';

-- Creación de la tabla alumno
CREATE TABLE IF NOT EXISTS alumno (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    edad INTEGER,
    telefono VARCHAR(20),
    correo VARCHAR(100),
    familiar BOOLEAN
);

COMMENT ON TABLE alumno IS 'Tabla que almacena la información de los alumnos';
COMMENT ON COLUMN alumno.id IS 'Identificador único del alumno';
COMMENT ON COLUMN alumno.nombre IS 'Nombre del alumno';
COMMENT ON COLUMN alumno.apellido IS 'Apellido del alumno';
COMMENT ON COLUMN alumno.edad IS 'Edad del alumno';
COMMENT ON COLUMN alumno.telefono IS 'Número de teléfono del alumno';
COMMENT ON COLUMN alumno.correo IS 'Correo electrónico del alumno';
COMMENT ON COLUMN alumno.familiar IS 'Indicador si el alumno tiene un familiar en la escuela';

-- Creación de la tabla clase
CREATE TABLE IF NOT EXISTS clase (
    id SERIAL PRIMARY KEY,
    instrumento_nivel_id INTEGER,
    profesor_instrumento_id INTEGER,
    FOREIGN KEY (instrumento_nivel_id) REFERENCES instrumento_nivel(id),
    FOREIGN KEY (profesor_instrumento_id) REFERENCES profesor_instrumento(id)
);

COMMENT ON TABLE clase IS 'Tabla que almacena la asignación de clases por alumno';
COMMENT ON COLUMN clase.id IS 'Identificador único de la asignación de clase por alumno';
COMMENT ON COLUMN clase.instrumento_nivel_id IS 'Identificador del nivel de instrumento asignado al alumno, referencia a instrumento_nivel(id)';
COMMENT ON COLUMN clase.profesor_instrumento_id IS 'Identificador del profesor de instrumento asignado al alumno, referencia a profesor_instrumento(id)';

-- Creación de la tabla descuento
CREATE TABLE IF NOT EXISTS descuento (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL,
    porcentaje INTEGER NOT NULL CHECK (porcentaje > 0)
);

COMMENT ON TABLE descuento IS 'Tabla que define los descuentos aplicables';
COMMENT ON COLUMN descuento.id IS 'Identificador único del descuento';
COMMENT ON COLUMN descuento.descripcion IS 'Descripción del descuento';
COMMENT ON COLUMN descuento.porcentaje IS 'Porcentaje de descuento aplicable';

-- Creación de la tabla inscripcion
CREATE TABLE IF NOT EXISTS inscripcion (
    id SERIAL PRIMARY KEY,
    alumno_id INTEGER REFERENCES alumno(id),
    clase_id INTEGER REFERENCES clase(id),
    fecha_inicio DATE CHECK (fecha_inicio >= CURRENT_DATE),
    fecha_fin DATE CHECK (fecha_fin >= CURRENT_DATE),
    descuento_id INTEGER REFERENCES descuento(id)
);


COMMENT ON TABLE inscripcion IS 'Tabla que registra las inscripciones de los alumnos a las clases, incluyendo fechas, descuentos y precios finales.';
COMMENT ON COLUMN inscripcion.id IS 'Identificador único para cada inscripción.';
COMMENT ON COLUMN inscripcion.alumno_id IS 'Referencia al alumno inscrito, corresponde al ID en la tabla alumno.';
COMMENT ON COLUMN inscripcion.clase_id IS 'Referencia a la clase inscrita, corresponde al ID en la tabla clase.';
COMMENT ON COLUMN inscripcion.fecha_inicio IS 'Fecha de inicio de la inscripción. No puede ser anterior a la fecha actual.';
COMMENT ON COLUMN inscripcion.fecha_fin IS 'Fecha de fin de la inscripción. No puede ser anterior a la fecha actual.';


-- ---------------- INSERTAR DATOS --------------------- --


-- Insertar datos en la tabla pack
INSERT INTO pack (pack, precio)
VALUES 
('Canto, Percusión', 40),
('Piano, Guitarra, Batería y Flauta', 35),
('Violín y Bajo', 40),
('Clarinete y Saxofón', 40);

-- Insertar descuentos
INSERT INTO descuento (descripcion, porcentaje) VALUES
('Familiar en la escuela', 10),
('Segundo curso del mismo instrumento', 50),
('Tercer curso del mismo instrumento', 25);

-- Insertar datos en la tabla instrumento
INSERT INTO instrumento (instrumento, pack_id)
VALUES 
('Piano', 2),
('Guitarra', 2),
('Batería', 2),
('Violín', 3),
('Canto', 1),
('Flauta', 2),
('Saxofón', 4),
('Clarinete', 4),
('Percusión', 1),
('Bajo', 3);

-- Insertar datos en la tabla nivel
INSERT INTO nivel (nivel)
VALUES 
('Cero'), ('Iniciación'), ('Medio'), ('Avanzado');

-- Insertar datos en la tabla profesor
INSERT INTO profesor (profesor)
VALUES 
('Mar'), ('Flor'), ('Álvaro'), ('Marifé'), ('Nayara'), ('Nieves'), ('Sofía');

-- Insertar Relaciones entre Profesores e Instrumentos
-- Relaciones para Piano
INSERT INTO profesor_instrumento (profesor_id, instrumento_id) VALUES
(1, 1), -- Mar
(2, 1), -- Flor
(3, 1), -- Álvaro
(4, 1), -- Marifé
(5, 1); -- Nayara

-- Relaciones para Guitarra
INSERT INTO profesor_instrumento (profesor_id, instrumento_id) VALUES
(1, 2), -- Mar
(2, 2); -- Flor

-- Relaciones para Batería
INSERT INTO profesor_instrumento (profesor_id, instrumento_id) VALUES
(1, 3); -- Mar

-- Relaciones para Violín
INSERT INTO profesor_instrumento (profesor_id, instrumento_id) VALUES
(5, 4); -- Nayara

-- Relaciones para Canto
INSERT INTO profesor_instrumento (profesor_id, instrumento_id) VALUES
(4, 5); -- Marifé

-- Relaciones para Flauta
INSERT INTO profesor_instrumento (profesor_id, instrumento_id) VALUES
(1, 6); -- Mar

-- Relaciones para Saxofón
INSERT INTO profesor_instrumento (profesor_id, instrumento_id) VALUES
(6, 7); -- Nieves

-- Relaciones para Clarinete
INSERT INTO profesor_instrumento (profesor_id, instrumento_id) VALUES
(6, 8); -- Nieves

-- Relaciones para Percusión
INSERT INTO profesor_instrumento (profesor_id, instrumento_id) VALUES
(7, 9); -- Sofía

-- Relaciones para Bajo
INSERT INTO profesor_instrumento (profesor_id, instrumento_id) VALUES
(5, 10); -- Nayara


-- Insertar datos en la tabla instrumento_nivel
INSERT INTO instrumento_nivel (instrumento_id, nivel_id)
SELECT i.id, n.id
FROM instrumento i
CROSS JOIN nivel n
WHERE 
    (i.instrumento = 'Piano' AND n.nivel IN ('Cero', 'Iniciación', 'Medio', 'Avanzado')) OR
    (i.instrumento = 'Guitarra' AND n.nivel IN ('Iniciación', 'Medio')) OR
    (i.instrumento = 'Batería' AND n.nivel IN ('Iniciación', 'Medio', 'Avanzado')) OR
    (i.instrumento = 'Flauta' AND n.nivel IN ('Iniciación', 'Medio')) OR
    (i.instrumento = 'Bajo' AND n.nivel IN ('Iniciación', 'Medio')) OR
    (i.instrumento NOT IN ('Piano', 'Guitarra', 'Batería', 'Flauta', 'Bajo') AND n.nivel = 'Iniciación');

-- Insertar datos en la tabla clase
INSERT INTO clase (instrumento_nivel_id, profesor_instrumento_id)
SELECT instrumento_nivel.id, profesor_instrumento.id
FROM instrumento_nivel
JOIN profesor_instrumento ON instrumento_nivel.instrumento_id = profesor_instrumento.instrumento_id;


-- Insertar datos en la tabla alumno
INSERT INTO alumno (nombre, apellido, edad, telefono, correo, familiar)
VALUES
('Carlos', 'García', 25, '123456789', 'carlos@email.com', true),
('Ana', 'Martínez', 30, '987654321', 'ana@email.com', false),
('Juan', 'López', 20, '567890123', 'juan@email.com', false);


-- Inscripción de Carlos García
INSERT INTO inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES (
    1,
    (SELECT id FROM clase LIMIT 1), -- Selecciona el primer ID de clase disponible como ejemplo
    CURRENT_DATE,
    CURRENT_DATE + INTERVAL '1 year',
    (CASE 
        WHEN (SELECT familiar FROM alumno WHERE id = (SELECT id FROM alumno WHERE nombre = 'Carlos' AND apellido = 'García')) THEN 
            (SELECT id FROM descuento WHERE descripcion = 'Familiar en la escuela') 
        ELSE 
            NULL 
    END)
);

-- Inscripción de Ana Martínez
INSERT INTO inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES (
    (SELECT id FROM alumno WHERE nombre = 'Ana' AND apellido = 'Martínez'),
    (SELECT id FROM clase LIMIT 1), -- Selecciona el primer ID de clase disponible como ejemplo
    CURRENT_DATE,
    CURRENT_DATE + INTERVAL '1 year',
    (CASE 
        WHEN (SELECT familiar FROM alumno WHERE id = (SELECT id FROM alumno WHERE nombre = 'Ana' AND apellido = 'Martínez')) THEN 
            (SELECT id FROM descuento WHERE descripcion = 'Familiar en la escuela') 
        ELSE 
            NULL 
    END)
);

-- Inscripción de Juan López
INSERT INTO inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES (
    (SELECT id FROM alumno WHERE nombre = 'Juan' AND apellido = 'López'),
    (SELECT id FROM clase OFFSET 1 LIMIT 1), -- Selecciona el segundo ID de clase disponible como ejemplo
    CURRENT_DATE,
    CURRENT_DATE + INTERVAL '1 year',
    (CASE 
        WHEN (SELECT familiar FROM alumno WHERE id = (SELECT id FROM alumno WHERE nombre = 'Juan' AND apellido = 'López')) THEN 
            (SELECT id FROM descuento WHERE descripcion = 'Familiar en la escuela') 
        ELSE 
            NULL 
    END)
);


-- Comprobar que se hayan insertado los datos correctamente
SELECT * FROM pack;
SELECT * FROM instrumento;
SELECT * FROM nivel;
SELECT * FROM profesor;
SELECT * FROM instrumento_nivel;
SELECT * FROM profesor_instrumento;
SELECT * FROM alumno;
SELECT * FROM clase;
SELECT * FROM descuento;
SELECT * FROM inscripcion;
