from app.extensions import db
from sqlalchemy.dialects.postgresql import JSON
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class Profesor(db.Model):
    __tablename__ = 'profesores'

    profesor_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String,nullable=False)
    genero = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    celular = db.Column(db.Integer, nullable=False)
    ciudad = db.Column(db.String, nullable=False)
    estado = db.Column(db.String, nullable=False)
    disponibilidad = db.Column(JSON, nullable=False)

    def to_dict(self):
        return {
            "profesor_id": self.profesor_id,
            "nombre": self.nombre,
            "genero": self.genero,
            "email": self.email,
            "edad": self.edad,
            "celular": self.celular,
            "ciudad": self.ciudad,
            "estado": self.estado,
            "disponibilidad": self.disponibilidad,
        }


    def __repr__(self) -> str:
        return f"<Profesor {self.nombre}>"
    
    

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable= False)
    password_hash = db.Column(db.String, nullable=False)
    categoria = db.Column(db.String,nullable=False)

    def set_password(self,password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self,password):
        return bcrypt.check_password_hash(self.password_hash,password)


# curso es la Unidad didactica
class Curso(db.Model):
    __tablename__ = 'cursos'

    curso_id = db.Column(db.Integer, primary_key=True) # id del curso 
    nombre = db.Column(db.String, nullable= False) # nombre del curso 
    plan_estudios = db.Column(db.String, nullable=False) # plan de estudios al que pertenece
    modalidad = db.Column(db.String, nullable=False)
    semestre = db.Column(db.Integer, nullable=False)
    carrera  = db.Column(db.String, nullable=False)
    creditos = db.Column(db.Integer, nullable=False)

class Aulas(db.Model):
    __tablename__ = 'aulas'

    aula_id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String, nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)

    



"""
class Horario(db.Model):
    pass

class Aula(db.Model):
    pass
    """