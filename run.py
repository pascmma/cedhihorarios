from flask_cors import CORS
from app import create_app
from app.extensions import db
from sqlalchemy import text
import os

app = create_app()
CORS(app,origins="*")
# Verificar la conexión a la base de datos
with app.app_context():
    try:
        db.session.execute(text('SELECT 1'))  # Ejecuta una consulta básica para probar conexión
        print("Conexión exitosa a la base de datos.")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

# Crear las tablas en la base de datos
with app.app_context():
    try:
        db.create_all()  # Crea las tablas si no existen
        print("Tablas creadas exitosamente.")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")




if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port=5001,debug=True)
