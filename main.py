from application.api_service import APIService
from infrastructure.excel_exporter import export_to_excel
from infrastructure.api_implementation import APIImplementation
from infrastructure.env_reader import get_api_url, get_api_url_param_1, get_api_url_param_2, get_api_username , get_api_password

def main():
    base_url = get_api_url()
    if not base_url:
        print("Base URL is not configured. Exiting...")
        return
    username = get_api_username()
    password = get_api_password()
    api = APIImplementation(base_url, username, password)
    
    service = APIService(api)
    data = service.fetch_data()
    
    if data:
        export_to_excel(data)
    else:
        print("No data to export.")

if __name__ == "__main__":
    main()
