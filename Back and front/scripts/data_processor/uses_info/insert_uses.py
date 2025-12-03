import pandas as pd
import mysql.connector
import unicodedata
from scripts.db_connection import get_db_connection

# Importamos las funciones de procesamiento de datos
from scripts.data_processor.data_processor import (
    excel_data,
    create_dataframe_info_antonio_ante,
    create_dataframe_info_urcuqui,
    create_dataframe_info_pimampiro,
    create_dataframe_info_otavalo,
    create_dataframe_info_cotacachi,
    create_dataframe_info_ibarra
)

def normalize_text(text):
    """
    Elimina tildes y convierte a minúsculas para comparaciones más robustas.
    """
    if not isinstance(text, str):
        return str(text)
    text = text.lower().strip()
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

def get_db_mappings(cursor):
    """
    Obtiene mapas de Plantas y Ubicaciones, y calcula el siguiente ID disponible.
    """
    cursor.execute("SELECT id_plant_pk, current_name FROM plants")
    plant_map = {}
    for row in cursor.fetchall():
        id_p, name = row
        plant_map[name.strip().lower()] = id_p
        plant_map[normalize_text(name)] = id_p

    cursor.execute("SELECT id_location_pk, city_name FROM locations")
    location_map = {}
    for row in cursor.fetchall():
        id_l, city = row
        location_map[city.strip().lower()] = id_l
        location_map[normalize_text(city)] = id_l

    cursor.execute("SELECT id_plant_pk, id_location_pk FROM plants_locations")
    valid_relations = set(cursor.fetchall())
    
    cursor.execute("SELECT MAX(id_use_pk) FROM uses")
    result = cursor.fetchone()
    next_id = 1
    if result and result[0] is not None:
        next_id = result[0] + 1

    return plant_map, location_map, valid_relations, next_id

def prepare_city_data(df, city_name, plant_map, location_map, valid_relations):
    """
    Itera sobre el Excel y extrae los 3 tipos de usos posibles por cada planta.
    """
    raw_data_list = []
    
    # Normalización de la ciudad
    city_key_exact = city_name.strip().lower()
    city_key_norm = normalize_text(city_name)
    location_id = location_map.get(city_key_exact) or location_map.get(city_key_norm)

    if not location_id:
        print(f"⚠️  Advertencia: No se encontró ID para la ubicación '{city_name}'. Saltando...")
        return []

    # --- DEFINICIÓN DE COLUMNAS DE USO ---
    # Mapeo: Nombre de columna en el DF -> Nombre que irá a la base de datos (type_use)
    # Ajusta las claves (izquierda) si en tu CSV tienen mayúsculas o espacios distintos.
    use_columns_map = {
        'uso_ancestral_reportado': 'Uso Ancestral Reportado',
        'uso_ancestral_segun_fuentes_vivas': 'Uso Ancestral Según Fuentes Vivas',
        'uso_cientificamente_comprobado': 'Uso Científicamente Comprobado'
    }

    for _, row in df.iterrows():
        plant_name_raw = str(row['nombre_comun'])
        if plant_name_raw == 'nan' or not plant_name_raw.strip():
            continue
            
        p_key_exact = plant_name_raw.strip().title().lower()
        p_key_norm = normalize_text(plant_name_raw)
        plant_id = plant_map.get(p_key_exact) or plant_map.get(p_key_norm)

        if plant_id:
            # Solo procedemos si existe la relación planta-ubicación
            if (plant_id, location_id) in valid_relations:
                
                # REVISAR LAS 3 COLUMNAS DE USOS PARA ESTA FILA
                for col_csv, type_db_name in use_columns_map.items():
                    
                    # Obtenemos el valor de la celda
                    val = row.get(col_csv)
                    
                    # Verificamos si tiene contenido válido (no es NaN, ni vacío, ni '0')
                    val_str = str(val).strip()
                    if val is not None and val_str.lower() not in ['nan', '', 'none', '0']:
                        
                        raw_data_list.append({
                            'id_plant': plant_id,
                            'id_location': location_id,
                            'desc': val_str,      # La descripción es el contenido de la celda
                            'type': type_db_name  # El tipo es definido por la columna de origen
                        })
            else:
                pass # Relación no existe
                
    return raw_data_list

def insert_uses_to_db():
    connection = get_db_connection()
    if not connection:
        return

    cursor = connection.cursor()
    print("Obteniendo mapas y calculando ID inicial...")
    try:
        plant_map, location_map, valid_relations, next_id = get_db_mappings(cursor)
    except mysql.connector.Error as err:
        print(f"Error al consultar la BD: {err}")
        return

    cities_config = [
        ('Antonio Ante', create_dataframe_info_antonio_ante),
        ('Urcuquí', create_dataframe_info_urcuqui),
        ('Pimampiro', create_dataframe_info_pimampiro),
        ('Otavalo', create_dataframe_info_otavalo),
        ('Cotacachi', create_dataframe_info_cotacachi),
        ('Ibarra', create_dataframe_info_ibarra)
    ]

    print("Procesando DataFrames y extrayendo tipos de uso...")
    all_rows = []
    
    for city_name, data_func in cities_config:
        df = data_func(excel_data)
        batch = prepare_city_data(df, city_name, plant_map, location_map, valid_relations)
        all_rows.extend(batch)
        print(f" - {city_name}: {len(batch)} registros de usos extraídos.")

    if not all_rows:
        print("No hay datos para insertar.")
        return

    # Asignación de IDs incrementales
    final_data = []
    current_id = next_id
    for row in all_rows:
        final_data.append((
            current_id,
            row['id_plant'],
            row['id_location'],
            row['desc'],
            row['type']
        ))
        current_id += 1

    query = """
        INSERT INTO uses (id_use_pk, id_plant_pk, id_location_pk, description, type_use) 
        VALUES (%s, %s, %s, %s, %s)
    """

    try:
        cursor.executemany(query, final_data)
        connection.commit()
        print(f"✅ ÉXITO: Se insertaron {cursor.rowcount} registros en 'uses'.")
    except mysql.connector.Error as err:
        print(f"❌ Error al insertar datos: {err}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    insert_uses_to_db()