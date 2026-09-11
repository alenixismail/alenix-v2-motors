class EMA:
    @staticmethod
    def calculate(closes: list, period: int) -> float:
        if len(closes) < period:
            return closes[-1]
        ema = closes[0]
        multiplier = 2 / (period + 1)
        for close in closes[1:]:
            ema = close * multiplier + ema * (1 - multiplier)
        return ema
