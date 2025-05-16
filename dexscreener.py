import requests

def fetch_pairs():
    url = "https://api.dexscreener.com/latest/dex/pairs"
    response = requests.get(url)
    return response.json().get("pairs", []) if response.status_code == 200 else []