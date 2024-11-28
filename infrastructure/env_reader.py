import os
from dotenv import load_dotenv

load_dotenv()

def get_api_inc():
    inc_url = os.getenv("API_URL_INC")
    return inc_url

def get_api_inc_param_1():
    inc_param_1 = os.getenv("API_URL_INC_PARAM_1")
    return inc_param_1

def get_api_inc_param_2():
    inc_param_2 = os.getenv("API_URL_INC_PARAM_2")
    return inc_param_2

def get_api_req():
    req_url = os.getenv("API_URL_REQ")
    return req_url

def get_api_req_param_1():
    req_param_1 = os.getenv("API_URL_REQ_PARAM_1")
    return req_param_1

def get_api_req_param_2():
    req_param_2 = os.getenv("API_URL_REQ_PARAM_2")
    return req_param_2

def get_api_sla_url():
    sla_url = os.getenv("API_URL_SLA")
    return sla_url

def get_api_sla_param_1():
    sla_param_1 = os.getenv("API_URL_SLA_PARAM_1")
    return sla_param_1

def get_api_sla_param_2():
    sla_param_2 = os.getenv("API_URL_SLA_PARAM_2")
    return sla_param_2

def get_api_prob_url():
    prob_url = os.getenv("API_URL_PROB")
    return prob_url

def get_api_prob_param_1():
    prob_param_1 = os.getenv("API_URL_PROB_PARAM_1")
    return prob_param_1

def get_api_prob_param_2():
    prob_param_2 = os.getenv("API_URL_PROB_PARAM_2")
    return prob_param_2

def get_api_username():
    username = os.getenv("API_USERNAME")
    return username

def get_api_password():
    password = os.getenv("API_PASSWORD")
    return password

def get_sheet_name():
    sheet_name = os.getenv("SHEET_NAME")
    return sheet_name
