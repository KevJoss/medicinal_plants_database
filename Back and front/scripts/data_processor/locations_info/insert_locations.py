from scripts.db_connection import get_db_connection
from mysql.connector import Error

def insert_locations():
    locations_data = [
        ('Antonio Ante', 'Imbabura'),
        ('Urcuqui', 'Imbabura'),
        ('Otavalo', 'Imbabura'),
        ('Cotacachi', 'Imbabura'),
        ('Pimampiro', 'Imbabura'),
        ('Ibarra', 'Imbabura')
    ]

    connection = None
    try:
        connection = get_db_connection()
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            sql_query = """
            INSERT INTO locations (city_name, province_name) 
            VALUES (%s, %s)
            """
            
            cursor.executemany(sql_query, locations_data)
            
            connection.commit()
            
            print(f"¡Éxito! Se insertaron {cursor.rowcount} ubicaciones en la base de datos.")

    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
        
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada.")

if __name__ == "__main__":
    insert_locations()