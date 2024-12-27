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
        columnas = [column.name for column in tabla.__table__.columns]
        datos = db.session.query(tabla).all()

        if not datos:
            raise Exception("No se encontraron datos en la tabla.")

        # Convertir los datos obtenidos a un diccionario de columnas y valores
        datos_dict = []
        for fila in datos:
            fila_dict = {}
            for col in columnas:
                try:
                    fila_dict[col] = getattr(fila, col)  
                except AttributeError:
                    fila_dict[col] = None  
            datos_dict.append(fila_dict)

        df = pd.DataFrame(datos_dict)

        if df.empty:
            raise Exception("El DataFrame está vacío.")

        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name=tabla.__tablename__.capitalize())

        output.seek(0)
        return output
    except Exception as e:
        raise Exception(f"Error al generar el archivo Excel: {str(e)}")