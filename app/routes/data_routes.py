from app.models import Profesor,Aula,Curso
from flask import Blueprint,request, jsonify, send_file
from app.services.data_service import(formato_tablas,get_data_service)

excel_blueprint = Blueprint('excel',__name__)

@excel_blueprint.route('/generarModelo/<string:modelo>',methods=['GET'])
def generar_formato(modelo):
    try:
        modelos = {
            "profesor":Profesor,
            "aula":Aula,
            "curso":Curso
        }

        if modelo not in modelos:
            return jsonify({"error":"No existe la tabla"}),404
        output = formato_tablas(modelos[modelo])

        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=f"{modelo}_formato.xlsx"

        )

    except Exception as e:
        return{"error":str(e)},500
    
@excel_blueprint.route('/generarModeloFull/<string:modelo>',methods=['GET'])
def get_datos_route(modelo):
    try:
        modelos = {
            "profesor": Profesor,
            "aula": Aula,
            "curso": Curso,
        }

        if modelo not in modelos:
            return {"error": "Modelo no encontrado."}, 404

        output = get_data_service(modelos[modelo])

        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=f"{modelo}_lleno.xlsx"
        )
    except Exception as e:
        return {"error": str(e)}, 500