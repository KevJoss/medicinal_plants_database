import pandas as pd
import mysql.connector
from scripts.db_connection import get_db_connection

# Importamos las funciones de procesamiento de datos y el objeto excel_data
from scripts.data_processor.data_processor import (
    excel_data,
    create_dataframe_info_antonio_ante,
    create_dataframe_info_urcuqui,
    create_dataframe_info_pimampiro,
    create_dataframe_info_otavalo,
    create_dataframe_info_cotacachi,
    create_dataframe_info_ibarra
)

def get_unique_plants_dataframe():
    """
    Recopila los dataframes de todas las ciudades, los concatena 
    y filtra para obtener plantas únicas basándose en el nombre común.
    """
    print("Procesando datos del Excel...")
    
    # 1. Obtener DataFrames de cada ciudad
    df_antonio = create_dataframe_info_antonio_ante(excel_data)
    df_urcuqui = create_dataframe_info_urcuqui(excel_data)
    df_pimampiro = create_dataframe_info_pimampiro(excel_data)
    df_otavalo = create_dataframe_info_otavalo(excel_data)
    df_cotacachi = create_dataframe_info_cotacachi(excel_data)
    df_ibarra = create_dataframe_info_ibarra(excel_data)

    # 2. Concatenar todos en uno solo
    all_plants_df = pd.concat([
        df_antonio, df_urcuqui, df_pimampiro, df_otavalo, df_cotacachi, df_ibarra
    ], ignore_index=True)

    # 3. Seleccionar solo las columnas necesarias para la tabla 'plants'
    # Según models.py: current_name, scientific_name
    # En el dataframe son: 'nombre_comun', 'nombre_cientifico'
    plants_subset = all_plants_df[['nombre_comun', 'nombre_cientifico']].copy()

    # 4. Limpieza básica (quitar espacios en blanco extra)
    plants_subset['nombre_comun'] = plants_subset['nombre_comun'].astype(str).str.strip().str.title()
    plants_subset['nombre_cientifico'] = plants_subset['nombre_cientifico'].astype(str).str.strip()

    # 5. Eliminar duplicados basados en 'nombre_comun'
    # Mantenemos el primero que encuentre.
    unique_plants = plants_subset.drop_duplicates(subset=['nombre_comun'])
    
    # Filtrar valores vacíos o 'Nan' convertidos a string
    unique_plants = unique_plants[unique_plants['nombre_comun'] != 'Nan']
    unique_plants = unique_plants[unique_plants['nombre_comun'] != '']

    print(f"Se encontraron {len(unique_plants)} plantas únicas.")
    return unique_plants

def insert_plants_to_db():
    """
    Inserta las plantas únicas en la base de datos MySQL.
    """
    # 1. Obtener datos limpios
    df_plants = get_unique_plants_dataframe()
    
    # 2. Conectar a la base de datos
    connection = get_db_connection()
    if not connection:
        print("No se pudo establecer conexión con la base de datos.")
        return

    cursor = connection.cursor()

    # 3. Query SQL
    # Usamos INSERT IGNORE para que si el 'current_name' ya existe (por la restricción UNIQUE),
    # simplemente ignore ese registro y continúe sin dar error.
    query = """
        INSERT IGNORE INTO plants (current_name, scientific_name) 
        VALUES (%s, %s)
    """

    # 4. Preparar los datos como lista de tuplas
    data_to_insert = []
    for index, row in df_plants.iterrows():
        data_to_insert.append((row['nombre_comun'], row['nombre_cientifico']))

    # 5. Ejecutar inserción masiva
    try:
        cursor.executemany(query, data_to_insert)
        connection.commit()
        print(f"Operación completada. {cursor.rowcount} nuevos registros insertados en la tabla 'plants'.")
    except mysql.connector.Error as err:
        print(f"Error al insertar datos: {err}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    insert_plants_to_db()