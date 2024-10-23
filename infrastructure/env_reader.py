import os
from dotenv import load_dotenv

load_dotenv()

def get_api_url():
    return os.getenv("API_URL")

def get_api_url_param_1():
    return os.getenv("API_URL_PARAM_1")

def get_api_url_param_2():
    return os.getenv("API_URL_PARAM_2")

def get_api_username():
    return os.getenv("API_USERNAME")

def get_api_password():
    return os.getenv("API_PASSWORD")
