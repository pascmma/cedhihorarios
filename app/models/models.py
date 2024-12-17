from app.extensions import db
from sqlalchemy.dialects.postgresql import JSON
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class Profesor(db.Model):
    __tablename__ = 'profesores'

    profesor_id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String,nullable=False)
    email = db.Column(db.String, nullable=False)
    contacto = db.Column(db.Integer, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    ciudad = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    especialidad = db.Column(db.ARRAY(db.String),nullable=False)
    genero = db.Column(db.String, nullable=False)
    jornada = db.Column(db.String, nullable=False)
    horasSemanales = db.Column(db.Integer, nullable=False)
    prioridad = db.Column(db.Integer, nullable=False)
    disponibilidad = db.Column(JSON, nullable=False)

    def to_dict(self):
        return {
            "profesor_id": self.profesor_id,
            "nombres": self.nombres,
            "email": self.email,
            "contacto": self.contacto,
            "edad": self.edad,
            "ciudad": self.ciudad,
            "status": self.status,
            "especialidad": self.especialidad,
            "genero": self.genero,
            "jornada": self.jornada,
            "horasSemanales": self.horasSemanales,
            "prioridad": self.prioridad,
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
    estado = db.Column(db.Boolean,nullable=False) # ver si es una unidad didactica
    tipo_curso = db.Column(db.String, nullable=False)

    def to_dict(self):
        return{
            "curso_id":self.curso_id,
            "nombre":self.nombre,
            "plan_estudios":self.plan_estudios,
            "modalidad":self.modalidad,
            "semestre":self.semestre,
            "carrera":self.carrera,
            "creditos":self.creditos,
            "estado":self.estado,
            "tipo_curso":self.tipo_curso
        }




class Aula(db.Model):
    __tablename__ = 'aulas'

    aula_id = db.Column(db.Integer, primary_key=True)
    tipo_aula = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)
    local = db.Column(db.String, nullable=False)
    formato_aula = db.Column(db.String, nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return{
            "aula_id":self.aula_id,
            "tipo_aula":self.tipo_aula,
            "nombre":self.nombre,
            "local":self.local,
            "formato_aula":self.formato_aula,
            "capacidad":self.capacidad
            
            }

    



"""
class Horario(db.Model):
    pass

class Aula(db.Model):
    pass
    """