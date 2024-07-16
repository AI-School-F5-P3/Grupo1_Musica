from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError, NoResultFound, MultipleResultsFound
from sqlalchemy.orm import joinedload
from sqlalchemy import and_
from datetime import date
from fastapi import HTTPException
from logger import logger
import models
import schemas

# Crear nuevo alumno

async def crear_alumno(
    db: AsyncSession,
    alumno: schemas.Crear_Alumno, # Esquema de respuesta esperada
    nombre_instrumento: str,
    nombre_profesor: str,
    nombre_nivel: str
) -> models.Alumno:

    try:
        # Verificar que exista el instrumento en la tabla instrumentos
        query_instrumento = select(models.Instrumento).where(models.Instrumento.instrumento == nombre_instrumento)
        instrumento_result = await db.execute(query_instrumento)
        instrumento = instrumento_result.scalar_one_or_none()

        if not instrumento:
            logger.error("No se encuentra el instrumento en la base de datos")
            raise HTTPException(status_code=404, detail="Instrumento no encontrado")

            

        # Verificar que exista el profesor en la tabla profesor
        query_profesor = select(models.Profesor).where(models.Profesor.profesor == nombre_profesor)
        profesor_result = await db.execute(query_profesor)
        profesor = profesor_result.scalar_one_or_none()

        if not profesor:
            logger.error("No se encuentra el profesor en la base de datos")
            raise HTTPException(status_code=404, detail="Profesor no encontrado")

        # Verificar que exista el nivel en la tabla nivel
        query_nivel = select(models.Nivel).where(models.Nivel.nivel == nombre_nivel)
        nivel_result = await db.execute(query_nivel)
        nivel = nivel_result.scalar_one_or_none()

        if not nivel:
            logger.error("No se encuentra el nivel en la base de datos")
            raise HTTPException(status_code=404, detail="Nivel no encontrado")

    except SQLAlchemyError as e:
        await db.rollback()
        logger.error("Error de sqlalchemy, no se pueden verificar los datos")
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
            logger.error("No se encuentra la relacion entre profesor e instrumento")
            raise HTTPException(status_code=404, detail="Relación Profesor-Instrumento no encontrada")

        # Verificar relaciones en Instrumento_Nivel
        query_instrumento_nivel = select(models.Instrumento_Nivel).where(
            models.Instrumento_Nivel.instrumento_id == instrumento.id,
            models.Instrumento_Nivel.nivel_id == nivel.id
        )
        instrumento_nivel_result = await db.execute(query_instrumento_nivel)
        instrumento_nivel = instrumento_nivel_result.scalar_one_or_none()

        if not instrumento_nivel:
            logger.error("No se encuentra la relacion entre instrumento y nivel")
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
            logger.error("No se encuentra la clase de nivel e instrumento")
            raise HTTPException(status_code=404, detail="Clase no encontrada")

    except SQLAlchemyError as e:
        await db.rollback()
        logger.error("Error en la verificación de relaciones")
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
        logger.info("Se añade un nuevo alumno a la tabla")
        await db.flush()  # Esto asegura que nuevo_alumno obtenga un ID antes de usarlo en la inscripción

        # Obtener el ID del descuento "Sin descuento"
        query_descuento = select(models.Descuento).where(models.Descuento.descripcion == 'Sin descuento')
        descuento_result = await db.execute(query_descuento)
        descuento = descuento_result.scalar_one_or_none()

        if not descuento:
            logger.error("No se encuentra el descuento 4")
            raise HTTPException(status_code=500, detail="No se encontró el descuento 'Sin descuento' en la base de datos")

        alumno_inscripcion = models.Inscripcion(
            alumno_id=nuevo_alumno.id,
            clase_id=clase.id,
            fecha_inicio=date.today(),
            fecha_fin=None,
            descuento_id=descuento.id  # Asignar el ID del descuento "Sin descuento"
        )

        db.add(alumno_inscripcion)
        logger.info("Se añade una nueva inscripción a la tabla")
        await db.commit()
        await db.refresh(nuevo_alumno)

    except SQLAlchemyError as e:
        await db.rollback()
        logger.error("Error al crear un alumno nuevo")
        raise HTTPException(status_code=500, detail=f"No se pudo crear alumno nuevo: {str(e)}")

    return nuevo_alumno

#Crear nueva inscripcion

async def crear_inscripcion(
    db: AsyncSession,
    inscripcion: schemas.Crear_Inscripcion,
    nombre_instrumento:str,
    nombre_profesor:str,
    nombre_nivel:str
)-> models.Inscripcion:
    try:
        # Verificar que exista el instrumento en la tabla
        query_instrumento = select(models.Instrumento).where(models.Instrumento.instrumento == nombre_instrumento)
        instrumento_result = await db.execute(query_instrumento)
        instrumento = instrumento_result.scalars().first()

        if not instrumento:
            logger.error("No se encuentra el instrumento")
            raise HTTPException(status_code=404, detail="Instrumento no encontrado")

        # Verificar que exista el profesor en la tabla
        query_profesor = select(models.Profesor).where(models.Profesor.profesor == nombre_profesor)
        profesor_result = await db.execute(query_profesor)
        profesor = profesor_result.scalars().first()

        if not profesor:
            logger.error("No se encuentra el profesor")
            raise HTTPException(status_code=404, detail="Profesor no encontrado")

        # Verificar que exista el nivel en la tabla
        query_nivel = select(models.Nivel).where(models.Nivel.nivel == nombre_nivel)
        nivel_result = await db.execute(query_nivel)
        nivel = nivel_result.scalars().first()

        if not nivel:
            logger.error("No se encuentra el nivel")
            raise HTTPException(status_code=404, detail="Nivel no encontrado")
    
    except SQLAlchemyError as e:
        await db.rollback()
        logger.error("Error SQLAlchemy no se pueden verificar los datos")
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
            logger.error("No se encuentra la relación entre profesor e instrumento")
            raise HTTPException(status_code=404, detail="Relación Profesor-Instrumento no encontrada")

        # Verificar relaciones en Instrumento_Nivel
        query_instrumento_nivel = select(models.Instrumento_Nivel).where(
            models.Instrumento_Nivel.instrumento_id == instrumento.id,
            models.Instrumento_Nivel.nivel_id == nivel.id
        )
        instrumento_nivel_result = await db.execute(query_instrumento_nivel)
        instrumento_nivel = instrumento_nivel_result.scalar_one_or_none()

        if not instrumento_nivel:
            logger.error("No se encuentra la relación entre instrumento y nivel")
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
            logger.error("No se encuentra la clase en la tabla")
            raise HTTPException(status_code=404, detail="Clase no encontrada")

    except SQLAlchemyError as e:
        await db.rollback()
        logger.error("Error SQLAlchemy no pueden verificarse las relaciones y clase")
        raise HTTPException(status_code=500, detail=f"Error al verificar relaciones y clase: {str(e)}")

    try:
        # Verificar la existencia del alumno
        query_alumno = select(models.Alumno).where(
            and_(
                models.Alumno.nombre == inscripcion.nombre,
                models.Alumno.apellido == inscripcion.apellido
            )
        )
        alumno_result = await db.execute(query_alumno)
        alumno = alumno_result.scalar_one_or_none()

        if not alumno:
            logger.error("No se encuentra el alumno")
            raise HTTPException(status_code=404, detail="Alumno no encontrado")
        
        #Verificar descuento
        query_descuento = select(models.Descuento).where(models.Descuento.descripcion == 'Sin descuento')
        descuento_result = await db.execute(query_descuento)
        descuento = descuento_result.scalar_one_or_none()

        if not descuento:
            logger.error("No se encuentra el descuento 4")
            raise HTTPException(status_code=500, detail="No se encontró el descuento 'Sin descuento' en la base de datos")

    except SQLAlchemyError as e:
        await db.rollback()
        logger.error("Error SQLAlchemy al verificar datos")
        raise HTTPException(status_code=500, detail=f"Error al verificar datos: {str(e)}")
    try:
        alumno_inscripcion = models.Inscripcion(
            alumno_id=alumno.id,
            clase_id=clase.id,
            fecha_inicio=date.today(),
            fecha_fin=None,
            descuento_id=descuento.id  # Asignar el ID del descuento "Sin descuento"
        )

        db.add(alumno_inscripcion)
        logger.info('Se añade una nueva inscripción a la base de datos')
        await db.commit()
        await db.refresh(alumno_inscripcion)

    except SQLAlchemyError as e:
        await db.rollback()
        logger.error("No se pudo crear el alumno nuevo")
        raise HTTPException(status_code=500, detail=f"No se pudo crear alumno nuevo: {str(e)}")

    return {"mensaje":"exito"}


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
        logger.error("Alumno no encontrado")
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

    # Actualizar los campos del alumno
    update_data = alumno.model_dump(exclude_unset = True)
    for key, value in update_data.items():
        setattr(existing_alumno, key, value)

    try:
        await db.commit()
        logger.info(f'Se actualizan los datos del alumno{nombre}, {apellidos}')
        await db.refresh(existing_alumno)
    except SQLAlchemyError:
        await db.rollback()
        logger.error("No se pueden actualizar los datos")
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
        logger.error(f"No se encuentra el alumno {alumno_nombre}")
        raise HTTPException(status_code=404, detail='Alumno no encontrado')
    
    return alumno
# Borrar alumno

async def borrar_alumno(
    db: AsyncSession,
    alumno_nombre: str,
    alumno_apellidos: str
):
    async with db.begin():
        try:
            result = await db.execute(
                select(models.Alumno).filter(
                    models.Alumno.nombre == alumno_nombre,
                    models.Alumno.apellido == alumno_apellidos
                )
            )
            alumno = result.scalar_one()
        except NoResultFound:
            logger.error(f"No se encuentra el alumno {alumno_nombre}")
            raise HTTPException(status_code=404, detail="Alumno no encontrado")
        except MultipleResultsFound:
            logger.error(f"Se encontraron multiples resultados para el alumno {alumno_nombre}")
            raise HTTPException(status_code=500, detail="Se encontraron múltiples resultados para el alumno")
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error("Error en la base de datos")
            raise HTTPException(status_code=500, detail=f"Error de base de datos: {str(e)}")
        
        try:
            await db.delete(alumno)
            logger.info(f'Alumno {alumno_nombre} eliminado correctamente')
            await db.commit()
        except SQLAlchemyError as e:
            await db.rollback()
            logger.error(f'No se pudo borrar al alumno {alumno_nombre}')
            raise HTTPException(status_code=500, detail=f"No se pudo borrar al alumno: {str(e)}")
    
        return {"mensaje":"exito"}
# Crear profesores

async def crear_profesor(
    db: AsyncSession,
    profesor: schemas.ProfesorCreate
) -> schemas.ProfesorResponse:
    try:
        # Verificar que no exista el profesor
        query_profesor = select(models.Profesor).where(models.Profesor.profesor == profesor.profesor)
        result = await db.execute(query_profesor)
        profesor_existente = result.scalar_one_or_none()

        if profesor_existente:
            logger.error(f'El profesor {profesor} ya existe')
            raise HTTPException(status_code=400, detail="El profesor ya existe")

        # Crear el nuevo profesor
        nuevo_profesor = models.Profesor(profesor=profesor.profesor)
        db.add(nuevo_profesor)
        logger.info(f'Se añade el profesor {profesor}')
        await db.commit()
        await db.refresh(nuevo_profesor)

        # Lista de instrumentos
        instrumentos = [
            profesor.instrumento1,
            profesor.instrumento2,
            profesor.instrumento3,
            profesor.instrumento4,
            profesor.instrumento5
        ]

        # Crear los registros de profesor_instrumento
        for instrumento in instrumentos:
            if instrumento:
                query_instrumento = select(models.Instrumento).where(models.Instrumento.instrumento == instrumento)
                result = await db.execute(query_instrumento)
                instrumento_obj = result.scalar_one()

                nuevo_instrumento = models.Profesor_Instrumento(
                    profesor_id=nuevo_profesor.id,
                    instrumento_id=instrumento_obj.id
                )
                db.add(nuevo_instrumento)
                logger.info(f'Se añade la relación entre profesor e instrumentos')

        await db.commit()

        # Recargar el profesor después de la transacción
        await db.refresh(nuevo_profesor)

    except SQLAlchemyError as e:
        await db.rollback()
        logger.error(f"Error al crear el profesor {profesor}")
        raise HTTPException(status_code=500, detail=f"Error al crear profesor: {str(e)}")

    return schemas.ProfesorResponse(
        id=nuevo_profesor.id,
        profesor=nuevo_profesor.profesor,
        instrumento1=profesor.instrumento1,
        instrumento2=profesor.instrumento2,
        instrumento3=profesor.instrumento3,
        instrumento4=profesor.instrumento4,
        instrumento5=profesor.instrumento5
    )

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
        logger.error(f'No se encuentra al profesor {profesor_nombre}')
        raise HTTPException(status_code=404, detail="Profesor no encontrado")

    # Actualizar los campos del profesor
    update_data = profesor.model_dump()
    for key, value in update_data.items():
        setattr(existing_profesor, key, value)

    try:
        await db.commit()
        await db.refresh(existing_profesor)
        logger.info(f'Se actualizan los datos del profesor {profesor_nombre}')
    except SQLAlchemyError:
        await db.rollback()
        logger.error(f'No se pudo actualizar al profesor {profesor_nombre}')
        raise HTTPException(status_code=500, detail="No se pudo actualizar al profesor")
    
    return {"mensaje":"exito"}
    
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
        logger.error(f'{nombre_profesor} no encontrado')
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    
    # Formatear la respuesta para incluir el nombre del instrumento
    profesor_data = {
        "nombre_profesor": profesor.profesor,
        "instrumentos": [
            {"nombre_instrumento": pi.instrumento.instrumento}
            for pi in profesor.profesor_instrumentos
        ]
    }

    logger.info(f'Recuperados datos del profesor {nombre_profesor}')
    
    return profesor_data

# Borrar un profesor


async def borrar_profesor(
    db: AsyncSession, 
    profesor_name: str
):
    async with db.begin():
        result = await db.execute(select(models.Profesor).filter(models.Profesor.profesor == profesor_name))
        profesor = result.scalars().first()
        
        if not profesor:
            logger.error(f'Profesor {profesor_name} no encontrado')
            raise HTTPException(status_code=404, detail="Profesor no encontrado")
        
        await db.delete(profesor)
        
        try:
            await db.commit()
        except SQLAlchemyError:
            await db.rollback()
            logger.error(f'No se pudo borrar al profesor {profesor_name}')
            raise HTTPException(status_code=500, detail="No se pudo borrar el profesor")
    
        return {"mensaje": "Exito"}
    
# Actualizar precios

async def actualizar_precios(
    db: AsyncSession,
    pack_name: str,
    pack: schemas.ActualizarPrecio
) -> models.Pack: 

    result = await db.execute(select(models.Pack).filter(models.Pack.pack == pack_name))
    pack_existente = result.scalars().first()

    if not pack_existente:
        logger.error(f'No se encuentra el pack {pack_name}')
        raise HTTPException(status_code = 404, detail = "Pack no encontrado")
    
    update_data = pack.model_dump()
    for key, value in update_data.items():
        setattr(pack_existente, key, value)

    try:
        await db.commit()
        logger.info(f'Precio de {pack_name} actualizado')
        await db.refresh(pack_existente)
    except SQLAlchemyError:
        await db.rollback()
        logger.error(f"No se pudo actualizar el precio de {pack_name}")
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
        logger.error(f"Tipo de descuento {descuento_desc} no encontrado")
        raise HTTPException(status_code=404, detail = "Tipo de descuento no encontrado")
    
    update_data = descuento.model_dump()
    for key, value in update_data.items():
        setattr(descuento_existente, key, value)

    try:
        await db.commit()
        logger.info(f'Descuento de {descuento_desc} actualizado correctamente')
        await db.refresh(descuento_existente)
    except SQLAlchemyError:
        await db.rollback()
        logger.error(f"No se pudo actualizar el descuento de {descuento_desc}")
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
        logger.error(f'No se encuentra el pack {pack_name}')
        raise HTTPException(status_code=404, detail = "Pack no encontrado")
    
    logger.info(f'Revisado precio de {pack_name}')
    return pack_existente

# Comprobar descuentos

async def ver_descuentos(
    db:AsyncSession,
    descuento_descripcion: str
)-> models.Descuento:
    result = await db.execute(select(models.Descuento).filter(models.Descuento.descripcion == descuento_descripcion))
    descuento_existente = result.scalars().first()

    if not descuento_existente:
        logger.error(f"Tipo de descuento {descuento_descripcion} no encontrado")
        raise HTTPException(status_code=404, detail = "Descripción de descuento no encontrado")
    
    logger.info(f'Revisado descuento de {descuento_descripcion}')
    return descuento_existente