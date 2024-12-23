from app.models import UnidadDidactica,Curso
from app.extensions import db
from sqlalchemy.orm import joinedload

"""
CRUD unidades didacticas
"""

def get_all_unidades():
    return UnidadDidactica.query.all()

def get_all_unidades_2():
    unidades = UnidadDidactica.query.options(joinedload(UnidadDidactica.curso)).all()
    resultado = []
    
    for unidad in unidades:
        
        unidad_dict = unidad.to_dict()
        
        if unidad.curso:
            curso_dict = unidad.curso.to_dict()
            unidad_dict.update(curso_dict)  
            
        resultado.append(unidad_dict)
    
    return resultado

def get_unidad_service(unidad_id):
    return UnidadDidactica.query.get(unidad_id)

def add_unidad_service(data):
    
    new_unidad = UnidadDidactica(
        programa = data.get('programa'),
        tipo_plan = data.get('tipo_plan'),
        plan_estudios = data.get('plan_estudios'),
        modalidad =data.get('modalidad'),
        enfoque =data.get('enfoque'),
        seccion = data.get('seccion'),
        semestre =data.get('semestre'),
        profesor_principal = data.get('profesor_principal'),
        profesor_apoyo = data.get('profesor_apoyo'),
        unidad_didactica = data.get('unidad_didactica'),
        periodo_academico =data.get('periodo_academico'),
        

    )
    db.session.add(new_unidad)
    db.session.commit()
    return new_unidad

def add_unidad_service_2(data):
    aux = data.get('unidad_didactica')
    curso_ids = Curso.query.with_entities(Curso.curso_id).filter_by(nombre=aux).first()
    if curso_ids:
        curso_ids = curso_ids[0]
    else:
        raise ValueError()

    new_unidad = UnidadDidactica(
        programa = data.get('programa'),
        tipo_plan = data.get('tipo_plan'),
        plan_estudios = data.get('plan_estudios'),
        modalidad =data.get('modalidad'),
        enfoque =data.get('enfoque'),
        seccion = data.get('seccion'),
        semestre =data.get('semestre'),
        profesor_principal = data.get('profesor_principal'),
        profesor_apoyo = data.get('profesor_apoyo'),
        unidad_didactica = data.get('unidad_didactica'),
        periodo_academico =data.get('periodo_academico'),
        curso_id = curso_ids,
        horas_semanales= data.get('horas_semanales')

        

    )
    db.session.add(new_unidad)
    db.session.commit()
    return new_unidad



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

def prueba(data):
    nombre = data.get('nombre')
    curso = Curso.query.with_entities(Curso.creditos).filter_by(nombre=nombre).first()
    return curso

