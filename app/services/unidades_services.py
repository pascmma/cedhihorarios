from app.models import UnidadDidactica
from app.extensions import db
"""
CRUD unidades didacticas
"""

def get_all_unidades():
    return UnidadDidactica.query.all()

def get_unidad_service(unidad_id):
    return UnidadDidactica.query.get(unidad_id)

def add_unidad_service(data):
    new_unidad = UnidadDidactica(
        programa = data.get('programa'),
        tipo_plan = data.get('tipo_plan'),
        plan_estudios = data.get('plan_estudios'),
        modalidad =data.get('modalidad'),
        enfoque =data.get('enfoque'),
        seccion = data.get('enfoque'),
        periodo_academico =data.get('periodo_academico'),
        profesor_principal = data.get('profesor_principal'),
        profesor_secundario = data.get('profesor_secundario')

    )

def update_unidad_service(unidad_id,data):
    unidad = UnidadDidactica.query.get(unidad_id)
    if not unidad:
        return None
    for key,value in data.items():
        setattr(unidad,key,value)

    db.session.commit()
    return unidad

def delete_unidad_service(unidad_id):
    unidad = UnidadDidactica.query.get(unidad_id)
    if not unidad:
        return False
    db.session.delete(unidad)
    db.session.commit()
    return True