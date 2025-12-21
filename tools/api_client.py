import requests
from core.permissions import is_api_allowed

def call(api_name, endpoint):
    if not is_api_allowed(api_name):
        raise Exception("❌ API not allowed")

    r = requests.get(endpoint, timeout=10)
    return r.json()