ALLOWED_DOMAINS = [
    "github.com",
    "api.coingecko.com"
]

ALLOWED_APIS = [
    "coingecko"
]

def is_domain_allowed(url):
    return any(d in url for d in ALLOWED_DOMAINS)

def is_api_allowed(api_name):
    return api_name in ALLOWED_APIS