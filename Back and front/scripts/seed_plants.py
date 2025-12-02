from data_processor import get_cleaned_data
from db_connection import get_db_connection

def insert_plants():
    # 1. Obtener datos limpios
    print("Cargando y limpiando datos del Excel...")
    data = get_cleaned_data()
    plants_dict = data["plants_dict"]
    places_list = data["places_list"]

    # 2. Conectar a BD
    connection = get_db_connection()
    if not connection:
        return
    cursor = connection.cursor()

    # 3. Query (Usando INSERT IGNORE para evitar errores si ya existen)
    query = "INSERT IGNORE INTO plants (location_id, current_name, scientific_name) VALUES (%s, %s, %s)"

    # 4. Preparar datos
    count = 1 # Ojo: Asegúrate de manejar los IDs correctamente si son autoincrementales
    rows_to_insert = []
    
    for place in places_list:
        # Aquí necesitarías lógica para obtener el location_id real de la BD si ya insertaste locaciones
        # Por ahora uso tu lógica del notebook:
        for plant in plants_dict[place]:
            tempo = plant.copy()
            tempo.insert(0, count) # location_id simulado
            rows_to_insert.append(tuple(tempo))
        count += 1

    # 5. Ejecutar
    try:
        cursor.executemany(query, rows_to_insert)
        connection.commit()
        print(f"{cursor.rowcount} plantas insertadas.")
    except Exception as e:
        print(f"Error: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    insert_plants()