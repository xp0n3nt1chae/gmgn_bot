import requests
from config import API_KEY, TRADING_CHAIN

class GMGNTrader:
    def __init__(self):
        self.api_key = API_KEY
        self.chain = TRADING_CHAIN
        self.base_url = "https://gmgn.ai/api/trade"

    def trade(self, token_address, action="buy", amount=0.1):
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {
            "chain": self.chain,
            "token_address": token_address,
            "action": action,
            "amount": amount
        }
        r = requests.post(self.base_url, json=payload, headers=headers)
        return r.json() if r.status_code == 200 else None