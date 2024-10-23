import pandas as pd

def export_to_excel(data, sheet_name="data"):
    if not data:
        print("No data to export.")
        return

    if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        keys = data[0].keys()
        df = pd.DataFrame(data)
        file_name = f"{sheet_name}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        df.to_excel(file_name, index=False)
        print(f"Data exported successfully to {file_name}.")
    else:
        print("Invalid data format for export. Expected a list of dictionaries.")
