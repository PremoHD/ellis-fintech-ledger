import time
from tools.web_reader import fetch

def monitor_url(url, interval=60):
    while True:
        data = fetch(url)
        print(f"📡 Monitored {url}")
        time.sleep(interval)