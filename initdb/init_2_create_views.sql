-- -----------------------------  Crear la vista vista_clase_info ----------------------------- --

CREATE VIEW armonia.vista_clase_info AS
SELECT 
    c.id AS clase_id, 
    CONCAT(i.instrumento, ' - ', n.nivel) AS instrumento_nivel,
    i.pack_id,
    p.pack AS nombre_pack,
    p.precio AS precio_clase    
FROM 
    armonia.clase c
JOIN 
    armonia.instrumento_nivel in_nivel ON c.instrumento_nivel_id = in_nivel.id
JOIN 
    armonia.instrumento i ON in_nivel.instrumento_id = i.id
JOIN 
    armonia.nivel n ON in_nivel.nivel_id = n.id
JOIN 
    armonia.pack p ON i.pack_id = p.id;

-- -- Exportar los datos de la vista a un archivo CSV
-- COPY (SELECT * FROM armonia.vista_clase_info) TO '/mnt/data/vista_clase_info.csv' WITH (FORMAT CSV, HEADER);

SELECT * FROM armonia.vista_clase_info;

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

-- -- Exportar los datos de la vista a un archivo CSV
-- COPY (SELECT * FROM armonia.vista_alumnos_por_clase) TO '/mnt/data/vista_alumnos_por_clase.csv' WITH (FORMAT CSV, HEADER);

-- Seleccionar todos los datos de la vista vista_alumnos_por_clase
SELECT * FROM armonia.vista_alumnos_por_clase;


-- -----------------------------  Crear la vista vista_asistencia_alumnos ----------------------------- --

DROP VIEW IF EXISTS armonia.vista_asistencia_alumnos;
CREATE OR REPLACE VIEW armonia.vista_asistencia_alumnos AS
SELECT 
    CONCAT(a.nombre,' ', a.apellido) AS alumno,
    COUNT(CASE WHEN pk.id = 1 THEN c.id END) AS cantidad_clases_sin_pack,
    COUNT(CASE WHEN pk.id = 2 THEN c.id END) AS cantidad_clases_pack_A,
    COUNT(CASE WHEN pk.id = 3 THEN c.id END) AS cantidad_clases_pack_B,
    COUNT(CASE WHEN pk.id = 4 THEN c.id END) AS cantidad_clases_pack_C,
    COUNT(c.id) AS total_clases
FROM armonia.alumno a
LEFT JOIN armonia.inscripcion ins ON a.id = ins.alumno_id
LEFT JOIN armonia.clase c ON ins.clase_id = c.id
LEFT JOIN armonia.instrumento_nivel inl ON c.instrumento_nivel_id = inl.id
LEFT JOIN armonia.instrumento i ON inl.instrumento_id = i.id
LEFT JOIN armonia.nivel n ON inl.nivel_id = n.id
LEFT JOIN armonia.profesor_instrumento pi ON c.profesor_instrumento_id = pi.id
LEFT JOIN armonia.profesor p ON pi.profesor_id = p.id
LEFT JOIN armonia.pack pk ON i.pack_id = pk.id -- Asumiendo que el pack está relacionado con el instrumento
-- WHERE a.id = 1
GROUP BY a.id
ORDER BY a.id;

-- -- Exportar los datos de la vista a un archivo CSV
-- COPY (SELECT * FROM armonia.vista_asistencia_alumnos) TO '/mnt/data/vista_asistencia_alumnos.csv' WITH (FORMAT CSV, HEADER);

SELECT * FROM armonia.vista_asistencia_alumnos;
