import time
from datetime import datetime
from config import *
from dexscreener import fetch_pairs
from gmgn_trader import GMGNTrader
from trend_analyzer import TrendAnalyzer
from utils import get_rugcheck_url, get_bubblemaps_url
from database import log_token

def mock_fetch_prices():  # Replace with real price history fetch
    return [1.0, 1.05, 1.08, 1.1]

def run_bot():
    trader = GMGNTrader()
    while True:
        print("Fetching token list...")
        pairs = fetch_pairs()
        for pair in pairs:
            try:
                token_address = pair["baseToken"]["address"]
                chain = pair["chainId"]
                market_cap = float(pair.get("fdv", 0))
                volume = float(pair.get("volume", {}).get("h1", 0))
                age_minutes = (datetime.utcnow() - datetime.utcfromtimestamp(pair["pairCreatedAt"] / 1000)).total_seconds() / 60
                holders = int(pair.get("holders", 0))
                pair_name = pair.get("pairName")
                price = float(pair.get("priceUsd", 0))

                if market_cap >= MIN_MARKET_CAP and volume >= MIN_VOLUME_1H and age_minutes >= MIN_AGE_MINUTES and holders >= MIN_HOLDERS:
                    prices = mock_fetch_prices()  # Replace this with real data
                    trend = TrendAnalyzer(prices).calculate_trend()

                    rug_url = get_rugcheck_url(chain, token_address)
                    bubble_url = get_bubblemaps_url(chain, token_address)

                    if trend == "Bullish":
                        print(f"Buying {pair_name} - {trend}")
                        trader.trade(token_address, "buy", TRADE_AMOUNT)

                    log_token((datetime.utcnow().isoformat(), pair_name, chain, price, trend, rug_url, bubble_url))

            except Exception as e:
                print("Error:", e)
        time.sleep(240)

if __name__ == "__main__":
    run_bot()