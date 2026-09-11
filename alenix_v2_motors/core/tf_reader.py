from .ema import EMA

class TFReader:
    @staticmethod
    def read(ohlcv: list, tf: str) -> dict:
        closes = [x["close"] for x in ohlcv[-200:]]
        ema9 = EMA.calculate(closes, 9)
        ema21 = EMA.calculate(closes, 21)
        ema50 = EMA.calculate(closes, 50)
        ema200 = EMA.calculate(closes, 200)
        price = closes[-1]
        
        if ema9 > ema21 > ema50 > ema200:
            state = "BULLISH_EXPANSION"
        elif ema9 > ema21 > ema50 and ema50 > ema200:
            state = "BULLISH_STACKED"
        elif ema9 < ema21 < ema50 < ema200:
            state = "BEARISH_EXPANSION"
        elif ema9 < ema21 < ema50 and ema50 < ema200:
            state = "BEARISH_STACKED"
        elif (ema9 > ema200 and ema200 > ema21) or (ema9 < ema200 and ema200 < ema21):
            state = "RECLAIMING"
        else:
            state = "COMPRESSION"
        
        return {
            "tf": tf,
            "state": state,
            "ema9": ema9,
            "ema21": ema21,
            "ema50": ema50,
            "ema200": ema200,
            "price": price,
            "high_20": max([x["high"] for x in ohlcv[-20:]]),
            "low_20": min([x["low"] for x in ohlcv[-20:]]),
        }
