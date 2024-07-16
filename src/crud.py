from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from sqlalchemy import and_
import datetime
from fastapi import HTTPException
import models
import schemas

# Crear alumnos / alumno nuevo

async def crear_alumno(
    db: AsyncSession,
    alumno: schemas.Crear_Alumno,
    nombre_instrumento: str,
    nombre_profesor: str,
    nombre_nivel: str
) -> models.Alumno:

    try:
        # Verificar que exista el instrumento
        query_instrumento = select(models.Instrumento).where(models.Instrumento.instrumento == nombre_instrumento)
        instrumento_result = await db.execute(query_instrumento)
        instrumento = instrumento_result.scalar_one_or_none()

        if not instrumento:
            raise HTTPException(status_code=404, detail="Instrumento no encontrado")

        # Verificar que exista el profesor
        query_profesor = select(models.Profesor).where(models.Profesor.profesor == nombre_profesor)
        profesor_result = await db.execute(query_profesor)
        profesor = profesor_result.scalar_one_or_none()

        if not profesor:
            raise HTTPException(status_code=404, detail="Profesor no encontrado")

        # Verificar que exista el nivel
        query_nivel = select(models.Nivel).where(models.Nivel.nivel == nombre_nivel)
        nivel_result = await db.execute(query_nivel)
        nivel = nivel_result.scalar_one_or_none()

        if not nivel:
            raise HTTPException(status_code=404, detail="Nivel no encontrado")

    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al verificar datos: {str(e)}")

    try:
        # Verificar relaciones en Profesor_Instrumento
        query_profesor_instrumento = select(models.Profesor_Instrumento).where(
            models.Profesor_Instrumento.instrumento_id == instrumento.id,
            models.Profesor_Instrumento.profesor_id == profesor.id
        )
        profesor_instrumento_result = await db.execute(query_profesor_instrumento)
        profesor_instrumento = profesor_instrumento_result.scalar_one_or_none()

        if not profesor_instrumento:
            raise HTTPException(status_code=404, detail="Relación Profesor-Instrumento no encontrada")

        # Verificar relaciones en Instrumento_Nivel
        query_instrumento_nivel = select(models.Instrumento_Nivel).where(
            models.Instrumento_Nivel.instrumento_id == instrumento.id,
            models.Instrumento_Nivel.nivel_id == nivel.id
        )
        instrumento_nivel_result = await db.execute(query_instrumento_nivel)
        instrumento_nivel = instrumento_nivel_result.scalar_one_or_none()

        if not instrumento_nivel:
            raise HTTPException(status_code=404, detail="Relación Instrumento-Nivel no encontrada")

        # Verificar la existencia de la clase
        query_clase = select(models.Clase).where(
            and_(
                models.Clase.instrumento_nivel_id == instrumento_nivel.id,
                models.Clase.profesor_instrumento_id == profesor_instrumento.id
            )
        )
        clase_result = await db.execute(query_clase)
        clase = clase_result.scalar_one_or_none()

        if not clase:
            raise HTTPException(status_code=404, detail="Clase no encontrada")

    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al verificar relaciones y clase: {str(e)}")

    try:
        nuevo_alumno = models.Alumno(
            nombre=alumno.nombre,
            apellido=alumno.apellido,
            edad=alumno.edad,
            telefono=alumno.telefono,
            correo=alumno.correo,
            familiar=alumno.familiar,
            total_mes=alumno.total_mes
        )

        db.add(nuevo_alumno)
        await db.flush()  # Esto asegura que nuevo_alumno obtenga un ID antes de usarlo en la inscripción

        # Obtener el ID del descuento "Sin descuento"
        query_descuento = select(models.Descuento).where(models.Descuento.descripcion == 'Sin descuento')
        descuento_result = await db.execute(query_descuento)
        descuento = descuento_result.scalar_one_or_none()

        if not descuento:
            raise HTTPException(status_code=500, detail="No se encontró el descuento 'Sin descuento' en la base de datos")

        alumno_inscripcion = models.Inscripcion(
            alumno_id=nuevo_alumno.id,
            clase_id=clase.id,
            fecha_inicio=datetime.date.today(),
            fecha_fin=None,
            descuento_id=descuento.id  # Asignar el ID del descuento "Sin descuento"
        )

        db.add(alumno_inscripcion)
        await db.commit()
        await db.refresh(nuevo_alumno)

    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"No se pudo crear alumno nuevo: {str(e)}")

    return nuevo_alumno

# Crear alumno / alumno existente

# Actualizar datos de alumno
async def actualizar_alumno(
    db: AsyncSession,
    nombre: str,
    apellidos: str, 
    alumno: schemas.ActualizarAlumno
) -> models.Alumno:
    result = await db.execute(
        select(models.Alumno).where(
            models.Alumno.nombre == nombre,
            models.Alumno.apellido == apellidos)
        )
    existing_alumno = result.scalars().first()

    if not existing_alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

    # Actualizar los campos del alumno
    update_data = alumno.model_dump()
    for key, value in update_data.items():
        setattr(existing_alumno, key, value)

    try:
        await db.commit()
        await db.refresh(existing_alumno)
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="No se pudo actualizar el alumno")
    
    return existing_alumno

# Comprobar datos de alumno

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

import models

async def ver_alumno(
    db: AsyncSession,
    alumno_nombre: str,
    alumno_apellidos: str
) -> models.Alumno:
    result = await db.execute(
        select(models.Alumno)
        .options(
            joinedload(models.Alumno.inscripciones)
            .joinedload(models.Inscripcion.clase)
            .joinedload(models.Clase.instrumento_nivel)
            .joinedload(models.Instrumento_Nivel.nivel),
            joinedload(models.Alumno.inscripciones)
            .joinedload(models.Inscripcion.clase)
            .joinedload(models.Clase.profesor_instrumento)
            .joinedload(models.Profesor_Instrumento.profesor)
        )
        .filter(
            models.Alumno.nombre == alumno_nombre,
            models.Alumno.apellido == alumno_apellidos
        )
    )
    alumno = result.scalars().first()

    if not alumno:
        raise HTTPException(status_code=404, detail='Alumno no encontrado')
    
    return alumno
# Borrar alumno

async def borrar_alumno(
    db: AsyncSession,
    alumno_nombre: str,
    alumno_apellidos: str
):
    async with db.begin():
        result = await db.execute(
            select(models.Alumno).filter(
                models.Alumno.nombre == alumno_nombre,
                models.Alumno.apellido == alumno_apellidos)
            )
        alumno = result.scalars().first()
        
        if not alumno:
            raise HTTPException(status_code=404, detail="Alumno no encontrado")
        
        await db.delete(alumno)
        
        try:
            await db.commit()
        except SQLAlchemyError:
            await db.rollback()
            raise HTTPException(status_code=500, detail="No se pudo borrar al alumno")
    
        return alumno


# Crear profesores

async def crear_profesor(
    db: AsyncSession,
    profesor: schemas.ProfesorCreate
) -> models.Profesor:
    nuevo_profesor = models.Profesor(profesor=profesor.profesor)
    db.add(nuevo_profesor)

    try:
        await db.commit()
        await db.refresh(nuevo_profesor)
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="No se pudo crear profesor nuevo")
    
    return nuevo_profesor

# Actualizar profesor

async def update_profesor(
    db: AsyncSession,
    profesor_nombre:str,
    profesor:schemas.ActualizarProfesor
)-> models.Profesor:
    result = await db.execute(
        select(models.Profesor).where(
            models.Profesor.profesor == profesor_nombre)
        )
    existing_profesor = result.scalars().first()

    if not existing_profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")

    # Actualizar los campos del profesor
    update_data = profesor.model_dump()
    for key, value in update_data.items():
        setattr(existing_profesor, key, value)

    try:
        await db.commit()
        await db.refresh(existing_profesor)
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="No se pudo actualizar al profesor")
    
    return existing_profesor
    
# Recuperar profesor por nombre

async def buscar_profesor(
    db: AsyncSession,
    nombre_profesor: str
):
    result = await db.execute(
        select(models.Profesor)
        .options(joinedload(models.Profesor.profesor_instrumentos).joinedload(models.Profesor_Instrumento.instrumento))
        .filter(models.Profesor.profesor == nombre_profesor)
    )
    profesor = result.scalars().first()

    if profesor is None:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    
    # Formatear la respuesta para incluir el nombre del instrumento
    profesor_data = {
        "nombre_profesor": profesor.profesor,
        "instrumentos": [
            {"nombre_instrumento": pi.instrumento.instrumento}
            for pi in profesor.profesor_instrumentos
        ]
    }
    
    return profesor_data

# Borrar un profesor

async def borrar_profesor(
    db: AsyncSession, 
    profesor_id: int
):
    async with db.begin():
        result = await db.execute(select(models.Profesor).filter(models.Profesor.id == profesor_id))
        profesor = result.scalars().first()
        
        if not profesor:
            raise HTTPException(status_code=404, detail="Profesor no encontrado")
        
        await db.delete(profesor)
        
        try:
            await db.commit()
        except SQLAlchemyError:
            await db.rollback()
            raise HTTPException(status_code=500, detail="No se pudo borrar el profesor")
    
    return profesor

# Actualizar precios

async def actualizar_precios(
    db: AsyncSession,
    pack_name: str,
    pack: schemas.ActualizarPrecio
) -> models.Pack: 

    result = await db.execute(select(models.Pack).filter(models.Pack.pack == pack_name))
    pack_existente = result.scalars().first()

    if not pack_existente:
        raise HTTPException(status_code = 404, detail = "Pack no encontrado")
    
    update_data = pack.model_dump()
    for key, value in update_data.items():
        setattr(pack_existente, key, value)

    try:
        await db.commit()
        await db.refresh(pack_existente)
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code=500, detail="No se pudo actualizar el precio")
    return pack_existente
        
# Actualizar descuentos

async def actualizar_descuentos(
    db: AsyncSession,
    descuento_desc: str,
    descuento: schemas.ActualizarDescuento
) -> models.Descuento:
    result = await db.execute(select(models.Descuento).filter(models.Descuento.descripcion == descuento_desc))
    descuento_existente = result.scalars().first()

    if not descuento_existente:
        raise HTTPException(status_code=404, detail = "Tipo de descuento no encontrado")
    
    update_data = descuento.model_dump()
    for key, value in update_data.items():
        setattr(descuento_existente, key, value)

    try:
        await db.commit()
        await db.refresh(descuento_existente)
    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(status_code= 500, detail = "No se pudo actualizar el descuento")
    
    return descuento_existente
        
# Comprobar precios

async def ver_precios(
    db: AsyncSession,
    pack_name: str
) -> models.Pack:
    result = await db.execute(select(models.Pack).filter(models.Pack.pack == pack_name))
    pack_existente = result.scalars().first()

    if not pack_existente:
        raise HTTPException(status_code=404, detail = "Pack no encontrado")
    
    return pack_existente

# Comprobar descuentos

async def ver_descuentos(
    db:AsyncSession,
    descuento_descripcion: str
)-> models.Descuento:
    result = await db.execute(select(models.Descuento).filter(models.Descuento.descripcion == descuento_descripcion))
    descuento_existente = result.scalars().first()

    if not descuento_existente:
        raise HTTPException(status_code=404, detail = "Descripción de descuento no encontrado")
    
    return descuento_existente