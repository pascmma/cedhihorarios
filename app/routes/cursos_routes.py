from flask import Blueprint,request, jsonify
from app.services.cursos_service import (get_all_cursos,get_curso_by_id,create_curso,update_curso,delete_curso,update_availability,delete_cursos_array)

cursos_blueprint = Blueprint('cursos',__name__)

@cursos_blueprint.route('/getCursos',methods=['GET'])
def get_cursos():
    print("Inicio de get cursos")
    cursos = get_all_cursos()
    response = {
        "cursos":[curso.to_dict() for curso in cursos]
    }
    return jsonify(response),200

@cursos_blueprint.route('/getCurso/<int:curso_id>',methods=['GET'])
def get_curso(curso_id):
    curso = get_curso_by_id(curso_id)
    if not curso:
        return jsonify({"error":"Curso no encontrado."}), 404
    return jsonify(curso.to_dict())

@cursos_blueprint.route('/addCurso',methods=['POST'])
def add_curso():
    data = request.json
    print("Se inicio el agregar del curso.")
    new_curso = create_curso(data)
    response = {
        "message":"Curso agregado exitosamente",
        "curso":new_curso.to_dict()
    }
    return jsonify(response),201

@cursos_blueprint.route('/updateCurso/<int:curso_id>',methods=['PUT'])
def update_curso_data(curso_id):
    data = request.json
    updated_curso = update_curso(curso_id,data)
    if not updated_curso:
        return jsonify({"error":"Curso no encontrado"}),404
    response = {
        "message":"Curso agregado exitosamente",
        "aula": updated_curso.to_dict()
    }
    return jsonify(updated_curso.to_dict())
    
@cursos_blueprint.route('/deleteCurso/<int:curso_id>',methods=['DELETE'])
def delete_curso_data(curso_id):
    deleted = delete_curso(curso_id)
    if not deleted:
        return jsonify({"error":"Curso no encontrado"}),404
    return jsonify({"message":"Curso eliminado correctamente"})


@cursos_blueprint.route('/enableCurso/<int:curso_id>',methods=['PATCH'])
def enable_curso(curso_id):
    try:
        result = update_availability(curso_id)
        if not result:
            return jsonify({"error":"Curso no encontrado"}),404
        return jsonify({"message":"Curso habilitado como Unidad Didactica"})
    except Exception as e:
        return jsonify({"error":str(e)}),500 
    
@cursos_blueprint.route('/deleteSelectedCursos', methods=['DELETE'])
def delete_cursos_selected_route():
    data = request.get_json()

    if not data or not isinstance(data,list):
        return jsonify({"error":"Se necesita un cuerpo con 'curso_id"}),404
    
    resultado = delete_cursos_array(data)

    if "error" in resultado:
        return jsonify({"error":resultado["error"]}),500
    
    return jsonify({
        "message":"eliminacion completada",
    }),200