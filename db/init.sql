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

-- -----------------------------  Eliminar las tablas si existen  ----------------------------- --

DROP TABLE IF EXISTS armonia.pack CASCADE;
DROP TABLE IF EXISTS armonia.instrumento CASCADE;
DROP TABLE IF EXISTS armonia.nivel CASCADE;
DROP TABLE IF EXISTS armonia.profesor CASCADE;
DROP TABLE IF EXISTS armonia.instrumento_nivel CASCADE;
DROP TABLE IF EXISTS armonia.profesor_instrumento CASCADE;
DROP TABLE IF EXISTS armonia.alumno CASCADE;
DROP TABLE IF EXISTS armonia.clase CASCADE;
DROP TABLE IF EXISTS armonia.descuento CASCADE;
DROP TABLE IF EXISTS armonia.inscripcion CASCADE;

-- -----------------------------  Crear las tablas  ----------------------------- --

-- Crear la tabla pack
CREATE TABLE armonia.pack(
    "id" SERIAL PRIMARY KEY,
    "pack" VARCHAR(100),
    "precio" INTEGER NOT NULL
);

-- Comentarios sobre la tabla pack y sus columnas
COMMENT ON TABLE armonia.pack IS 'Tabla que almacena la información de los paquetes de clases ofrecidos';
COMMENT ON COLUMN armonia.pack."id" IS 'Identificador único del paquete';
COMMENT ON COLUMN armonia.pack."pack" IS 'Nombre del paquete de clases';
COMMENT ON COLUMN armonia.pack."precio" IS 'Precio del paquete de clases';

-- Crear la tabla instrumento
CREATE TABLE armonia.instrumento(
    "id" SERIAL PRIMARY KEY,
    "instrumento" VARCHAR(100) NOT NULL,
    "pack_id" INTEGER NOT NULL,
    CONSTRAINT fk_pack_id FOREIGN KEY (pack_id) REFERENCES armonia.pack("id")
);

-- Comentarios sobre la tabla instrumento y sus columnas
COMMENT ON TABLE armonia.instrumento IS 'Tabla que almacena los instrumentos musicales';
COMMENT ON COLUMN armonia.instrumento."id" IS 'Identificador único del instrumento';
COMMENT ON COLUMN armonia.instrumento."instrumento" IS 'Nombre del instrumento';
COMMENT ON COLUMN armonia.instrumento."pack_id" IS 'Identificador del pack al que pertenece el instrumento, referencia a pack(id)';

-- Crear la tabla nivel
CREATE TABLE armonia.nivel(
    "id" SERIAL PRIMARY KEY,
    "nivel" VARCHAR(100) UNIQUE NOT NULL
);

-- Comentarios sobre la tabla nivel y sus columnas
COMMENT ON TABLE armonia.nivel IS 'Tabla que almacena los niveles de aprendizaje';
COMMENT ON COLUMN armonia.nivel."id" IS 'Identificador único del nivel';
COMMENT ON COLUMN armonia.nivel."nivel" IS 'Nombre del nivel de aprendizaje';

-- Crear la tabla profesor
CREATE TABLE armonia.profesor(
    "id" SERIAL PRIMARY KEY,
    "profesor" VARCHAR(100) UNIQUE NOT NULL
);

-- Comentarios sobre la tabla profesor y sus columnas
COMMENT ON TABLE armonia.profesor IS 'Tabla que almacena la información de los profesores';
COMMENT ON COLUMN armonia.profesor."id" IS 'Identificador único del profesor';
COMMENT ON COLUMN armonia.profesor."profesor" IS 'Nombre del profesor';

-- Crear la tabla instrumento_nivel
CREATE TABLE armonia.instrumento_nivel(
    "id" SERIAL PRIMARY KEY,
    "instrumento_id" INTEGER NOT NULL,
    "nivel_id" INTEGER NOT NULL,
    CONSTRAINT fk_instrumento_id FOREIGN KEY (instrumento_id) REFERENCES armonia.instrumento("id"),
    CONSTRAINT fk_nivel_id FOREIGN KEY (nivel_id) REFERENCES armonia.nivel("id")
);

-- Comentarios sobre la tabla instrumento_nivel y sus columnas
COMMENT ON TABLE armonia.instrumento_nivel IS 'Tabla que almacena la relación entre instrumentos y niveles';
COMMENT ON COLUMN armonia.instrumento_nivel."id" IS 'Identificador único de la relación entre instrumento y nivel';
COMMENT ON COLUMN armonia.instrumento_nivel."instrumento_id" IS 'Identificador del instrumento';
COMMENT ON COLUMN armonia.instrumento_nivel."nivel_id" IS 'Identificador del nivel';

-- Crear la tabla profesor_instrumento
CREATE TABLE armonia.profesor_instrumento(
    "id" SERIAL PRIMARY KEY,
    "profesor_id" INTEGER NOT NULL,
    "instrumento_id" INTEGER NOT NULL,
    CONSTRAINT fk_profesor_id FOREIGN KEY (profesor_id) REFERENCES armonia.profesor("id"),
    CONSTRAINT fk_instrumento_id_pi FOREIGN KEY (instrumento_id) REFERENCES armonia.instrumento("id")
);

-- Comentarios sobre la tabla profesor_instrumento y sus columnas
COMMENT ON TABLE armonia.profesor_instrumento IS 'Tabla que almacena la relación entre profesores e instrumentos';
COMMENT ON COLUMN armonia.profesor_instrumento."id" IS 'Identificador único de la relación entre profesor e instrumento';
COMMENT ON COLUMN armonia.profesor_instrumento."profesor_id" IS 'Identificador del profesor';
COMMENT ON COLUMN armonia.profesor_instrumento."instrumento_id" IS 'Identificador del instrumento';

-- Crear la tabla alumno
CREATE TABLE armonia.alumno (
    "id" SERIAL PRIMARY KEY,
    "nombre" VARCHAR(100) NOT NULL,
    "apellido" VARCHAR(100) NOT NULL,
    "edad" INTEGER,
    "telefono" VARCHAR(20) NOT NULL,
    "correo" VARCHAR(100) NOT NULL UNIQUE,
    "familiar" BOOLEAN,
    "total_mes" INTEGER
);

-- Comentarios sobre la tabla alumno y sus columnas
COMMENT ON TABLE armonia.alumno IS 'Tabla que almacena la información de los alumnos';
COMMENT ON COLUMN armonia.alumno."id" IS 'Identificador único del alumno';
COMMENT ON COLUMN armonia.alumno."nombre" IS 'Nombre del alumno';
COMMENT ON COLUMN armonia.alumno."apellido" IS 'Apellido del alumno';
COMMENT ON COLUMN armonia.alumno."edad" IS 'Edad del alumno';
COMMENT ON COLUMN armonia.alumno."telefono" IS 'Número de teléfono del alumno';
COMMENT ON COLUMN armonia.alumno."correo" IS 'Correo electrónico del alumno';
COMMENT ON COLUMN armonia.alumno."familiar" IS 'Si tiene un familiar en el centro';
COMMENT ON COLUMN armonia.alumno."total_mes" IS 'Descuento total';

-- Crear la tabla clase
CREATE TABLE armonia.clase(
    "id" SERIAL PRIMARY KEY,
    "instrumento_nivel_id" INTEGER NOT NULL,
    "profesor_instrumento_id" INTEGER NOT NULL,
    CONSTRAINT fk_instrumento_nivel_id FOREIGN KEY (instrumento_nivel_id) REFERENCES armonia.instrumento_nivel("id"),
    CONSTRAINT fk_profesor_instrumento_id_cl FOREIGN KEY (profesor_instrumento_id) REFERENCES armonia.profesor_instrumento("id")
);

-- Comentarios sobre la tabla clase y sus columnas
COMMENT ON TABLE armonia.clase IS 'Tabla que almacena la asignación de clases por alumno';
COMMENT ON COLUMN armonia.clase."id" IS 'Identificador único de la asignación de clase por alumno';
COMMENT ON COLUMN armonia.clase."instrumento_nivel_id" IS 'Identificador del nivel de instrumento asignado al alumno, referencia a instrumento_nivel(id)';
COMMENT ON COLUMN armonia.clase."profesor_instrumento_id" IS 'Identificador del profesor de instrumento asignado al alumno, referencia a profesor_instrumento(id)';

-- Crear la tabla descuento
CREATE TABLE armonia.descuento(
    "id" SERIAL PRIMARY KEY,
    "descripcion" VARCHAR(100),
    "porcentaje" INTEGER NOT NULL
);

-- Comentarios sobre la tabla descuento y sus columnas
COMMENT ON TABLE armonia.descuento IS 'Tabla que define los descuentos aplicables';
COMMENT ON COLUMN armonia.descuento."id" IS 'Identificador único del descuento';
COMMENT ON COLUMN armonia.descuento."descripcion" IS 'Descripción del descuento';
COMMENT ON COLUMN armonia.descuento."porcentaje" IS 'Porcentaje de descuento aplicable';

-- Crear la tabla inscripcion con restricciones de fecha
CREATE TABLE armonia.inscripcion(
    "id" SERIAL PRIMARY KEY,
    "alumno_id" INTEGER NOT NULL,
    "clase_id" INTEGER NOT NULL,
    "fecha_inicio" DATE NOT NULL CHECK (fecha_inicio >= CURRENT_DATE),
    "fecha_fin" DATE CHECK (fecha_fin >= CURRENT_DATE + INTERVAL '15 days'),
    "descuento_id" INTEGER NOT NULL,
    CONSTRAINT fk_alumno_id FOREIGN KEY (alumno_id) REFERENCES armonia.alumno("id"),
    CONSTRAINT fk_clase_id FOREIGN KEY (clase_id) REFERENCES armonia.clase("id"),
    CONSTRAINT fk_descuento_id FOREIGN KEY (descuento_id) REFERENCES armonia.descuento("id"),
    CONSTRAINT chk_no_descuento_1 CHECK (descuento_id <> 1)
);

-- Comentarios sobre la tabla inscripcion y sus columnas
COMMENT ON TABLE armonia.inscripcion IS 'Tabla que registra las inscripciones de los alumnos a las clases, incluyendo fechas, descuentos y precios finales.';
COMMENT ON COLUMN armonia.inscripcion."id" IS 'Identificador único para cada inscripción.';
COMMENT ON COLUMN armonia.inscripcion."alumno_id" IS 'Referencia al alumno inscrito, corresponde al ID en la tabla alumno.';
COMMENT ON COLUMN armonia.inscripcion."clase_id" IS 'Referencia a la clase inscrita, corresponde al ID en la tabla clase.';
COMMENT ON COLUMN armonia.inscripcion."fecha_inicio" IS 'Fecha de inicio de la inscripción. No puede ser anterior a la fecha actual.';
COMMENT ON COLUMN armonia.inscripcion."fecha_fin" IS 'Fecha de fin de la inscripción. No puede ser anterior a la fecha actual.';
COMMENT ON COLUMN armonia.inscripcion."descuento_id" IS 'Descuento aplicado a la inscripción.';

-- -----------------------------  Insertar datos en las tablas  ----------------------------- --

-- Insertar datos en la tabla pack
INSERT INTO armonia.pack (pack, precio)
VALUES 
('Canto, Percusión', 40),
('Piano, Guitarra, Batería y Flauta', 35),
('Violín y Bajo', 40),
('Clarinete y Saxofón', 40);

-- SELECT * FROM armonia.pack;

-- Insertar datos en la tabla instrumento
INSERT INTO armonia.instrumento (instrumento, pack_id)
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

-- SELECT * FROM armonia.instrumento;

-- Insertar datos en la tabla nivel
INSERT INTO armonia.nivel (nivel)
VALUES 
('Cero'), ('Iniciación'), ('Medio'), ('Avanzado');

-- SELECT * FROM armonia.nivel;

INSERT INTO armonia.profesor (profesor)
VALUES 
('Mar'), ('Flor'), ('Álvaro'), ('Marifé'), ('Nayara'), ('Nieves'), ('Sofía');

-- SELECT * FROM armonia.profesor;


-- Insertar Relaciones entre Profesores e Instrumentos
-- Relaciones para Piano
INSERT INTO armonia.profesor_instrumento (profesor_id, instrumento_id) VALUES
(1, 1), -- Mar
(2, 1), -- Flor
(3, 1), -- Álvaro
(4, 1), -- Marifé
(5, 1); -- Nayara

-- SELECT * FROM armonia.profesor_instrumento;

-- Relaciones para Guitarra
INSERT INTO armonia.profesor_instrumento (profesor_id, instrumento_id) VALUES
(1, 2), -- Mar
(2, 2); -- Flor

-- Relaciones para Batería
INSERT INTO armonia.profesor_instrumento (profesor_id, instrumento_id) VALUES
(1, 3); -- Mar

-- Relaciones para Violín
INSERT INTO armonia.profesor_instrumento (profesor_id, instrumento_id) VALUES
(5, 4); -- Nayara

-- Relaciones para Canto
INSERT INTO armonia.profesor_instrumento (profesor_id, instrumento_id) VALUES
(4, 5); -- Marifé

-- Relaciones para Flauta
INSERT INTO armonia.profesor_instrumento (profesor_id, instrumento_id) VALUES
(1, 6); -- Mar

-- Relaciones para Saxofón
INSERT INTO armonia.profesor_instrumento (profesor_id, instrumento_id) VALUES
(6, 7); -- Nieves

-- Relaciones para Clarinete
INSERT INTO armonia.profesor_instrumento (profesor_id, instrumento_id) VALUES
(6, 8); -- Nieves

-- Relaciones para Percusión
INSERT INTO armonia.profesor_instrumento (profesor_id, instrumento_id) VALUES
(7, 9); -- Sofía

-- Relaciones para Bajo
INSERT INTO armonia.profesor_instrumento (profesor_id, instrumento_id) VALUES
(5, 10); -- Nayara

-- SELECT * FROM armonia.profesor_instrumento;


-- Insertar datos en la tabla instrumento_nivel
INSERT INTO armonia.instrumento_nivel (instrumento_id, nivel_id)
SELECT i.id, n.id
FROM armonia.instrumento i
CROSS JOIN armonia.nivel n
WHERE 
    (i.instrumento = 'Piano' AND n.nivel IN ('Cero', 'Iniciación', 'Medio', 'Avanzado')) OR
    (i.instrumento = 'Guitarra' AND n.nivel IN ('Iniciación', 'Medio')) OR
    (i.instrumento = 'Batería' AND n.nivel IN ('Iniciación', 'Medio', 'Avanzado')) OR
    (i.instrumento = 'Flauta' AND n.nivel IN ('Iniciación', 'Medio')) OR
    (i.instrumento = 'Bajo' AND n.nivel IN ('Iniciación', 'Medio')) OR
    (i.instrumento NOT IN ('Piano', 'Guitarra', 'Batería', 'Flauta', 'Bajo') AND n.nivel = 'Iniciación');

-- SELECT * FROM armonia.instrumento_nivel;

-- Insertar datos en la tabla clase
INSERT INTO armonia.clase (instrumento_nivel_id, profesor_instrumento_id)
SELECT armonia.instrumento_nivel.id, profesor_instrumento.id
FROM armonia.instrumento_nivel
JOIN armonia.profesor_instrumento ON armonia.instrumento_nivel.instrumento_id = armonia.profesor_instrumento.instrumento_id;

-- SELECT * FROM armonia.clase;

-- Insertar descuentos

INSERT INTO armonia.descuento (descripcion, porcentaje) VALUES
('Familiar en la escuela', 10),
('Segundo curso del mismo instrumento', 50),
('Tercer curso del mismo instrumento', 25),
('Sin descuento', 0);

-- SELECT * FROM armonia.descuento;

--- Insertar datos en la tabla alumno
INSERT INTO armonia.alumno (nombre, apellido, edad, telefono, correo, familiar,total_mes)
VALUES
('Carlos', 'García', 25, '123456789', 'carlos@email.com', true, 0),
('Ana', 'Martínez', 30, '987654321', 'ana@email.com', false, 0),
('Juan', 'López', 20, '567890123', 'juan@email.com', false, 0),
('Marta', 'Fernández', 28, '111222333', 'marta@email.com', true, 0),
('Pedro', 'González', 22, '444555666', 'pedro@email.com', false, 0),
('Laura', 'Díaz', 26, '777888999', 'laura@email.com', true, 0),
('Luis', 'Torres', 24, '123123123', 'luis@email.com', false, 0),
('Sofía', 'Cruz', 29, '321321321', 'sofia@email.com', true, 0),
('Javier', 'Ramírez', 23, '456456456', 'javier@email.com', false, 0),
('Clara', 'Pérez', 21, '654654654', 'clara@email.com', true, 0),
('Mario', 'Vargas', 27, '789789789', 'mario@email.com', false, 0),
('Natalia', 'Mendoza', 31, '234234234', 'natalia@email.com', true, 0),
('Diego', 'Reyes', 32, '567567567', 'diego@email.com', false, 0),
('Isabel', 'Sánchez', 19, '890890890', 'isabel@email.com', true, 0),
('Fernando', 'Cámara', 33, '123456780', 'fernando@email.com', false, 0),
('Beatriz', 'Salazar', 30, '987654320', 'beatriz@email.com', true, 0),
('Victor', 'Morales', 26, '567890124', 'victor@email.com', false, 0),
('Gabriela', 'Jiménez', 27, '444555667', 'gabriela@email.com', true, 0),
('Hugo', 'Ortega', 25, '111222334', 'hugo@email.com', false, 0),
('Valeria', 'Cordero', 22, '333444555', 'valeria@email.com', true, 0)
ON CONFLICT (correo) DO NOTHING;

-- SELECT * FROM armonia.alumno;


-- Inscripción de los alumnos en las clases específicas

-- Inscribir alumnos en clases

-- Inscripciones para Piano (clase_id 1)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 1, '2024-09-15', '2024-12-15', 4),
(2, 1, '2024-09-15', '2024-12-15', 4),
(3, 1, '2024-09-15', '2024-12-15', 4),
(4, 1, '2024-09-15', '2024-12-15', 4),
(5, 1, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para Guitarra (clase_id 2)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 2, '2024-09-15', '2024-12-15', 4),
(7, 2, '2024-09-15', '2024-12-15', 4),
(8, 2, '2024-09-15', '2024-12-15', 4),
(9, 2, '2024-09-15', '2024-12-15', 4),
(10, 2, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para Batería (clase_id 3)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(11, 3, '2024-09-15', '2024-12-15', 4),
(12, 3, '2024-09-15', '2024-12-15', 4),
(13, 3, '2024-09-15', '2024-12-15', 4),
(14, 3, '2024-09-15', '2024-12-15', 4),
(15, 3, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para Violín (clase_id 4)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(16, 4, '2024-09-15', '2024-12-15', 4),
(17, 4, '2024-09-15', '2024-12-15', 4),
(18, 4, '2024-09-15', '2024-12-15', 4),
(19, 4, '2024-09-15', '2024-12-15', 4),
(20, 4, '2024-09-15', '2024-12-15', 4);

-- Clase vacía (clase_id 5)

-- Inscripciones para Canto (clase_id 6)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 6, '2024-09-15', '2024-12-15', 4),
(2, 6, '2024-09-15', '2024-12-15', 4),
(3, 6, '2024-09-15', '2024-12-15', 4),
(4, 6, '2024-09-15', '2024-12-15', 4),
(5, 6, '2024-09-15', '2024-12-15', 4);

-- Clase vacía (clase_id 7)

-- Clase vacía (clase_id 8)

-- Inscripciones para Flauta (clase_id 9)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 9, '2024-09-15', '2024-12-15', 4),
(7, 9, '2024-09-15', '2024-12-15', 4),
(8, 9, '2024-09-15', '2024-12-15', 4),
(9, 9, '2024-09-15', '2024-12-15', 4),
(10, 9, '2024-09-15', '2024-12-15', 4);

-- Clase vacía (clase_id 10)

-- Inscripciones para Saxofón (clase_id 11)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 11, '2024-09-15', '2024-12-15', 4),
(2, 11, '2024-09-15', '2024-12-15', 4),
(3, 11, '2024-09-15', '2024-12-15', 4),
(4, 11, '2024-09-15', '2024-12-15', 4),
(5, 11, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para Clarinete (clase_id 12)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 12, '2024-09-15', '2024-12-15', 4),
(7, 12, '2024-09-15', '2024-12-15', 4),
(8, 12, '2024-09-15', '2024-12-15', 4),
(9, 12, '2024-09-15', '2024-12-15', 4),
(10, 12, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para Bajo (clase_id 13)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 13, '2024-09-15', '2024-12-15', 4),
(2, 13, '2024-09-15', '2024-12-15', 4),
(3, 13, '2024-09-15', '2024-12-15', 4),
(4, 13, '2024-09-15', '2024-12-15', 4),
(5, 13, '2024-09-15', '2024-12-15', 4);

-- Clase vacía (clase_id 14)

-- Inscripciones para Percusión (clase_id 15)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 15, '2024-09-15', '2024-12-15', 4),
(7, 15, '2024-09-15', '2024-12-15', 4),
(8, 15, '2024-09-15', '2024-12-15', 4),
(9, 15, '2024-09-15', '2024-12-15', 4),
(10, 15, '2024-09-15', '2024-12-15', 4);

-- Clase vacía (clase_id 16)

-- Inscripciones para otro instrumento (clase_id 17)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 17, '2024-09-15', '2024-12-15', 4),
(2, 17, '2024-09-15', '2024-12-15', 4),
(3, 17, '2024-09-15', '2024-12-15', 4),
(4, 17, '2024-09-15', '2024-12-15', 4),
(5, 17, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 18)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 18, '2024-09-15', '2024-12-15', 4),
(7, 18, '2024-09-15', '2024-12-15', 4),
(8, 18, '2024-09-15', '2024-12-15', 4),
(9, 18, '2024-09-15', '2024-12-15', 4),
(10, 18, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 19)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 19, '2024-09-15', '2024-12-15', 4),
(2, 19, '2024-09-15', '2024-12-15', 4),
(3, 19, '2024-09-15', '2024-12-15', 4),
(4, 19, '2024-09-15', '2024-12-15', 4),
(5, 19, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 20)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 20, '2024-09-15', '2024-12-15', 4),
(7, 20, '2024-09-15', '2024-12-15', 4),
(8, 20, '2024-09-15', '2024-12-15', 4),
(9, 20, '2024-09-15', '2024-12-15', 4),
(10, 20, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 21)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 21, '2024-09-15', '2024-12-15', 4),
(2, 21, '2024-09-15', '2024-12-15', 4),
(3, 21, '2024-09-15', '2024-12-15', 4),
(4, 21, '2024-09-15', '2024-12-15', 4),
(5, 21, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 22)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 22, '2024-09-15', '2024-12-15', 4),
(7, 22, '2024-09-15', '2024-12-15', 4),
(8, 22, '2024-09-15', '2024-12-15', 4),
(9, 22, '2024-09-15', '2024-12-15', 4),
(10, 22, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 23)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 23, '2024-09-15', '2024-12-15', 4),
(2, 23, '2024-09-15', '2024-12-15', 4),
(3, 23, '2024-09-15', '2024-12-15', 4),
(4, 23, '2024-09-15', '2024-12-15', 4),
(5, 23, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 24)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 24, '2024-09-15', '2024-12-15', 4),
(7, 24, '2024-09-15', '2024-12-15', 4),
(8, 24, '2024-09-15', '2024-12-15', 4),
(9, 24, '2024-09-15', '2024-12-15', 4),
(10, 24, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 25)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 25, '2024-09-15', '2024-12-15', 4),
(2, 25, '2024-09-15', '2024-12-15', 4),
(3, 25, '2024-09-15', '2024-12-15', 4),
(4, 25, '2024-09-15', '2024-12-15', 4),
(5, 25, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 26)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 26, '2024-09-15', '2024-12-15', 4),
(7, 26, '2024-09-15', '2024-12-15', 4),
(8, 26, '2024-09-15', '2024-12-15', 4),
(9, 26, '2024-09-15', '2024-12-15', 4),
(10, 26, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 27)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 27, '2024-09-15', '2024-12-15', 4),
(2, 27, '2024-09-15', '2024-12-15', 4),
(3, 27, '2024-09-15', '2024-12-15', 4),
(4, 27, '2024-09-15', '2024-12-15', 4),
(5, 27, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 28)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 28, '2024-09-15', '2024-12-15', 4),
(7, 28, '2024-09-15', '2024-12-15', 4),
(8, 28, '2024-09-15', '2024-12-15', 4),
(9, 28, '2024-09-15', '2024-12-15', 4),
(10, 28, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 29)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 29, '2024-09-15', '2024-12-15', 4),
(2, 29, '2024-09-15', '2024-12-15', 4),
(3, 29, '2024-09-15', '2024-12-15', 4),
(4, 29, '2024-09-15', '2024-12-15', 4),
(5, 29, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 30)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 30, '2024-09-15', '2024-12-15', 4),
(7, 30, '2024-09-15', '2024-12-15', 4),
(8, 30, '2024-09-15', '2024-12-15', 4),
(9, 30, '2024-09-15', '2024-12-15', 4),
(10, 30, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 31)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 31, '2024-09-15', '2024-12-15', 4),
(2, 31, '2024-09-15', '2024-12-15', 4),
(3, 31, '2024-09-15', '2024-12-15', 4),
(4, 31, '2024-09-15', '2024-12-15', 4),
(5, 31, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 32)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 32, '2024-09-15', '2024-12-15', 4),
(7, 32, '2024-09-15', '2024-12-15', 4),
(8, 32, '2024-09-15', '2024-12-15', 4),
(9, 32, '2024-09-15', '2024-12-15', 4),
(10, 32, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 33)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 33, '2024-09-15', '2024-12-15', 4),
(2, 33, '2024-09-15', '2024-12-15', 4),
(3, 33, '2024-09-15', '2024-12-15', 4),
(4, 33, '2024-09-15', '2024-12-15', 4),
(5, 33, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 34)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 34, '2024-09-15', '2024-12-15', 4),
(7, 34, '2024-09-15', '2024-12-15', 4),
(8, 34, '2024-09-15', '2024-12-15', 4),
(9, 34, '2024-09-15', '2024-12-15', 4),
(10, 34, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 35)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(1, 35, '2024-09-15', '2024-12-15', 4),
(2, 35, '2024-09-15', '2024-12-15', 4),
(3, 35, '2024-09-15', '2024-12-15', 4),
(4, 35, '2024-09-15', '2024-12-15', 4),
(5, 35, '2024-09-15', '2024-12-15', 4);

-- Inscripciones para otro instrumento (clase_id 36)
INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
VALUES
(6, 36, '2024-09-15', '2024-12-15', 4),
(7, 36, '2024-09-15', '2024-12-15', 4),
(8, 36, '2024-09-15', '2024-12-15', 4),
(9, 36, '2024-09-15', '2024-12-15', 4),
(10, 36, '2024-09-15', '2024-12-15', 4);

SELECT * FROM armonia.inscripcion;

-- ----------------------------- Comprobar que se hayan insertado los datos correctamente ----------------------------- --
SELECT * FROM armonia.pack;
SELECT * FROM armonia.instrumento;
SELECT * FROM armonia.nivel;
SELECT * FROM armonia.profesor;
SELECT * FROM armonia.instrumento_nivel;
SELECT * FROM armonia.profesor_instrumento;
SELECT * FROM armonia.alumno;
SELECT * FROM armonia.clase;
SELECT * FROM armonia.descuento;
SELECT * FROM armonia.inscripcion;

-- -----------------------------  Crear la vista vista_alumnos_por_clase ----------------------------- --
CREATE OR REPLACE VIEW armonia.vista_alumnos_por_clase AS
SELECT 
    CONCAT(i.instrumento, ' - ', n.nivel) AS clase,
    p.profesor,
    COUNT(ins.alumno_id) AS cantidad_alumnos,
    STRING_AGG(a.nombre, ', ') AS nombres_alumnos
FROM armonia.clase c
JOIN armonia.instrumento_nivel inl ON c.instrumento_nivel_id = inl.id
JOIN armonia.instrumento i ON inl.instrumento_id = i.id
JOIN armonia.nivel n ON inl.nivel_id = n.id
JOIN armonia.profesor_instrumento pi ON c.profesor_instrumento_id = pi.id
JOIN armonia.profesor p ON pi.profesor_id = p.id
LEFT JOIN armonia.inscripcion ins ON c.id = ins.clase_id
LEFT JOIN armonia.alumno a ON ins.alumno_id = a.id
GROUP BY i.instrumento, n.nivel, p.profesor;

-- Exportar los datos de la vista a un archivo CSV
COPY (SELECT * FROM armonia.vista_alumnos_por_clase) TO '/mnt/data/vista_alumnos_por_clase.csv' WITH (FORMAT CSV, HEADER);

-- Seleccionar todos los datos de la vista vista_alumnos_por_clase
SELECT * FROM armonia.vista_alumnos_por_clase;

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