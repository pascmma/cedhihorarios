from flask import Blueprint,request,jsonify
from app.services.auth_service import register_user,login_user,get_all_users

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    categoria = data.get('categoria')
    
    if not all([email,password,categoria]):
        return jsonify({"error":"Faltan datos obligarorios"}), 400
    
    response, status_code = register_user(email,password,categoria)
    return jsonify(response),status_code

    


@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not all([email,password]):
        return jsonify({"error":"Faltan datos necesarios"}), 400
    response,status_code = login_user(email,password)
    return jsonify(response), status_code

@auth_blueprint.route('/getUsers',methods=['GET'])
def get_users():
    response, status_code = get_all_users()
    return jsonify(response), status_code

