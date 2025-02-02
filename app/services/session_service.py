#from app.models import sessssion
from app.models import UnidadDidactica, Curso,Profesor,Aula,SesionesAcademicas
from app.extensions import db
from datetime import datetime, timedelta
from sqlalchemy.orm import joinedload

from math import floor

def dividir_horas_semanales(horas_semanales):
    """
    Divide las horas semanales en sesiones según las reglas:
    - Si es impar y mayor a 3, asigna 3 horas a la primera sesión.
    - El resto se divide en sesiones de 2 horas.
    """
    sesiones = []

    if horas_semanales == 1:
        sesiones.append(1)
        return sesiones

    if horas_semanales > 3 and horas_semanales % 2 != 0:
        sesiones.append(3)
        horas_semanales -= 3
    
    while horas_semanales >= 2:
        sesiones.append(2)
        horas_semanales -= 2

    if horas_semanales > 0:  # Para cualquier resto menor a 2
        sesiones.append(horas_semanales)
    
    return sesiones 

def generar_horario_base():
    horario_base = {}
    dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes"]
    hora_inicio = datetime.strptime("08:00", "%H:%M")
    hora_fin = datetime.strptime("16:00", "%H:%M")
    bloque_duracion = timedelta(minutes=45)

    for dia in dias_semana:
        horario_base[dia] = []
        hora_actual = hora_inicio
        while hora_actual + bloque_duracion <= hora_fin:
            bloque = {
                "hora_inicio": hora_actual.strftime("%H:%M"),
                "hora_fin": (hora_actual + bloque_duracion).strftime("%H:%M"),
                "ocupado": False,
                "unidad_didactica": None,
                "profesor": None,
                "aula": None
            }
            horario_base[dia].append(bloque)
            hora_actual += bloque_duracion

    return horario_base

def asignar_horarios():
    profesores = Profesor.query.order_by(Profesor.prioridad).all()
    unidades = UnidadDidactica.query.all()
    aulas = Aula.query.all()

    horario_general = generar_horario_base()
    conflictos = []

    for unidad in unidades:
        horas_restantes = unidad.horas_semanales
        asignado = False

        for profesor in profesores:
            disponibilidad = profesor.disponibilidad

            for dia, bloques in horario_general.items():
                if horas_restantes <= 0:
                    break

                if dia in [d["dia"] for d in disponibilidad]:
                    bloques_disponibles = [
                        b for b in bloques
                        if not b["ocupado"] and any(
                            b["hora_inicio"] >= d["horaInicio"] and b["hora_fin"] <= d["horaFin"]
                            for d in disponibilidad if d["dia"] == dia
                        )
                    ]

                    for bloque in bloques_disponibles:
                        if horas_restantes <= 0:
                            break

                        # Asignar aula disponible
                        aula_disponible = next(
                            (aula for aula in aulas if not any(
                                b["ocupado"] and b["aula"] == aula.nombre
                                for b in bloques
                            )), None
                        )

                        if aula_disponible:
                            bloque["ocupado"] = True
                            bloque["unidad_didactica"] = unidad.unidad_didactica
                            bloque["profesor"] = profesor.nombres
                            bloque["aula"] = aula_disponible.nombre
                            horas_restantes -= 0.75  # 45 minutos = 0.75 horas
                            asignado = True

        if not asignado:
            conflictos.append({
                "unidad_didactica": unidad.unidad_didactica,
                "profesor_prioridad": profesor.prioridad
            })

    return {"horario_general": horario_general, "conflictos": conflictos}



def get_sesiones():
    return SesionesAcademicas.query.all()

def get_sesion(sesion_academica_id):
    return SesionesAcademicas.query.get(sesion_academica_id)

def add_sesion(data):
    # Buscar la unidad didáctica por su nombre
    unidad_didactica_nombre = data.get('unidad_didactica')
    if not unidad_didactica_nombre:
        return {"error": "El campo 'unidad_didactica' es obligatorio"}, 400

    unidad = UnidadDidactica.query.filter_by(unidad_didactica=unidad_didactica_nombre).first()

    if not unidad:
        return {"error": f"No se encontró la Unidad Didáctica con el nombre '{unidad_didactica_nombre}'"}, 404

    
    new_sesion = SesionesAcademicas(
        tipo_aula=data.get('tipo_aula',None),
        unidad_didactica=unidad.unidad_didactica, 
        horario=data.get('horario'),
        sede=data.get('sede', None),
        tipo_curso=data.get('tipo_curso', None),
        periodo_academico=unidad.periodo_academico,  
        seccion=unidad.seccion,  
        semestre=unidad.semestre,  
        programa=unidad.programa,  
        profesor_principal=unidad.profesor_principal,
        profesor_apoyo=unidad.profesor_apoyo,  
        flag_cruce=data.get('flag_cruce', False) 
    )

    
    db.session.add(new_sesion)
    db.session.commit()

    return new_sesion



def update_sesion(sesion_academica_id,data):
    sesion = SesionesAcademicas.query.get(sesion_academica_id)
    if not sesion:
        return None
    for key, value in data.items():
        setattr(sesion,key,value)

    db.session.commit()
    return sesion


def delete_sesion(sesion_academica_id):
    sesion = SesionesAcademicas.query.get(sesion_academica_id)
    if not sesion:
        return False
    db.session.delete(sesion)
    db.session.commit()
    return True


def delete_all_sesions():
    db.session.query(SesionesAcademicas).delete()
    db.session.commit()
    return True


def delete_sesiones_array(sesiones):
    sesiones_ids = [sesion['sesion_academica_id'] for sesion in sesiones]

    sesiones_to_delete = SesionesAcademicas.query.filter(SesionesAcademicas.sesion_academica_id.in_(sesiones_ids)).all()

    for sesion in sesiones_to_delete:
        db.session.delete(sesion)
    db.session.commit()

    return{
        "message":"Se eliminaron las sesiones."
    }