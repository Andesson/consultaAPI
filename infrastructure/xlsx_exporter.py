import xlwt
from datetime import datetime

async def save_to_excel(data, sheet_name):
    if not data:
        print("No data to export.")
        return

    date_str = datetime.now().strftime("%d%m%Y")
    file_name = f"{sheet_name}_{date_str}.xls"
    print(f"Saving to {file_name}")

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheet_name)
    headers = data[0].keys()
    for col_num, header in enumerate(headers):
        sheet.write(0, col_num, header)
        
    for row_num, entry in enumerate(data, start=1):
        for col_num, (key, value) in enumerate(entry.items()):
            sheet.write(row_num, col_num, value)

    workbook.save(file_name)
    print(f"Dados salvos no arquivo: {file_name}")
