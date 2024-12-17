from app.models import Profesor
from app.extensions import db

def get_all_profesores():
    return Profesor.query.all()

def get_profesor_by_id(profesor_id):
    return Profesor.query.get(profesor_id)

def create_profesor(data):
    new_profesor = Profesor(
        nombres = data.get('nombres'),
        email=data.get('email'),
        edad=data.get('edad'),
        contacto=data.get('contacto'),
        ciudad=data.get('ciudad'),
        status=data.get('status'),
        especialidad=data.get('especialidad'),
        genero=data.get('genero'),
        jornada=data.get('jornada'),
        horasSemanales=data.get('horasSemanales'),
        prioridad=data.get('prioridad'),
        disponibilidad=data.get('disponibilidad')
    )
    db.session.add(new_profesor)
    db.session.commit()
    return new_profesor


def update_profesor(profesor_id,data):
    profesor = Profesor.query.get(profesor_id)
    if not profesor:
        return None
    
    for key,value in data.items():
        setattr(profesor,key,value)

    db.session.commit()
    return profesor


def delete_profesor(profesor_id):
    profesor = Profesor.query.get(profesor_id)
    if not profesor:
        return False
    db.session.delete(profesor)
    db.session.commit()
    return True 