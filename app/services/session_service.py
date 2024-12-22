#from app.models import sessssion
from app.models import UnidadDidactica, Curso,Profesor
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
    pass


"""
FILTRAR POR  LA PRIORIDAD DE LOS PROFESORS
"""

"""
FILTRAR LAS HORAS SEMANALES DE LA UNIDAD DIDACTICA
"""

"""
SEPARAR LAS HORAS DEPENDIENDO DE LAS HORAS QUE SE TENGAN EN LA SEMANA
"""

"""
SEPARAR EN DOS HORARIOS CON EL REFRIGERIO DE EN MEDIO
"""
