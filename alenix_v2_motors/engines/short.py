from typing import Optional
from ..core.tf_reader import TFReader
from ..core.contracts import MotorCandidate

class ShortDowntrendEngine:
    engine_name = "SHORT"
    
    @staticmethod
    def detect(symbol: str, ohlcv: dict) -> Optional[MotorCandidate]:
        tf_4h = TFReader.read(ohlcv["4h"], "4h")
        tf_1h = TFReader.read(ohlcv["1h"], "1h")
        
        notes = [f"4h={tf_4h['state']}", f"1h={tf_1h['state']}"]
        
        if tf_4h["state"] not in ["BEARISH_EXPANSION", "BEARISH_STACKED"] or tf_4h["ema9"] >= tf_4h["ema200"]:
            return None
        notes.append("✓ 4h downtrend")
        
        if tf_4h["price"] < tf_4h["high_20"] * 0.95:
            return None
        notes.append("✓ bounce")
        
        if tf_1h["ema9"] > tf_1h["ema21"]:
            return None
        notes.append("✓ 1h bearish")
        
        return MotorCandidate(
            symbol=symbol,
            engine_name="SHORT",
            direction="SHORT",
            entry_price=tf_1h["price"],
            invalidate=tf_4h["high_20"] + (tf_4h["ema21"] - tf_4h["low_20"]) * 0.5,
            confidence=0.70,
            tf_setup="4h downtrend + 4h bounce + 1h sell test",
            notes=notes,
        )
