from app.routes.auth_routes import auth_blueprint
from app.routes.profesor_routes import profesor_blueprint
from app.routes.cursos_routes import cursos_blueprint
from app.routes.aula_routes import aulas_blueprint
from app.routes.unidades_routes import unidad_blueprint
from app.routes.sesiones_routes import sesion_academica_blueprint
from app.routes.data_routes import excel_blueprint

def register_blueprints(app):
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(profesor_blueprint, url_prefix='/profesores')
    app.register_blueprint(cursos_blueprint, url_prefix='/cursos')
    app.register_blueprint(aulas_blueprint, url_prefix='/aulas')
    app.register_blueprint(unidad_blueprint, url_prefix='/unidades')
    app.register_blueprint(sesion_academica_blueprint, url_prefix='/sesiones')
    app.register_blueprint(excel_blueprint, url_prefix='/excel')
    

    
