from app.models import Usuario
from app.extensions import db
from flask_jwt_extended import create_access_token
from datetime import timedelta



def register_user(email,password,categoria):
    try:

        if Usuario.query.filter_by(email=email).first():
            return{"error":"Email ya registrado"}, 400
    
        new_user = Usuario(email=email,categoria=categoria)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()
        return{"message": "Usuario registrado existosamente"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error":f"Error interno en el servidor: {str(e)}"},500

def login_user(email,password):
    try:
        user = Usuario.query.filter_by(email=email).first()
        print("EL usuario es: ",user)
        if not user or not user.check_password(password):
            return {"error":"Credenciales invalidas"},401
        access_token = create_access_token(identity={"user_id":user.user_id,"email":user.email},expires_delta=timedelta(hours=10))

        #return {"menssage":"Inicio de sesion exitoso","user_id":user.user_id,"token":access_token},200
        return {"menssage":"Inicio de sesion exitoso", "token":access_token,'user': {"user_id":user.user_id, "categoria": user.categoria, "email": user.email}},200
    except Exception as e:
        return {"error": f"Error interno del servidor: {str(e)}"}, 500


    

def get_all_users():
    try:
        users = Usuario.query.all()
        user_list = [
            {"user_id":user.user_id, "email":user.email, "categoria":user.categoria}
            for user in users
        ]
        return user_list,200
    except Exception as e:
        return {"error":f"Error al obtener los usuarios: {str(e)}"},500
