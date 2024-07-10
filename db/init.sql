-- Eliminar la base de datos si existe previamente
DROP DATABASE IF EXISTS armonia;

-- Crear la base de datos con el nombre 'armonia'
CREATE DATABASE armonia
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'es_ES.UTF-8'
    LC_CTYPE = 'es_ES.UTF-8'
    TEMPLATE = template0
    CONNECTION LIMIT = -1;

-- Agregar un comentario sobre la base de datos
COMMENT ON DATABASE armonia
    IS 'Base de datos para la escuela de música Armonía';

-- Conexión a la base de datos creada
\c armonia;

-- Crear la tabla pack
CREATE TABLE "pack" (
    "id" SERIAL PRIMARY KEY,
    "pack" VARCHAR(100),
    "precio" INTEGER NOT NULL
);

-- Comentarios sobre la tabla pack y sus columnas
COMMENT ON TABLE "pack" IS 'Tabla que almacena la información de los paquetes de clases ofrecidos';
COMMENT ON COLUMN "pack"."id" IS 'Identificador único del paquete';
COMMENT ON COLUMN "pack"."pack" IS 'Nombre del paquete de clases';
COMMENT ON COLUMN "pack"."precio" IS 'Precio del paquete de clases';

-- Crear la tabla instrumento
CREATE TABLE "instrumento" (
    "id" SERIAL PRIMARY KEY,
    "instrumento" VARCHAR(100) NOT NULL,
    "pack_id" INTEGER NOT NULL,
    CONSTRAINT fk_pack_id FOREIGN KEY (pack_id) REFERENCES "pack" ("id")
);

-- Comentarios sobre la tabla instrumento y sus columnas
COMMENT ON TABLE "instrumento" IS 'Tabla que almacena los instrumentos musicales';
COMMENT ON COLUMN "instrumento"."id" IS 'Identificador único del instrumento';
COMMENT ON COLUMN "instrumento"."instrumento" IS 'Nombre del instrumento';
COMMENT ON COLUMN "instrumento"."pack_id" IS 'Identificador del pack al que pertenece el instrumento, referencia a pack(id)';

-- Crear la tabla nivel
CREATE TABLE "nivel" (
    "id" SERIAL PRIMARY KEY,
    "nivel" VARCHAR(100) UNIQUE NOT NULL
);

-- Comentarios sobre la tabla nivel y sus columnas
COMMENT ON TABLE "nivel" IS 'Tabla que almacena los niveles de aprendizaje';
COMMENT ON COLUMN "nivel"."id" IS 'Identificador único del nivel';
COMMENT ON COLUMN "nivel"."nivel" IS 'Nombre del nivel de aprendizaje';

-- Crear la tabla profesor
CREATE TABLE "profesor" (
    "id" SERIAL PRIMARY KEY,
    "profesor" VARCHAR(100) UNIQUE NOT NULL
);

-- Comentarios sobre la tabla profesor y sus columnas
COMMENT ON TABLE "profesor" IS 'Tabla que almacena la información de los profesores';
COMMENT ON COLUMN "profesor"."id" IS 'Identificador único del profesor';
COMMENT ON COLUMN "profesor"."profesor" IS 'Nombre del profesor';

-- Crear la tabla instrumento_nivel
CREATE TABLE "instrumento_nivel" (
    "id" SERIAL PRIMARY KEY,
    "instrumento_id" INTEGER NOT NULL,
    "nivel_id" INTEGER NOT NULL,
    CONSTRAINT fk_instrumento_id FOREIGN KEY (instrumento_id) REFERENCES "instrumento" ("id"),
    CONSTRAINT fk_nivel_id FOREIGN KEY (nivel_id) REFERENCES "nivel" ("id")
);

-- Comentarios sobre la tabla instrumento_nivel y sus columnas
COMMENT ON TABLE "instrumento_nivel" IS 'Tabla que almacena la relación entre instrumentos y niveles';
COMMENT ON COLUMN "instrumento_nivel"."id" IS 'Identificador único de la relación entre instrumento y nivel';
COMMENT ON COLUMN "instrumento_nivel"."instrumento_id" IS 'Identificador del instrumento';
COMMENT ON COLUMN "instrumento_nivel"."nivel_id" IS 'Identificador del nivel';

-- Crear la tabla profesor_instrumento
CREATE TABLE "profesor_instrumento" (
    "id" SERIAL PRIMARY KEY,
    "profesor_id" INTEGER NOT NULL,
    "instrumento_id" INTEGER NOT NULL,
    CONSTRAINT fk_profesor_id FOREIGN KEY (profesor_id) REFERENCES "profesor" ("id"),
    CONSTRAINT fk_instrumento_id_pi FOREIGN KEY (instrumento_id) REFERENCES "instrumento" ("id")
);

-- Comentarios sobre la tabla profesor_instrumento y sus columnas
COMMENT ON TABLE "profesor_instrumento" IS 'Tabla que almacena la relación entre profesores e instrumentos';
COMMENT ON COLUMN "profesor_instrumento"."id" IS 'Identificador único de la relación entre profesor e instrumento';
COMMENT ON COLUMN "profesor_instrumento"."profesor_id" IS 'Identificador del profesor';
COMMENT ON COLUMN "profesor_instrumento"."instrumento_id" IS 'Identificador del instrumento';

-- Crear la tabla alumno
CREATE TABLE "alumno" (
    "id" SERIAL PRIMARY KEY,
    "nombre" VARCHAR(100) NOT NULL,
    "apellido" VARCHAR(100) NOT NULL,
    "edad" INTEGER,
    "telefono" VARCHAR(20) NOT NULL,
    "correo" VARCHAR(100) NOT NULL,
    "familiar" BOOLEAN,
    "total_mes" INTEGER
);

-- Comentarios sobre la tabla alumno y sus columnas
COMMENT ON TABLE "alumno" IS 'Tabla que almacena la información de los alumnos';
COMMENT ON COLUMN "alumno"."id" IS 'Identificador único del alumno';
COMMENT ON COLUMN "alumno"."nombre" IS 'Nombre del alumno';
COMMENT ON COLUMN "alumno"."apellido" IS 'Apellido del alumno';
COMMENT ON COLUMN "alumno"."edad" IS 'Edad del alumno';
COMMENT ON COLUMN "alumno"."telefono" IS 'Número de teléfono del alumno';
COMMENT ON COLUMN "alumno"."correo" IS 'Correo electrónico del alumno';
COMMENT ON COLUMN "alumno"."familiar" IS 'Si tiene un familiar en el centro';
COMMENT ON COLUMN "alumno"."total_mes" IS 'Descuento total';

-- Crear la tabla clase
CREATE TABLE "clase" (
    "id" SERIAL PRIMARY KEY,
    "instrumento_nivel_id" INTEGER NOT NULL,
    "profesor_instrumento_id" INTEGER NOT NULL,
    CONSTRAINT fk_instrumento_nivel_id FOREIGN KEY (instrumento_nivel_id) REFERENCES "instrumento_nivel" ("id"),
    CONSTRAINT fk_profesor_instrumento_id_cl FOREIGN KEY (profesor_instrumento_id) REFERENCES "profesor_instrumento" ("id")
);

-- Comentarios sobre la tabla clase y sus columnas
COMMENT ON TABLE "clase" IS 'Tabla que almacena la asignación de clases por alumno';
COMMENT ON COLUMN "clase"."id" IS 'Identificador único de la asignación de clase por alumno';
COMMENT ON COLUMN "clase"."instrumento_nivel_id" IS 'Identificador del nivel de instrumento asignado al alumno, referencia a instrumento_nivel(id)';
COMMENT ON COLUMN "clase"."profesor_instrumento_id" IS 'Identificador del profesor de instrumento asignado al alumno, referencia a profesor_instrumento(id)';

-- Crear la tabla descuento
CREATE TABLE "descuento" (
    "id" SERIAL PRIMARY KEY,
    "descripcion" VARCHAR(100),
    "porcentaje" INTEGER NOT NULL
);

-- Comentarios sobre la tabla descuento y sus columnas
COMMENT ON TABLE "descuento" IS 'Tabla que define los descuentos aplicables';
COMMENT ON COLUMN "descuento"."id" IS 'Identificador único del descuento';
COMMENT ON COLUMN "descuento"."descripcion" IS 'Descripción del descuento';
COMMENT ON COLUMN "descuento"."porcentaje" IS 'Porcentaje de descuento aplicable';

-- Crear la tabla inscripcion con restricciones de fecha
CREATE TABLE "inscripcion" (
    "id" SERIAL PRIMARY KEY,
    "alumno_id" INTEGER NOT NULL,
    "clase_id" INTEGER NOT NULL,
    "fecha_inicio" DATE NOT NULL CHECK (fecha_inicio >= CURRENT_DATE),
    "fecha_fin" DATE CHECK (fecha_fin >= CURRENT_DATE + INTERVAL '15 days'),
    "descuento_id" INTEGER NOT NULL,
    CONSTRAINT fk_alumno_id FOREIGN KEY (alumno_id) REFERENCES "alumno" ("id"),
    CONSTRAINT fk_clase_id FOREIGN KEY (clase_id) REFERENCES "clase" ("id"),
    CONSTRAINT fk_descuento_id FOREIGN KEY (descuento_id) REFERENCES "descuento" ("id"),
    CONSTRAINT chk_no_descuento_1 CHECK ("descuento_id" <> 1)
);

-- Comentarios sobre la tabla inscripcion y sus columnas
COMMENT ON TABLE "inscripcion" IS 'Tabla que registra las inscripciones de los alumnos a las clases, incluyendo fechas, descuentos y precios finales.';
COMMENT ON COLUMN "inscripcion"."id" IS 'Identificador único para cada inscripción.';
COMMENT ON COLUMN "inscripcion"."alumno_id" IS 'Referencia al alumno inscrito, corresponde al ID en la tabla alumno.';
COMMENT ON COLUMN "inscripcion"."clase_id" IS 'Referencia a la clase inscrita, corresponde al ID en la tabla clase.';
COMMENT ON COLUMN "inscripcion"."fecha_inicio" IS 'Fecha de inicio de la inscripción. No puede ser anterior a la fecha actual.';
COMMENT ON COLUMN "inscripcion"."fecha_fin" IS 'Fecha de fin de la inscripción. No puede ser anterior a la fecha actual.';
COMMENT ON COLUMN "inscripcion"."descuento_id" IS 'Descuento aplicado a la inscripción.';




-- Insertar datos en la tabla pack
INSERT INTO "pack" ("pack", "precio") VALUES
('Canto, Percusión', 40),
('Piano, Guitarra, Batería y Flauta', 35),
('Violín y Bajo', 40),
('Clarinete y Saxofón', 40);

-- Insertar datos en la tabla instrumento
INSERT INTO "instrumento" ("instrumento", "pack_id") VALUES
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
INSERT INTO "nivel" ("nivel") VALUES
('Cero'), 
('Iniciación'), 
('Medio'), 
('Avanzado');

-- Insertar datos en la tabla profesor
INSERT INTO "profesor" ("profesor") VALUES
('Mar'), 
('Flor'), 
('Álvaro'), 
('Marifé'), 
('Nayara'), 
('Nieves'), 
('Sofía');

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

-- Insertar datos en la tabla descuento
INSERT INTO "descuento" ("descripcion", "porcentaje") VALUES
('Familiar en la escuela', 10),
('Segundo curso del mismo pack', 50),
('Tercer curso del mismo pack', 75),
('Sin descuento', 0);

-- Insertar datos en la tabla alumno
INSERT INTO "alumno" ("nombre", "apellido", "edad", "telefono", "correo", "familiar", "total_mes")
VALUES
('Carlos', 'García', 25, '123456789', 'carlos@email.com', TRUE, 0),
('Ana', 'Martínez', 30, '987654321', 'ana@email.com', FALSE, 0),
('Juan', 'López', 20, '567890123', 'juan@email.com', FALSE, 0);

-- Inscripción de los alumnos en las clases específicas

-- Inscripción de Carlos García en Piano Avanzado
INSERT INTO inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES (
    1, -- ID de Carlos García (según los datos previamente insertados)
    4, -- ID de la clase de Piano Avanzado (según los datos previamente insertados)
    '2024-07-15', -- Fecha de inicio de la inscripción para Carlos García
    '2024-12-15', -- Fecha de fin de la inscripción para Carlos García
    4 -- ID del descuento aplicado (según los datos previamente insertados)
);

-- Inscripción de Ana Martínez en Violín Medio
INSERT INTO inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES (
    2, -- ID de Ana Martínez (según los datos previamente insertados)
    2, -- ID de la clase de Violín Medio (según los datos previamente insertados)
    '2024-07-15', -- Fecha de inicio de la inscripción para Ana Martínez
    '2024-12-15', -- Fecha de fin de la inscripción para Ana Martínez
    4 -- ID del descuento aplicado (según los datos previamente insertados)
);

-- Inscripción de Juan López en Canto
INSERT INTO inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES (
    3, -- ID de Juan López (según los datos previamente insertados)
    1, -- ID de la clase de Canto (según los datos previamente insertados)
    '2024-07-15', -- Fecha de inicio de la inscripción para Juan López
    '2024-12-15', -- Fecha de fin de la inscripción para Juan López
    4 -- ID del descuento aplicado (según los datos previamente insertados)
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