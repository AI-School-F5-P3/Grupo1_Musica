-- Establecer la codificación de caracteres a UTF8
\encoding UTF8

-- Establecer la codificación de cliente a UTF8
SET client_encoding TO 'UTF8';

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
    CONSTRAINT chk_no_descuento_1 CHECK (descuento_id <> 0)
);

-- Comentarios sobre la tabla inscripcion y sus columnas
COMMENT ON TABLE armonia.inscripcion IS 'Tabla que registra las inscripciones de los alumnos a las clases, incluyendo fechas, descuentos y precios finales.';
COMMENT ON COLUMN armonia.inscripcion."id" IS 'Identificador único para cada inscripción.';
COMMENT ON COLUMN armonia.inscripcion."alumno_id" IS 'Referencia al alumno inscrito, corresponde al ID en la tabla alumno.';
COMMENT ON COLUMN armonia.inscripcion."clase_id" IS 'Referencia a la clase inscrita, corresponde al ID en la tabla clase.';
COMMENT ON COLUMN armonia.inscripcion."fecha_inicio" IS 'Fecha de inicio de la inscripción. No puede ser anterior a la fecha actual.';
COMMENT ON COLUMN armonia.inscripcion."fecha_fin" IS 'Fecha de fin de la inscripción. No puede ser anterior a la fecha actual.';
COMMENT ON COLUMN armonia.inscripcion."descuento_id" IS 'Descuento aplicado a la inscripción.';