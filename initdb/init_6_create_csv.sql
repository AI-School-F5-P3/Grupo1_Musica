-- Exportar los datos de la vista a un archivo CSV
COPY (SELECT * FROM armonia.vista_clase_info) TO '/mnt/data/vista_clase_info.csv' WITH (FORMAT CSV, HEADER);

COPY (SELECT * FROM armonia.vista_alumnos_por_clase) TO '/mnt/data/vista_alumnos_por_clase.csv' WITH (FORMAT CSV, HEADER);

COPY (SELECT * FROM armonia.vista_asistencia_alumnos) TO '/mnt/data/vista_asistencia_alumnos.csv' WITH (FORMAT CSV, HEADER);