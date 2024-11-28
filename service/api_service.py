from infrastructure.env_reader import get_sheet_name
from infrastructure.api_implementation import APIImplementation
from infrastructure.excel_exporter import save_to_excel
from infrastructure.env_reader import (
    get_api_inc,
    get_api_inc_param_1,
    get_api_inc_param_2,
    get_api_req,
    get_api_req_param_1,
    get_api_req_param_2,
    get_api_username,
    get_api_password,
)
from mapper.field_mapper import FieldMapper

class APIService:
    def __init__(self):
        self.api_inc = APIImplementation(get_api_inc(), get_api_username(), get_api_password())
        self.api_req = APIImplementation(get_api_req(), get_api_username(), get_api_password())

    async def fetch_and_export(self, api, get_param_1, get_param_2, api_url, field_mapping_func):
        combined_data = await self.fetch_data_generic(api, get_param_1, get_param_2)
        sheet_name = self.generate_sheet_name(api_url)
        await save_to_excel(combined_data, sheet_name, field_mapping_func())
        return combined_data

    async def fetch_data_generic(self, api, get_param_1, get_param_2):
        combined_data = []
        param_1 = get_param_1
        param_2 = get_param_2

        if not param_1 and not param_2:
            data = await api.fetch_data("")
            if data:
                combined_data.extend(data.get("result", []))
        else:
            if param_1:
                data_1 = await api.fetch_data(param_1)
                if data_1:
                    combined_data.extend(data_1.get("result", []))

            if param_2:
                data_2 = await api.fetch_data(param_2)
                if data_2:
                    combined_data.extend(data_2.get("result", []))

        return combined_data

    def generate_sheet_name(self, api_url):
        last_segment = api_url.split('/')[-1].split('?')[0]
        sheet_name = f"{get_sheet_name()}_{last_segment}"
        return sheet_name

    async def fetch_data(self):
        # Dados para API INC
        combined_data_inc = await self.fetch_and_export(
            self.api_inc, get_api_inc_param_1(), get_api_inc_param_2(), get_api_inc(), FieldMapper.get_field_mapping_inc
        )

        # Dados para API REQ
        combined_data_req = await self.fetch_and_export(
            self.api_req, get_api_req_param_1(), get_api_req_param_2(), get_api_req(), FieldMapper.get_field_mapping_req
        )

        return combined_data_inc, combined_data_req