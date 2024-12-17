from flask import Flask
from app.config import Config
from app.extensions import db
from app.routes.auth_routes import auth_blueprint
from app.routes.profesor_routes import profesor_blueprint
from app.routes.cursos_routes import cursos_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')  # Agregar prefijo opcional
    app.register_blueprint(profesor_blueprint, url_prefix='/profesor')
    app.register_blueprint(cursos_blueprint, url_prefix='/cursos')
    
    return app

