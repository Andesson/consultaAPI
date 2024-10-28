from pyexcelerate import Workbook
from datetime import datetime

async def save_to_excel(data, sheet_name, field_mapping):
    if not data:
        print("No data to export.")
        return
    try:
        unique_data = {entry['number']: entry for entry in data}.values()
        data = list(unique_data)

        date_str = datetime.now().strftime("%d%m%Y")
        file_name = f"{sheet_name}_{date_str}.xls"
        print(f"Saving to {file_name}")

        headers = list(field_mapping.values())
        rows = [[entry.get(field, "") for field in field_mapping.keys()] for entry in data]
        data_for_excel = [headers] + rows

        wb = Workbook()
        wb.new_sheet(sheet_name, data=data_for_excel)
        wb.save(file_name)

        print(f"Dados salvos no arquivo: {file_name}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo {file_name}: {e}")
