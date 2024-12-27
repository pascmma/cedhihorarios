from app.extensions import db
import pandas as pd
from io import BytesIO



def formato_tablas(tabla):
    try:
        columnas = [column.name for column in tabla.__table__.columns]

        df = pd.DataFrame(columns=columnas)
        output = BytesIO()
        with pd.ExcelWriter(output,engine='openpyxl') as writer:
            df.to_excel(writer,index=False,sheet_name=tabla.__tablename__.capitalize())
        output.seek(0)

        return output
    except Exception as e:
        raise Exception(f"Error al generar el archivo Excel:  {str(e)}")
    

def get_data_service(tabla):
    try:
        print("INICIO DE GET")
        # Obtener nombres de las columnas de la tabla
        columnas = [column.name for column in tabla.__table__.columns]

        # Obtener todos los datos de la tabla
        datos = db.session.query(tabla).all()
        print("DATOS: ",datos)

        # Verificar si se han recuperado datos
        if not datos:
            raise Exception("No se encontraron datos en la tabla.")

        # Convertir los datos obtenidos a un diccionario de columnas y valores
        datos_dict = []
        for fila in datos:
            fila_dict = {}
            for col in columnas:
                fila_dict[col] = getattr(fila, col)
            datos_dict.append(fila_dict)

        # Crear un DataFrame con los datos
        df = pd.DataFrame(datos_dict)

        # Verificar que el DataFrame no esté vacío
        if df.empty:
            raise Exception("El DataFrame está vacío.")

        # Crear un archivo Excel en memoria
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            # Escribir el DataFrame en una hoja de Excel
            df.to_excel(writer, index=False, sheet_name=tabla.__tablename__.capitalize())

        # Preparar el archivo para ser descargado
        output.seek(0)
        return output
    except Exception as e:
        raise Exception(f"Error al generar el archivo Excel: {str(e)}")