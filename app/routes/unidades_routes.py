from flask import Blueprint, request, jsonify
from app.services.unidades_services import(get_all_unidades,get_unidad_service,add_unidad_service,update_unidad_service,delete_unidad_service,prueba,add_unidad_service_2,get_all_unidades_2)
from app.services.session_service import (generar_horario_base)


unidad_blueprint = Blueprint('unidad',__name__)

@unidad_blueprint.route('/getUnidades',methods=['GET'])
def get_unidades():
    print("Inicio de get unidades")
    unidades = get_all_unidades_2()
    response = {
        "unidades":[unidad for unidad in unidades]
    }
    return jsonify(response),200

@unidad_blueprint.route('/getUnidad/<int:unidad_id>',methods=['GET'])
def get_unidad(unidad_id):
    unidad = get_unidad_service(unidad_id)
    if not unidad:
        return jsonify({"error":"No se encontro la unidad didactica"})
    return jsonify(unidad.to_dict())


@unidad_blueprint.route('/addUnidad',methods=['POST'])
def add_unidad():
    data =request.json
    new_unidad = add_unidad_service_2(data)
    response = {
        "message":"Unidad didactica agregado exitosamente",
        "unidad":new_unidad.to_dict()
    }
    return jsonify(response),201


@unidad_blueprint.route('/updateUnidad/<int:unidad_id>',methods=['PUT'])
def update_unidad(unidad_id):
    data =request.json
    updated = update_unidad_service(unidad_id,data)
    if not updated:
        return jsonify({"error":"Unidad no encontrada"}),404
    return jsonify(updated.to_dict()),201

@unidad_blueprint.route('/deleteUnidad/<int:unidad_id>',methods=['DELETE'])
def delete_unidad(unidad_id):
    deleted =delete_unidad_service(unidad_id)
    if not deleted:
        return jsonify({"error":"Unidad didactica no encotradad"}),404
    return jsonify({"message":"Unidad didactica eleminada correctamente"}),201

@unidad_blueprint.route('/test',methods=['GET'])
def test():
    horario = generar_horario_base()

    print("el horario base")
    return jsonify({"horario":horario})