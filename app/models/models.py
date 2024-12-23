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
    ciudad = db.Column(db.String, nullable=False)
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
            "ciudad": self.ciudad,
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

    def to_dict(self):
        return{
            "curso_id":self.curso_id,
            "nombre":self.nombre,
            "plan_estudios":self.plan_estudios,
            "semestre":self.semestre,
            "carrera":self.carrera,
            "creditos":self.creditos,
            "estado":self.estado,
            "tipo_curso":self.tipo_curso
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
    nombre_unidad = db.Column(db.String, nullable=True)
    aula = db.Column(db.String,nullable=True)
    aforo = db.Column(db.Integer,nullable=True)
    dia = db.Column(db.String,nullable=True)
    tipo_clase = db.Column(db.String,nullable=True)
    docente = db.Column(db.String,nullable=True)
    hora_inicio = db.Column(db.String,nullable=True)
    hora_final = db.Column(db.String,nullable=True)
    cruce = db.Column(db.String,nullable=True)

    def to_dict(self):
        return{
            "sesion_academica_id":self.sesion_academica_id,
            "tipo_aula":self.tipo_aula,
            "nombre_unidad":self.nombre_unidad,
            "aula":self.aula,
            "aforo":self.aforo,
            "dia":self.dia,
            "tipo_clase":self.tipo_clase,
            "docente":self.docente,
            "hora_inicio":self.hora_inicio,
            "hora_final":self.hora_final,
            "cruce":self.cruce
        }
    

"""
class Horario(db.Model):
    pass

    """