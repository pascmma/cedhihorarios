from app.models import Aula
from app.extensions import db

def get_all_aulas():
    print("OBTENER TODAS LAS AULAS")
    return Aula.query.all()

def create_aula(data):
    new_aula = Aula(
        tipo_aula = data.get('tipo_aula'),
        nombre = data.get('nombre'),
        local = data.get('local'),
        formato_aula = data.get('formato_aula'),
        capacidad = data.get('capacidad')
    )
    db.session.add(new_aula)
    db.session.commit()
    return new_aula
    

def update_aula(aula_id,data):
    aula = Aula.query.get(aula_id)
    if not aula:
        return None
    for key, value in data.items():
        setattr(aula,key,value)
    db.session.commit()
    return aula
    