from flask import Blueprint,request,jsonify
from app.services.aulas_service import (get_all_aulas,create_aula,update_aula,delete_aula_service)

aulas_blueprint = Blueprint('aulas',__name__)

@aulas_blueprint.route('/getAulas',methods=['GET'])
def get_aulas():
    aulas = get_all_aulas()
    response = {
        "aulas":[aula.to_dict() for aula in aulas]
    }
    return jsonify(response),200

@aulas_blueprint.route('/addAula',methods=['POST'])
def add_aula():
    data= request.json
    new_aula = create_aula(data)
    response = {
        "message":"Curso agregado exitosamente",
        "aula":new_aula.to_dict()
    }
    return jsonify(response),201


@aulas_blueprint.route('/updateAula/<int:aula_id>', methods=['PUT'])
def update_aula_data(aula_id):
    data = request.json
    updated_aula = update_aula(aula_id,data)
    if not updated_aula:
        return jsonify({"error":"Aula no encontrada"}),404
    response = {
        "message":"Curso agregado exitosamente",
        "aula": updated_aula.to_dict()
    }
    return jsonify(response),201


@aulas_blueprint.route('/deleteAula/<int:aula_id>', methods=['DELETE'])
def delete_aula(aula_id):
    deleted_aula = delete_aula_service(aula_id)
    if not deleted_aula:
        return jsonify({"error":"Aula no encontrada."})
    return jsonify({"message":"Aula eliminada correctamente"})