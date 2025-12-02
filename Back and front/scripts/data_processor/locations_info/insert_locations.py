import pandas as pd

from scripts.data_processor.data_processor import excel_data
from scripts.data_processor.data_processor import create_dataframe_info_antonio_ante
from scripts.data_processor.data_processor import create_dataframe_info_cotacachi
from scripts.data_processor.data_processor import create_dataframe_info_otavalo
from scripts.data_processor.data_processor import create_dataframe_info_pimampiro
from scripts.data_processor.data_processor import create_dataframe_info_ibarra
from scripts.data_processor.data_processor import create_dataframe_info_urcuqui

Antonio_ante = create_dataframe_info_antonio_ante(excel_data)[['nombre_comun', 'nombre_cientifico']]
Urcuqui = create_dataframe_info_urcuqui(excel_data)[['ciudad', 'provincia']]
Pimampiro = create_dataframe_info_pimampiro(excel_data)[['ciudad', 'provincia']]
Otavalo= create_dataframe_info_otavalo(excel_data)[['ciudad', 'provincia']]
Cotacachi = create_dataframe_info_cotacachi(excel_data)[['ciudad', 'provincia']]
Ibarra = create_dataframe_info_ibarra(excel_data)[['ciudad', 'provincia']]

if __name__ == '__main__':
    print("Antonio Ante")
    print(Antonio_ante.head(3))
    print()
    print("Urcuqui")
    print(Urcuqui.head(3))
    print()
    print("Pimampiro")
    print(Pimampiro.head(3))
    print()
    print("Otavalo")
    print(Otavalo.head(3))
    print()
    print("Cotacachi")
    print(Cotacachi.head(3))
    print()
    print("Ibarra")
    print(Ibarra.head(3))
    print()