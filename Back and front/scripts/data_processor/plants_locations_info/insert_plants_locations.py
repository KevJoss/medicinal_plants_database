import pandas as pd
import mysql.connector
from scripts.db_connection import get_db_connection

# Importamos las funciones y la data del procesador
from scripts.data_processor.data_processor import (
    excel_data,
    create_dataframe_info_antonio_ante,
    create_dataframe_info_urcuqui,
    create_dataframe_info_pimampiro,
    create_dataframe_info_otavalo,
    create_dataframe_info_cotacachi,
    create_dataframe_info_ibarra
)

def get_all_relationships_dataframe():
    """
    Obtiene un DataFrame gigante con todas las filas del Excel,
    manteniendo la columna 'nombre_comun' y 'ciudad'.
    """
    print("Procesando relaciones Planta-Ubicación desde Excel...")
    
    df_antonio = create_dataframe_info_antonio_ante(excel_data)
    df_urcuqui = create_dataframe_info_urcuqui(excel_data)
    df_pimampiro = create_dataframe_info_pimampiro(excel_data)
    df_otavalo = create_dataframe_info_otavalo(excel_data)
    df_cotacachi = create_dataframe_info_cotacachi(excel_data)
    df_ibarra = create_dataframe_info_ibarra(excel_data)

    # Concatenamos todo
    full_df = pd.concat([
        df_antonio, df_urcuqui, df_pimampiro, df_otavalo, df_cotacachi, df_ibarra
    ], ignore_index=True)

    # Seleccionamos solo lo que nos importa para la relación
    rel_df = full_df[['nombre_comun', 'ciudad']].copy()

    # Limpieza idéntica a insert_plants.py para asegurar coincidencias
    rel_df['nombre_comun'] = rel_df['nombre_comun'].astype(str).str.strip().str.title()
    rel_df['ciudad'] = rel_df['ciudad'].astype(str).str.strip()

    # Filtrar vacíos
    rel_df = rel_df[rel_df['nombre_comun'] != 'Nan']
    rel_df = rel_df[rel_df['nombre_comun'] != '']

    # Eliminamos duplicados exactos (misma planta en misma ciudad)
    rel_df = rel_df.drop_duplicates()

    return rel_df

def get_id_maps(cursor):
    """
    Crea diccionarios para traducir Nombres a IDs consultando la base de datos.
    Retorna: (mapa_plantas, mapa_ubicaciones)
    Ej: ({'Manzanilla': 1, ...}, {'Ibarra': 5, ...})
    """
    # 1. Mapa de Plantas
    cursor.execute("SELECT id_plant_pk, current_name FROM plants")
    plants_rows = cursor.fetchall()
    # Diccionario: Clave=Nombre, Valor=ID
    plants_map = {name: pk for pk, name in plants_rows}

    # 2. Mapa de Ubicaciones
    cursor.execute("SELECT id_location_pk, city_name FROM locations")
    locations_rows = cursor.fetchall()
    locations_map = {name: pk for pk, name in locations_rows}

    return plants_map, locations_map

def seed_plants_locations():
    connection = get_db_connection()
    if not connection:
        return

    cursor = connection.cursor()
    
    try:
        # 1. Obtener datos del Excel
        df_relationships = get_all_relationships_dataframe()
        
        # 2. Obtener IDs actuales de la BD
        print("Obteniendo IDs de la base de datos...")
        plants_map, locations_map = get_id_maps(cursor)

        # 3. Preparar lista de tuplas (id_plant, id_location)
        data_to_insert = []
        
        print("Mapeando nombres a IDs...")
        for index, row in df_relationships.iterrows():
            plant_name = row['nombre_comun']
            city_name = row['ciudad']

            plant_id = plants_map.get(plant_name)
            location_id = locations_map.get(city_name)

            # Solo agregamos si encontramos ambos IDs (integridad referencial)
            if plant_id and location_id:
                data_to_insert.append((plant_id, location_id))
            else:
                # Opcional: Imprimir advertencias si algo no cruza
                print(f"Advertencia: No se encontró ID para {plant_name} en {city_name}")
                pass

        # 4. Insertar en la tabla intermedia
        # Usamos INSERT IGNORE para evitar errores si corres el script dos veces
        query = """
        INSERT IGNORE INTO plants_locations (id_plant_pk, id_location_pk)
        VALUES (%s, %s)
        """

        if data_to_insert:
            cursor.executemany(query, data_to_insert)
            connection.commit()
            print(f"¡Éxito! Se insertaron/vincularon {cursor.rowcount} relaciones planta-ubicación.")
        else:
            print("No se encontraron datos nuevos para insertar.")

    except mysql.connector.Error as err:
        print(f"Error en la base de datos: {err}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    seed_plants_locations()