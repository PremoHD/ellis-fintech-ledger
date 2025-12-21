from tools.web_reader import fetch
from core.online_guard import allow_online_action

def run(url):
    allow_online_action("web research")
    return fetch(url)