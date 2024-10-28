from infrastructure.env_reader import get_sheet_name
from infrastructure.api_implementation import APIImplementation
#from infrastructure.xlsx_exporter import save_to_excel
from infrastructure.excel_exporter import save_to_excel
from infrastructure.env_reader import (
    get_api_url,
    get_api_url_param_1,
    get_api_url_param_2,
    get_api_url2,
    get_api_url2_param_1,
    get_api_url2_param_2,
    get_api_username,
    get_api_password,
)
from model.field_mapper import FieldMapper

class APIService:
    def __init__(self):
        self.api1 = APIImplementation(get_api_url(), get_api_username(), get_api_password())
        self.api2 = APIImplementation(get_api_url2(), get_api_username(), get_api_password())

    async def fetch_data_from_api1(self):
        combined_data = []
        param_1 = get_api_url_param_1()
        param_2 = get_api_url_param_2()

        if not param_1 and not param_2:
            print("Fetching data from API URL1 without parameters.")
            data_1 = await self.api1.fetch_data("")
            if data_1:
                combined_data.extend(data_1.get("result", []))
        else:
            if param_1:
                print(f"Fetching data from API URL1 with param_1: {param_1}")
                data_1 = await self.api1.fetch_data(param_1)
                if data_1:
                    combined_data.extend(data_1.get("result", []))

            if param_2:
                print(f"Fetching data from API URL1 with param_2: {param_2}")
                data_2 = await self.api1.fetch_data(param_2)
                if data_2:
                    combined_data.extend(data_2.get("result", []))

        return combined_data

    async def fetch_data_from_api2(self):
        combined_data2 = []
        param2_1 = get_api_url2_param_1()
        param2_2 = get_api_url2_param_2()

        if not param2_1 and not param2_2:
            print("Fetching data from API URL2 without parameters.")
            data_3 = await self.api2.fetch_data("")
            if data_3:
                combined_data2.extend(data_3.get("result", []))
        else:
            if param2_1:
                print(f"Fetching data from API URL2 with param_1: {param2_1}")
                data_3 = await self.api2.fetch_data(param2_1)
                if data_3:
                    combined_data2.extend(data_3.get("result", []))

            if param2_2:
                print(f"Fetching data from API URL2 with param_2: {param2_2}")
                data_4 = await self.api2.fetch_data(param2_2)
                if data_4:
                    combined_data2.extend(data_4.get("result", []))

        return combined_data2

    async def fetch_data(self):
        combined_data = await self.fetch_data_from_api1()
        api1_url = get_api_url()
        last_segment_api1 = api1_url.split('/')[-1].split('?')[0]
        sheet_name_api1 = f"{get_sheet_name()}_{last_segment_api1}"
        await save_to_excel(combined_data, sheet_name_api1, FieldMapper.get_field_mapping_api1())

        combined_data2 = await self.fetch_data_from_api2()
        api2_url = get_api_url2()
        last_segment_api2 = api2_url.split('/')[-1].split('?')[0]
        sheet_name_api2 = f"{get_sheet_name()}_{last_segment_api2}"
        await save_to_excel(combined_data2, sheet_name_api2, FieldMapper.get_field_mapping_api2())

        return combined_data, combined_data2