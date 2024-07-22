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







SELECT armonia.inscribir_alumno(1, 1, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(2, 14, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(3, 8, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(4, 19, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(5, 22, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(6, 5, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(7, 17, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(8, 9, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(9, 21, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(10, 3, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(11, 26, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(12, 1, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(13, 15, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(14, 30, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(15, 28, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(16, 7, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(17, 4, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(18, 6, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(19, 12, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(20, 33, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(1, 16, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(2, 32, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(3, 10, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(4, 24, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(5, 18, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(6, 35, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(7, 13, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(8, 31, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(9, 25, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(10, 29, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(11, 20, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(12, 27, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(13, 23, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(14, 34, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(15, 2, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(16, 36, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(17, 6, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(18, 10, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(19, 14, '2024-09-01', '2024-12-12');
SELECT armonia.inscribir_alumno(20, 3, '2024-09-01', '2024-12-12');

-- SELECT *
-- FROM armonia.inscripcion AS inscripcion
-- JOIN armonia.vista_clase_info AS vista ON vista.clase_id = inscripcion.clase_id
-- WHERE inscripcion.alumno_id = 1;

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