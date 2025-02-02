from app.models import Curso
from app.extensions import db

def get_all_cursos():
    return Curso.query.all()

def get_curso_by_id(profesor_id):
    return Curso.query.get(profesor_id)

def create_curso(data):
    new_curso = Curso(
        nombre = data.get('nombre'),
        carrera = data.get('carrera'),
        plan_estudios = data.get('plan_estudios'),
        semestre = data.get('semestre'),    
        creditos = data.get('creditos'),
        tipo_curso = data.get('tipo_curso'),
        estado = False,
        estado_curso = data.get('estado_curso')
    )
    db.session.add(new_curso)
    db.session.commit()
    return new_curso


def update_curso(curso_id,data):
    curso = Curso.query.get(curso_id)
    if not curso:
        return None
    
    for key,value in data.items():
        setattr(curso,key,value)

    db.session.commit()
    return curso


def delete_curso(curso_id):
    curso = Curso.query.get(curso_id)
    if not curso:
        return False
    db.session.delete(curso)
    db.session.commit()
    return True 

def update_availability(curso_id):
    curso = Curso.query.get(curso_id)
    if not curso:
        return None
    curso.estado = True
    db.session.commit()
    return True
    
        
def delete_cursos_array(cursos):
    cursos_ids = [curso['curso_id'] for curso in cursos]

    cursos_to_delete = Curso.query.filter(Curso.curso_id.in_(cursos_ids)).all()

    for curso in cursos_to_delete:
        db.session.delete(curso)
    db.session.commit()

    return{
        "message":"Se eliminaron los cursos."
    }