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
    
def delete_aula_service(aula_id):
    aula = Aula.query.get(aula_id)
    if not aula:
        return False
    db.session.delete(aula)
    db.session.commit()
    return True
    

def delete_aulas_array(aulas):
    aulas_ids = [aula['aula_id'] for aula in aulas]

    aulas_to_delete = Aula.query.filter(Aula.aula_id.in_(aulas_ids)).all()

    for aula in aulas_to_delete:
        db.session.delete(aula)
    db.session.commit()

    return{
        "message":"Se eliminaron las aulas."
    }