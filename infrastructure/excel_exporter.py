import pandas as pd
from datetime import datetime
import os

async def save_to_excel(data, sheet_name):
    if not data:
        print("No data to export.")
        return
    date_str = datetime.now().strftime("%d%m%Y")
    file_name = f"{sheet_name}_{date_str}.xlsx"
    print(f"Saving to {file_name}")

    df = pd.DataFrame(data)
    df.to_excel(file_name, index=False, sheet_name=sheet_name)
