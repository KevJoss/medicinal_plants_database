import pandas as pd
import os

current_script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(
    current_script_dir, 
    '..', '..', '..',   
    'Data_cleaning',    
    'Proyecto plantas medicinales_test.xlsx' 
)

file_path = os.path.normpath(file_path)

# Read the excel file with plants information
excel_data = pd.ExcelFile(file_path)

def create_dataframe_info_antonio_ante(excel_data):
    urcuqui_ante_excel_dataframe = pd.read_excel(excel_data, sheet_name='Antonio Ante')
    antonio_ante_columns_general_info_db = ['nombre_comun']

    antonio_ante_nombre_comun_data = urcuqui_ante_excel_dataframe.loc[1:, 'Nombre Común ']
    antonio_ante_nombre_cientifico_data = urcuqui_ante_excel_dataframe.loc[1:, 'Nombre Científico']
    antonio_ante_uso_ancestral_reportado = urcuqui_ante_excel_dataframe.loc[1:, 'Uso']
    antonio_ante_uso_ancestral_fuentes_vivas = urcuqui_ante_excel_dataframe.loc[1:, 'Unnamed: 5']
    antonio_ante_uso_comprobado = urcuqui_ante_excel_dataframe.loc[1:, 'Unnamed: 6']
    antonio_ante_origen = urcuqui_ante_excel_dataframe.loc[1:, 'Toponimo ']
    antonio_ante_distribucion = urcuqui_ante_excel_dataframe.loc[1:, 'Información de procedencia (De donde lo traen, o si es cultivo propio)']
    antonio_ante_distribucion_comercial = urcuqui_ante_excel_dataframe.loc[1:, 'Lugar de distribución']
    antonio_ante_referencia_1 = urcuqui_ante_excel_dataframe.loc[1:, 'Investigaciones previas']
    antonio_ante_referencia_2 = urcuqui_ante_excel_dataframe.loc[1:, 'Unnamed: 11']
    antonio_ante_referencia_3 = urcuqui_ante_excel_dataframe.loc[1:, 'Unnamed: 12']
    
    antonio_ante_dataframe = pd.DataFrame(data=list(antonio_ante_nombre_comun_data), columns=antonio_ante_columns_general_info_db)

    antonio_ante_dataframe['nombre_cientifico'] = list(antonio_ante_nombre_cientifico_data)
    antonio_ante_dataframe['ciudad'] = ["Antonio Ante"] * len(antonio_ante_dataframe)
    antonio_ante_dataframe['provincia'] = ["Imbabura"] * len(antonio_ante_dataframe)
    antonio_ante_dataframe['origen'] = list(antonio_ante_origen)
    antonio_ante_dataframe['distribucion'] = list(antonio_ante_distribucion)
    antonio_ante_dataframe['distribucion_comercial'] = list(antonio_ante_distribucion_comercial)
    antonio_ante_dataframe['uso_ancestral_reportado'] = list(antonio_ante_uso_ancestral_reportado)
    antonio_ante_dataframe['uso_ancestral_segun_fuentes_vivas'] = list(antonio_ante_uso_ancestral_fuentes_vivas)
    antonio_ante_dataframe['uso_cientificamente_comprobado'] = list(antonio_ante_uso_comprobado)
    antonio_ante_dataframe['referencia_1'] = list(antonio_ante_referencia_1)
    antonio_ante_dataframe['referencia_2'] = list(antonio_ante_referencia_2)
    antonio_ante_dataframe['referencia_3'] = list(antonio_ante_referencia_3)
    
    return antonio_ante_dataframe


def create_dataframe_info_urcuqui(excel_data):
    urcuqui_ante_excel_dataframe = pd.read_excel(excel_data, sheet_name='Urcuquí')
    urcuqui_columns_general_info_db = ['nombre_comun']

    urcuqui_nombre_comun_data = urcuqui_ante_excel_dataframe.loc[1:, 'Nombre Común ']
    urcuqui_nombre_cientifico_data = urcuqui_ante_excel_dataframe.loc[1:, 'Nombre Científico']
    urcuqui_uso_ancestral_reportado = urcuqui_ante_excel_dataframe.loc[1:, 'Uso']
    urcuqui_uso_ancestral_fuentes_vivas = urcuqui_ante_excel_dataframe.loc[1:, 'Unnamed: 5']
    urcuqui_uso_comprobado = urcuqui_ante_excel_dataframe.loc[1:, 'Unnamed: 6']
    urcuqui_origen = urcuqui_ante_excel_dataframe.loc[1:, 'Topónimo del Sitio de Cultivo ']
    urcuqui_distribucion = urcuqui_ante_excel_dataframe.loc[1:, 'Información de procedencia (De donde lo traen, o si es cultivo propio)']
    urcuqui_distribucion_comercial = urcuqui_ante_excel_dataframe.loc[1:, 'Habitad (Mercado de Ibarra)']
    urcuqui_referencia_1 = urcuqui_ante_excel_dataframe.loc[1:, 'Investigaciones previas']
    urcuqui_referencia_2 = urcuqui_ante_excel_dataframe.loc[1:, 'Unnamed: 11']
    urcuqui_referencia_3 = urcuqui_ante_excel_dataframe.loc[1:, 'Unnamed: 12']
    
    urcuqui_dataframe = pd.DataFrame(data=list(urcuqui_nombre_comun_data), columns=urcuqui_columns_general_info_db)

    urcuqui_dataframe['nombre_cientifico'] = list(urcuqui_nombre_cientifico_data)
    urcuqui_dataframe['ciudad'] = ["Urcuqui"] * len(urcuqui_dataframe)
    urcuqui_dataframe['provincia'] = ["Imbabura"] * len(urcuqui_dataframe)
    urcuqui_dataframe['origen'] = list(urcuqui_origen)
    urcuqui_dataframe['distribucion'] = list(urcuqui_distribucion)
    urcuqui_dataframe['distribucion_comercial'] = list(urcuqui_distribucion_comercial)
    urcuqui_dataframe['uso_ancestral_reportado'] = list(urcuqui_uso_ancestral_reportado)
    urcuqui_dataframe['uso_ancestral_segun_fuentes_vivas'] = list(urcuqui_uso_ancestral_fuentes_vivas)
    urcuqui_dataframe['uso_cientificamente_comprobado'] = list(urcuqui_uso_comprobado)
    urcuqui_dataframe['referencia_1'] = list(urcuqui_referencia_1)
    urcuqui_dataframe['referencia_2'] = list(urcuqui_referencia_2)
    urcuqui_dataframe['referencia_3'] = list(urcuqui_referencia_3)
    
    return urcuqui_dataframe

def create_dataframe_info_pimampiro(excel_data):
    pimampiro_ante_excel_dataframe = pd.read_excel(excel_data, sheet_name='Pimampiro')
    pimampiro_columns_general_info_db = ['nombre_comun']

    pimampiro_nombre_comun_data = pimampiro_ante_excel_dataframe.loc[1:, 'Nombre Común ']
    pimampiro_nombre_cientifico_data = pimampiro_ante_excel_dataframe.loc[1:, 'Nombre Científico']
    pimampiro_uso_ancestral_reportado = pimampiro_ante_excel_dataframe.loc[1:, 'Uso']
    pimampiro_uso_ancestral_fuentes_vivas = pimampiro_ante_excel_dataframe.loc[1:, 'Unnamed: 5']
    pimampiro_uso_comprobado = pimampiro_ante_excel_dataframe.loc[1:, 'Unnamed: 6']
    pimampiro_origen = pimampiro_ante_excel_dataframe.loc[1:, 'Toponimo ']
    pimampiro_distribucion = pimampiro_ante_excel_dataframe.loc[1:, 'Información de procedencia (De donde lo traen, o si es cultivo propio)']
    pimampiro_distribucion_comercial = pimampiro_ante_excel_dataframe.loc[1:, 'Lugar de distribución']
    pimampiro_referencia_1 = pimampiro_ante_excel_dataframe.loc[1:, 'Investigaciones previas']
    pimampiro_referencia_2 = pimampiro_ante_excel_dataframe.loc[1:, 'Unnamed: 11']
    pimampiro_referencia_3 = pimampiro_ante_excel_dataframe.loc[1:, 'Unnamed: 12']
    
    pimampiro_dataframe = pd.DataFrame(data=list(pimampiro_nombre_comun_data), columns=pimampiro_columns_general_info_db)

    pimampiro_dataframe['nombre_cientifico'] = list(pimampiro_nombre_cientifico_data)
    pimampiro_dataframe['ciudad'] = ["Pimampiro"] * len(pimampiro_dataframe)
    pimampiro_dataframe['provincia'] = ["Imbabura"] * len(pimampiro_dataframe)
    pimampiro_dataframe['origen'] = list(pimampiro_origen)
    pimampiro_dataframe['distribucion'] = list(pimampiro_distribucion)
    pimampiro_dataframe['distribucion_comercial'] = list(pimampiro_distribucion_comercial)
    pimampiro_dataframe['uso_ancestral_reportado'] = list(pimampiro_uso_ancestral_reportado)
    pimampiro_dataframe['uso_ancestral_segun_fuentes_vivas'] = list(pimampiro_uso_ancestral_fuentes_vivas)
    pimampiro_dataframe['uso_cientificamente_comprobado'] = list(pimampiro_uso_comprobado)
    pimampiro_dataframe['referencia_1'] = list(pimampiro_referencia_1)
    pimampiro_dataframe['referencia_2'] = list(pimampiro_referencia_2)
    pimampiro_dataframe['referencia_3'] = list(pimampiro_referencia_3)
    
    return pimampiro_dataframe

def create_dataframe_info_otavalo(excel_data):
    otavalo_ante_excel_dataframe = pd.read_excel(excel_data, sheet_name='Otavalo')
    otavalo_columns_general_info_db = ['nombre_comun']

    otavalo_nombre_comun_data = otavalo_ante_excel_dataframe.loc[1:, 'Nombre Común ']
    otavalo_nombre_cientifico_data = otavalo_ante_excel_dataframe.loc[1:, 'Nombre Científico']
    otavalo_uso_ancestral_reportado = otavalo_ante_excel_dataframe.loc[1:, 'Uso']
    otavalo_uso_ancestral_fuentes_vivas = otavalo_ante_excel_dataframe.loc[1:, 'Unnamed: 5']
    otavalo_uso_comprobado = otavalo_ante_excel_dataframe.loc[1:, 'Unnamed: 6']
    otavalo_origen = otavalo_ante_excel_dataframe.loc[1:, 'Topónimo del Sitio de Cultivo']
    otavalo_distribucion = otavalo_ante_excel_dataframe.loc[1:, 'Información de procedencia (De donde lo traen, o si es cultivo propio)']
    otavalo_distribucion_comercial = otavalo_ante_excel_dataframe.loc[1:, 'Lugar de distribución']
    otavalo_referencia_1 = otavalo_ante_excel_dataframe.loc[1:, 'Investigaciones previas']
    otavalo_referencia_2 = otavalo_ante_excel_dataframe.loc[1:, 'Unnamed: 11']
    otavalo_referencia_3 = otavalo_ante_excel_dataframe.loc[1:, 'Unnamed: 12']
    
    otavalo_dataframe = pd.DataFrame(data=list(otavalo_nombre_comun_data), columns=otavalo_columns_general_info_db)

    otavalo_dataframe['nombre_cientifico'] = list(otavalo_nombre_cientifico_data)
    otavalo_dataframe['ciudad'] = ["Otavalo"] * len(otavalo_dataframe)
    otavalo_dataframe['provincia'] = ["Imbabura"] * len(otavalo_dataframe)
    otavalo_dataframe['origen'] = list(otavalo_origen)
    otavalo_dataframe['distribucion'] = list(otavalo_distribucion)
    otavalo_dataframe['distribucion_comercial'] = list(otavalo_distribucion_comercial)
    otavalo_dataframe['uso_ancestral_reportado'] = list(otavalo_uso_ancestral_reportado)
    otavalo_dataframe['uso_ancestral_segun_fuentes_vivas'] = list(otavalo_uso_ancestral_fuentes_vivas)
    otavalo_dataframe['uso_cientificamente_comprobado'] = list(otavalo_uso_comprobado)
    otavalo_dataframe['referencia_1'] = list(otavalo_referencia_1)
    otavalo_dataframe['referencia_2'] = list(otavalo_referencia_2)
    otavalo_dataframe['referencia_3'] = list(otavalo_referencia_3)
    
    return otavalo_dataframe

def create_dataframe_info_cotacachi(excel_data):
    urcuqui_ante_excel_dataframe = pd.read_excel(excel_data, sheet_name='Cotacachi')
    cotacachi_columns_general_info_db = ['nombre_comun']

    cotacachi_nombre_comun_data = urcuqui_ante_excel_dataframe.loc[1:, 'Nombre Común ']
    cotacachi_nombre_cientifico_data = urcuqui_ante_excel_dataframe.loc[1:, 'Nombre Científico']
    cotacachi_uso_ancestral_reportado = urcuqui_ante_excel_dataframe.loc[1:, 'Usos']
    cotacachi_uso_ancestral_fuentes_vivas = urcuqui_ante_excel_dataframe.loc[1:, 'Unnamed: 5']
    cotacachi_uso_comprobado = urcuqui_ante_excel_dataframe.loc[1:, 'Unnamed: 6']
    cotacachi_origen = urcuqui_ante_excel_dataframe.loc[1:, 'Topónimo del Sitio de Cultivo']
    cotacachi_distribucion = urcuqui_ante_excel_dataframe.loc[1:, 'Información de procedencia (De donde lo traen, o si es cultivo propio)']
    cotacachi_distribucion_comercial = urcuqui_ante_excel_dataframe.loc[1:, 'Lugar de distribución']
    cotacachi_referencia_1 = urcuqui_ante_excel_dataframe.loc[1:, 'Investigaciones previas']
    cotacachi_referencia_2 = urcuqui_ante_excel_dataframe.loc[1:, 'Unnamed: 11']
    cotacachi_referencia_3 = urcuqui_ante_excel_dataframe.loc[1:, 'Unnamed: 12']
    
    cotacachi_dataframe = pd.DataFrame(data=list(cotacachi_nombre_comun_data), columns=cotacachi_columns_general_info_db)

    cotacachi_dataframe['nombre_cientifico'] = list(cotacachi_nombre_cientifico_data)
    cotacachi_dataframe['ciudad'] = ["Cotacachi"] * len(cotacachi_dataframe)
    cotacachi_dataframe['provincia'] = ["Imbabura"] * len(cotacachi_dataframe)
    cotacachi_dataframe['origen'] = list(cotacachi_origen)
    cotacachi_dataframe['distribucion'] = list(cotacachi_distribucion)
    cotacachi_dataframe['distribucion_comercial'] = list(cotacachi_distribucion_comercial)
    cotacachi_dataframe['uso_ancestral_reportado'] = list(cotacachi_uso_ancestral_reportado)
    cotacachi_dataframe['uso_ancestral_segun_fuentes_vivas'] = list(cotacachi_uso_ancestral_fuentes_vivas)
    cotacachi_dataframe['uso_cientificamente_comprobado'] = list(cotacachi_uso_comprobado)
    cotacachi_dataframe['referencia_1'] = list(cotacachi_referencia_1)
    cotacachi_dataframe['referencia_2'] = list(cotacachi_referencia_2)
    cotacachi_dataframe['referencia_3'] = list(cotacachi_referencia_3)
    
    return cotacachi_dataframe

def create_dataframe_info_ibarra(excel_data):
    ibarra_excel_dataframe = pd.read_excel(excel_data, sheet_name='Ibarra')
    ibarra_columns_general_info_db = ['nombre_comun']

    ibarra_nombre_comun_data = ibarra_excel_dataframe.loc[1:, 'Nombre Común ']
    ibarra_nombre_cientifico_data = ibarra_excel_dataframe.loc[1:, 'Nombre Científico']
    ibarra_uso_ancestral_reportado = ibarra_excel_dataframe.loc[1:, 'Uso']
    ibarra_uso_ancestral_fuentes_vivas = ibarra_excel_dataframe.loc[1:, 'Unnamed: 5']
    ibarra_uso_comprobado = ibarra_excel_dataframe.loc[1:, 'Unnamed: 6']
    ibarra_origen = ibarra_excel_dataframe.loc[1:, 'Topónimo del Sitio de Cultivo']
    ibarra_distribucion = ibarra_excel_dataframe.loc[1:, 'Lugar de distribución']
    ibarra_distribucion_comercial = ibarra_excel_dataframe.loc[1:, 'Información de procedencia ']
    ibarra_referencia_1 = ibarra_excel_dataframe.loc[1:, 'Investigaciones Previas']
    ibarra_referencia_2 = ibarra_excel_dataframe.loc[1:, 'Unnamed: 11']
    ibarra_referencia_3 = ibarra_excel_dataframe.loc[1:, 'Unnamed: 12']
    
    ibarra_dataframe = pd.DataFrame(data=list(ibarra_nombre_comun_data), columns=ibarra_columns_general_info_db)

    ibarra_dataframe['nombre_cientifico'] = list(ibarra_nombre_cientifico_data)
    ibarra_dataframe['ciudad'] = ["Ibarra"] * len(ibarra_dataframe)
    ibarra_dataframe['provincia'] = ["Imbabura"] * len(ibarra_dataframe)
    ibarra_dataframe['origen'] = list(ibarra_origen)
    ibarra_dataframe['distribucion'] = list(ibarra_distribucion)
    ibarra_dataframe['distribucion_comercial'] = list(ibarra_distribucion_comercial)
    ibarra_dataframe['uso_ancestral_reportado'] = list(ibarra_uso_ancestral_reportado)
    ibarra_dataframe['uso_ancestral_segun_fuentes_vivas'] = list(ibarra_uso_ancestral_fuentes_vivas)
    ibarra_dataframe['uso_cientificamente_comprobado'] = list(ibarra_uso_comprobado)
    ibarra_dataframe['referencia_1'] = list(ibarra_referencia_1)
    ibarra_dataframe['referencia_2'] = list(ibarra_referencia_2)
    ibarra_dataframe['referencia_3'] = list(ibarra_referencia_3)
    
    return ibarra_dataframe

# if __name__ == '__main__':
#     pass
    

