import requests
from core.permissions import is_domain_allowed

def fetch(url):
    if not is_domain_allowed(url):
        raise Exception("❌ Domain not allowed")

    r = requests.get(url, timeout=10)
    return r.text[:5000]  # hard limit