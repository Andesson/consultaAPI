import os
from dotenv import load_dotenv

load_dotenv()

def get_api_url():
    url = os.getenv("API_URL")
    print(f"API URL: {url}")
    return url

def get_api_url_param_1():
    param_1 = os.getenv("API_URL_PARAM_1")
    print(f"API URL Param 1: {param_1}")
    return param_1

def get_api_url_param_2():
    param_2 = os.getenv("API_URL_PARAM_2")
    print(f"API URL Param 2: {param_2}")
    return param_2

def get_api_url2():
    url2 = os.getenv("API_URL2")
    print(f"API URL 2: {url2}")
    return url2

def get_api_url2_param_1():
    param_2_1 = os.getenv("API_URL2_PARAM_1")
    print(f"API URL 2 Param 1: {param_2_1}")
    return param_2_1

def get_api_url2_param_2():
    param_2_2 = os.getenv("API_URL2_PARAM_2")
    print(f"API URL 2 Param 2: {param_2_2}")
    return param_2_2

def get_api_username():
    username = os.getenv("API_USERNAME")
    return username

def get_api_password():
    password = os.getenv("API_PASSWORD")
    return password

def get_sheet_name():
    sheet_name = os.getenv("SHEET_NAME")
    return sheet_name
