from app.routes.auth_routes import auth_blueprint
from app.routes.profesor_routes import profesor_blueprint
from app.routes.cursos_routes import cursos_blueprint
from app.routes.aula_routes import aulas_blueprint

def register_blueprints(app):
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(profesor_blueprint, url_prefix='/profesores')
    app.register_blueprint(cursos_blueprint, url_prefix='/cursos')
    app.register_blueprint(aulas_blueprint, url_prefix='/aulas')
    
