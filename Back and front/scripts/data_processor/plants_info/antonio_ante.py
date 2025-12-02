import pandas as pd
from scripts.data_processor import excel_data, general_info_db
antonio_ante_columns_general_info_db = ['nombre_comun']

antonio_ante_excel_dataframe = pd.read_excel(excel_data, sheet_name='Antonio Ante')

antonio_ante_nombre_comun_data = antonio_ante_excel_dataframe.loc[1:, 'Nombre Común ']
antonio_ante_nombre_cientifico_data = antonio_ante_excel_dataframe.loc[1:, 'Nombre Científico']
antonio_ante_toponimo_data = antonio_ante_excel_dataframe.loc[1:, 'Toponimo ']
urcuqui_informacion_procedencia_data = antonio_ante_excel_dataframe.loc[1:, 'Información de procedencia (De donde lo traen, o si es cultivo propio)']
antonio_ante_lugar_distribucion_data = antonio_ante_excel_dataframe.loc[1:, 'Lugar de distribución']

antonio_ante_dataframe_general_info_db = pd.DataFrame(data=list(antonio_ante_nombre_comun_data), columns=antonio_ante_columns_general_info_db)

antonio_ante_dataframe_general_info_db['nombre_cientifico'] = list(antonio_ante_nombre_cientifico_data)
antonio_ante_dataframe_general_info_db['toponimo'] = list(antonio_ante_toponimo_data)
antonio_ante_dataframe_general_info_db['informacion_procedencia'] = list(urcuqui_informacion_procedencia_data)
antonio_ante_dataframe_general_info_db['lugar_distribucion'] = list(antonio_ante_lugar_distribucion_data)

general_info_db['antonio_ante'] = antonio_ante_dataframe_general_info_db

if __name__ == "__main__":
    
    print(general_info_db['antonio_ante'].head(5))