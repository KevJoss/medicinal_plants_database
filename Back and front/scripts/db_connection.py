import mysql.connector

def get_db_connection():
    config = {
        'user': 'root',
        'password': '1234', 
        'host': '127.0.0.1',
        'port': 3306,
        'database': 'Medicinal_plants_proyect',
        'charset': 'utf8mb4'
    }
    try:
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None