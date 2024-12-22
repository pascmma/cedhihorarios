from flask import Blueprint, request, jsonify
from app.services.profesor_service import (get_all_profesores,get_profesor_by_id,create_profesor,update_profesor,delete_profesor)

profesor_blueprint = Blueprint('profesor',__name__)

@profesor_blueprint.route('/getProfesores',methods=['GET'])
def get_profesores():
    print("INICIO DE GET PROFESORES")
    profesores = get_all_profesores()
    response = {
        "profesores":[profesor.to_dict()for profesor in profesores]
    }
    return jsonify(response),200

@profesor_blueprint.route('/getProfesor/<int:profesor_id>', methods=['GET'])
def get_profesor(profesor_id):
    profesor = get_profesor_by_id(profesor_id)
    if not profesor:
        return jsonify({"error":"Profesor no encontrado"}), 404
    return jsonify(profesor.__dict__)

@profesor_blueprint.route('/addProfesor', methods=['POST'])
def add_profesor():
    print("Ruta de crear profesores")
    data = request.json
    new_profesor = create_profesor(data)
    response = {
        "message":"Profesor agregado exitosamente",
        "profesor": new_profesor.to_dict()
    }
    return jsonify(response),201

@profesor_blueprint.route('/updateProfesor/<int:profesor_id>',methods=['PUT'])
def update_profesor_data(profesor_id):
    data = request.json
    updated_profesor = update_profesor(profesor_id,data)
    if not update_profesor:
        return jsonify({"error":"Profesor no encontrado"}),404
    return jsonify(updated_profesor.to_dict())

@profesor_blueprint.route('/deleteProfesor/<int:profesor_id>', methods=['DELETE'])
def delete_profesor_data(profesor_id):
    deleted = delete_profesor(profesor_id)
    if not deleted:
        return jsonify({"error":"Profesor no encontrado"}),404
    return jsonify({"message":"Profesor eliminado correctamente"})
  