-- ----------------------------------------- funciones para la inscripcion de alumnos ------------------------------------------ --

-- --------------------- Obtener la cantidad de clases del mismo pack a las que ya esta inscrito un alumno --------------------- --

CREATE OR REPLACE FUNCTION armonia.obtener_cantidad_clases_pack(p_alumno_id INT, p_pack_id INT) -- Agrega el nuevo parámetro
RETURNS INT AS $$

DECLARE
    cantidad_clases INT; -- Declara una variable para almacenar el resultado
BEGIN
    -- Realiza la consulta para contar las clases del pack especificado para el alumno
    SELECT 
        COUNT(CASE WHEN pk.id = p_pack_id THEN c.id END) AS cantidad_clases_pack -- Cuenta las clases del pack especificado
    INTO cantidad_clases -- Almacena el resultado en la variable
    FROM armonia.alumno a -- Selecciona de la tabla de alumnos
    LEFT JOIN armonia.inscripcion ins ON a.id = ins.alumno_id -- Une con la tabla de inscripciones
    LEFT JOIN armonia.clase c ON ins.clase_id = c.id -- Une con la tabla de clases
    LEFT JOIN armonia.instrumento_nivel inl ON c.instrumento_nivel_id = inl.id -- Une con los niveles de instrumentos
    LEFT JOIN armonia.instrumento i ON inl.instrumento_id = i.id -- Une con la tabla de instrumentos
    LEFT JOIN armonia.nivel n ON inl.nivel_id = n.id -- Une con la tabla de niveles
    LEFT JOIN armonia.profesor_instrumento pi ON c.profesor_instrumento_id = pi.id -- Une con la tabla de profesores
    LEFT JOIN armonia.profesor p ON pi.profesor_id = p.id -- Une con la tabla de profesores
    LEFT JOIN armonia.pack pk ON i.pack_id = pk.id -- Une con la tabla de packs de instrumentos
    WHERE a.id = p_alumno_id -- Filtra por el ID del alumno proporcionado
    GROUP BY a.id; -- Agrupa por el ID del alumno para la agregación
    
    RETURN cantidad_clases; -- Devuelve la cantidad de clases del pack especificado
END; $$ LANGUAGE plpgsql;

-- --------------------------- funcion para modificar total_mes de alumnos -------------------------- --

CREATE OR REPLACE FUNCTION armonia.modificar_total_mes(p_alumno_id INT)
RETURNS VOID AS $$
DECLARE
    v_total_con_descuento NUMERIC;
BEGIN
    -- Calcular el total con descuento para el alumno
    SELECT 
        COALESCE(SUM(p.precio * (1 - d.porcentaje::float / 100)), 0)
    INTO 
        v_total_con_descuento
    FROM 
        armonia.inscripcion i
    JOIN 
        armonia.clase c ON i.clase_id = c.id
    JOIN 
        armonia.vista_clase_info vci ON c.id = vci.clase_id
    JOIN 
        armonia.pack p ON vci.pack_id = p.id
    JOIN 
        armonia.descuento d ON i.descuento_id = d.id
    WHERE 
        i.alumno_id = p_alumno_id;

    -- Actualizar la columna total_mes en la tabla alumno
    UPDATE armonia.alumno
    SET total_mes = v_total_con_descuento
    WHERE id = p_alumno_id;

    -- Registrar un mensaje (opcional, para depuración)
    RAISE NOTICE 'Total actualizado para el alumno %: %', p_alumno_id, v_total_con_descuento;
END;
$$ LANGUAGE plpgsql;


-- Ejecutar para actualizar todos los registros

-- DO $$
-- DECLARE
--     alumno_record RECORD;
-- BEGIN
--     FOR alumno_record IN SELECT id FROM armonia.alumno
--     LOOP
--         PERFORM armonia.modificar_total_mes(alumno_record.id);
--     END LOOP;
-- END $$;

-- SELECT * FROM armonia.alumno


-- --------------------------- funcion para inscribir alumnos -------------------------- --

CREATE OR REPLACE FUNCTION armonia.inscribir_alumno(
    p_alumno_id INT,
    p_clase_id INT,
    p_fecha_inicio DATE,
    p_fecha_fin DATE
) 
RETURNS VOID AS $$
DECLARE
    pack_id INT; -- Variable para almacenar el ID del pack
    cantidad_clases INT; -- Variable para contar clases del pack
    descuento_id INT; -- Variable para el ID del descuento
BEGIN
    -- Obtener el ID del pack al que pertenece la clase
    SELECT i.pack_id INTO pack_id
    FROM armonia.instrumento_nivel inl
    JOIN armonia.clase c ON inl.id = c.instrumento_nivel_id
    JOIN armonia.instrumento i ON inl.instrumento_id = i.id
    WHERE c.id = p_clase_id;

    -- Verificar cuántas clases del pack tiene el alumno
    cantidad_clases := armonia.obtener_cantidad_clases_pack(p_alumno_id, pack_id);

    -- Definir el descuento según la cantidad de clases
    IF cantidad_clases >= 2 THEN
        descuento_id := 3; -- Descuento por dos o más clases
    ELSIF cantidad_clases = 1 THEN
        descuento_id := 2; -- Descuento por una clase
    ELSE
        descuento_id := 4; -- Asignar descuento 0 por defecto 
    END IF;

    -- Insertar la nueva inscripción
    INSERT INTO armonia.inscripcion (alumno_id, clase_id, fecha_inicio, fecha_fin, descuento_id)
    VALUES (p_alumno_id, p_clase_id, p_fecha_inicio, p_fecha_fin, descuento_id);

	PERFORM armonia.modificar_total_mes(p_alumno_id);


END; $$ LANGUAGE plpgsql;