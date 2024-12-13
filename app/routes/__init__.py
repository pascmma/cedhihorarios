from app.routes.auth_routes import auth_blueprint
from app.routes.profesor_routes import profesor_blueprint

def register_blueprints(app):
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(profesor_blueprint, url_prefix='/profesores')
    
