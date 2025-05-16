import numpy as np

class TrendAnalyzer:
    def __init__(self, prices):
        self.prices = prices

    def calculate_trend(self):
        if len(self.prices) < 2:
            return "Neutral"
        change = ((self.prices[-1] - self.prices[0]) / self.prices[0]) * 100
        if change > 5:
            return "Bullish"
        elif change < -5:
            return "Bearish"
        else:
            return "Neutral"