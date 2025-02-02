from app.extensions import db
from sqlalchemy.dialects.postgresql import JSON
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
    

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

class Profesor(db.Model):
    __tablename__ = 'profesores'

    profesor_id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String,nullable=False)
    email = db.Column(db.String, nullable=False)
    contacto = db.Column(db.Integer, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    especialidad = db.Column(db.ARRAY(db.String),nullable=False)
    genero = db.Column(db.String, nullable=False)
    jornada = db.Column(db.String, nullable=False)
    prioridad = db.Column(db.Integer, nullable=False)
    disponibilidad = db.Column(JSON, nullable=False)

    def to_dict(self):
        return {
            "profesor_id": self.profesor_id,
            "nombres": self.nombres,
            "email": self.email,
            "contacto": self.contacto,
            "edad": self.edad,
            "status": self.status,
            "especialidad": self.especialidad,
            "genero": self.genero,
            "jornada": self.jornada,
            "prioridad": self.prioridad,
            "disponibilidad": self.disponibilidad,
        }


    def __repr__(self) -> str:
        return f"<Profesor {self.nombre}>"
    


# curso es la Unidad didactica
class Curso(db.Model):
    __tablename__ = 'cursos'

    curso_id = db.Column(db.Integer, primary_key=True) # id del curso 
    nombre = db.Column(db.String, nullable= False) # nombre del curso 
    plan_estudios = db.Column(db.Integer, nullable=False) # plan de estudios al que pertenece
    semestre = db.Column(db.Integer, nullable=False)
    carrera  = db.Column(db.String, nullable=False)
    creditos = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Boolean,nullable=False) # ver si es una unidad didactica
    tipo_curso = db.Column(db.String, nullable=False)
    estado_curso = db.Column(db.String, nullable=False) # si un curso es de formacion o carrera

    def to_dict(self):
        return{
            "curso_id":self.curso_id,
            "nombre":self.nombre,
            "plan_estudios":self.plan_estudios,
            "semestre":self.semestre,
            "carrera":self.carrera,
            "creditos":self.creditos,
            "estado":self.estado,
            "tipo_curso":self.tipo_curso,
            "estado_curso": self.estado_curso
        }
    unidades_didacticas = db.relationship('UnidadDidactica',back_populates='curso')




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

    
class UnidadDidactica(db.Model):
    __tablename__ = 'unidades_didacticas'

    unidad_id = db.Column(db.Integer, primary_key=True)
    programa = db.Column(db.String, nullable=False)  # Curso asociado
    tipo_plan = db.Column(db.String, nullable=False)
    plan_estudios = db.Column(db.Integer, nullable=False)
    modalidad = db.Column(db.String, nullable=False)
    enfoque = db.Column(db.String, nullable=False)
    semestre = db.Column(db.Integer, nullable=False)
    unidad_didactica = db.Column(db.String, nullable=False)
    periodo_academico = db.Column(db.String, nullable=False)
    seccion = db.Column(db.String, nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.curso_id'), nullable=False)  # Relación con Curso
    profesor_principal = db.Column(db.String,nullable=False) 
    profesor_apoyo = db.Column(db.String, nullable=False) 
    horas_semanales = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return{
            "unidad_id":self.unidad_id,
            "programa":self.programa,
            "tipo_plan":self.tipo_plan,
            "plan_estudios":self.plan_estudios,
            "modalidad":self.modalidad,
            "enfoque":self.enfoque,
            "seccion":self.seccion,
            "semestre":self.semestre,
            "profesor_principal":self.profesor_principal,
            "profesor_apoyo":self.profesor_apoyo,
            "unidad_didactica":self.unidad_didactica,
            "periodo_academico":self.periodo_academico,
            "horas_semanales":self.horas_semanales
            
            
        }   

    curso = db.relationship('Curso', back_populates='unidades_didacticas')
    
class SesionesAcademicas(db.Model):
    __tablename__ = 'sesiones_academicas'

    sesion_academica_id = db.Column(db.Integer, primary_key=True)
    tipo_aula = db.Column(db.String,nullable=True)
    unidad_didactica = db.Column(db.String, nullable=True)
    horario =  db.Column(JSON, nullable=False)
    sede = db.Column(db.String,nullable=True)
    tipo_curso = db.Column(db.String,nullable=True)
    periodo_academico = db.Column(db.String, nullable=False)
    seccion = db.Column(db.String, nullable=False)
    semestre = db.Column(db.Integer, nullable=False)
    programa = db.Column(db.String, nullable=False)
    profesor_principal = db.Column(db.String,nullable=False) 
    profesor_apoyo = db.Column(db.String, nullable=False) 
    flag_cruce = db.Column(db.Boolean, nullable=False)



    def to_dict(self):
        return{
           "sesion_academica_id":self.sesion_academica_id,
           "tipo_aula":self.tipo_aula,
           "unidad_didactica":self.unidad_didactica,
           "horario":self.horario,
           "sede":self.sede,
           "tipo_curso":self.tipo_curso,
           "periodo_academico":self.periodo_academico,
           "seccion":self.seccion,
           "semestre":self.semestre,
           "programa":self.programa,
           "profesor_principal":self.profesor_principal,
           "profesor_apoyo":self.profesor_apoyo,
           "flag_cruce":self.flag_cruce,
        }
    

"""
class Horario(db.Model):
    pass

    """