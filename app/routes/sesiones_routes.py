from flask import Blueprint, request,jsonify
from app.services.session_service import (add_sesion,get_sesion,get_sesiones,update_sesion,delete_sesion,generar_horario_base,asignar_horarios,delete_all_sesions)


sesion_academica_blueprint = Blueprint('sesiones',__name__)

@sesion_academica_blueprint.route('/getSesiones', methods=['GET'])
def get_sesiones_route():
    print("Inicio de get sesiones")
    sesiones = get_sesiones()
    response = {
        "sesiones":[sesion.to_dict() for sesion in sesiones]
    }
    return jsonify(response),200

@sesion_academica_blueprint.route('/getSesion/<int:sesion_academica_id>', methods=['GET'])
def get_sesion_route(sesion_academica_id):
    sesion = get_sesion(sesion_academica_id)
    if not sesion:
        return jsonify({"error":"No se encontro la sesion"})
    return jsonify(sesion.to_dict())

@sesion_academica_blueprint.route('/addSesion', methods=['POST'])
def add_sesion_route():
    data = request.json
    new_sesion = add_sesion(data)
    response = {
        "message":"Sesion academica agregada exitosamente",
        "sesion":new_sesion.to_dict()

    }
    return jsonify(response),201


@sesion_academica_blueprint.route('/updateSesion/<int:sesion_academica_id>', methods=['PUT'])
def update_sesion_route(sesion_academica_id):
    data = request.json
    updated = update_sesion(sesion_academica_id, data)
    if not updated:
        return jsonify ({"error":"Sesion no encontrada"}),404
    return jsonify(updated.to_dict()),201
 

@sesion_academica_blueprint.route('/deleteSesion/<int:sesion_academica_id>', methods=['DELETE'])
def delete_sesion_route(sesion_academica_id):
    deleted = delete_sesion(sesion_academica_id)
    if not deleted:
        return jsonify({"error":"Sesion academica no encontrada"}),404
    return jsonify({"message":"Sesion academica eliminada correctamente"}),201

@sesion_academica_blueprint.route('/generarHorario', methods=['GET'])
def generar_horario_route():
    pass

@sesion_academica_blueprint.route('/deleteAllSesions', methods=['GET'])
def delete_all_sesions_route():
    print("Inicio de borrar todas las sesiones")
    success = delete_all_sesions()

    if success:
        return jsonify({"message":"Se eliminaron todas las sesiones"}),201
    else:
        return jsonify({"message":"No se pudo eliminar"}),500


