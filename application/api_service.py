from infrastructure.env_reader import get_api_url_param_1, get_api_url_param_2

class APIService:
    def __init__(self, api):
        self.api = api

    def fetch_data(self):
        combined_data = []
        param1 = get_api_url_param_1()
        param2 = get_api_url_param_2()

        if param1:
            data1 = self.api.get_data(param1)
            if isinstance(data1, list):
                combined_data.extend(data1)
            elif isinstance(data1, dict):
                if 'result' in data1:
                    combined_data.extend(data1['result'])
                else:
                    print("Data returned is a dict but does not contain 'result' key.")
            else:
                print(f"Expected a list or dict but got: {type(data1)}")
        if param2:
            data2 = self.api.get_data(param2)
            if isinstance(data2, list):
                combined_data.extend(data2)
            elif isinstance(data2, dict):
                if 'result' in data2:
                    combined_data.extend(data2['result'])
                else:
                    print("Data returned is a dict but does not contain 'result' key.")
            else:
                print(f"Expected a list or dict but got: {type(data2)}")

        if not combined_data and not param1:
            data_base = self.api.get_data('')
            if isinstance(data_base, list):
                combined_data.extend(data_base)
            elif isinstance(data_base, dict):
                if 'result' in data_base:
                    combined_data.extend(data_base['result'])
                else:
                    print("Data returned is a dict but does not contain 'result' key.")
            else:
                print(f"Expected a list or dict but got: {type(data_base)}")

        return combined_data
