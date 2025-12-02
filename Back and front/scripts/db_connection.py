import mysql.connector
from mysql.connector import Error

def get_db_connection():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '1234',
        'database': 'Medicinal_plants_project',
        'port': 3306
    }
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None