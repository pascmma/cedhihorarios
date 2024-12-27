from app.extensions import db
import pandas as pd
import numpy as np
from io import BytesIO
from app.models import Profesor

# servicio de profesores
def formato_profesores():
    try:
        columnas = [column.name for column in Profesor.__table__.columns]

        df = pd.DataFrame(columns=columnas)
        output = BytesIO()
        with pd.ExcelWriter(output,engine='xlsxwriter') as writer:
            df.to_excel(writer,index=False,sheet_name='Profesores')
        output.seek(0)

        return output
    except Exception as e:
        raise Exception(f"Error al generar el archivo Excel:  {str(e)}")
    

# servicio de aulas
def formato_aulas():
    pass

# servicio de cursos
def formato_cursos():
    pass
