from typing import Optional
from ..core.tf_reader import TFReader
from ..core.contracts import MotorCandidate

class RangeMeanReversionEngine:
    engine_name = "RMR"
    
    @staticmethod
    def detect(symbol: str, ohlcv: dict) -> Optional[MotorCandidate]:
        tf_1h = TFReader.read(ohlcv["1h"], "1h")
        tf_15m = TFReader.read(ohlcv["15m"], "15m")
        
        notes = [f"1h={tf_1h['state']}", f"15m={tf_15m['state']}"]
        
        if tf_1h["state"] != "COMPRESSION":
            return None
        notes.append("✓ 1h compression")
        
        band_width = tf_1h["high_20"] - tf_1h["low_20"]
        if tf_1h["price"] < tf_1h["high_20"] - band_width * 0.1:
            return None
        notes.append("✓ upper band")
        
        if tf_15m["ema9"] >= tf_15m["ema21"]:
            return None
        notes.append("✓ 15m revert")
        
        return MotorCandidate(
            symbol=symbol,
            engine_name="RMR",
            direction="SHORT",
            entry_price=tf_15m["price"],
            invalidate=tf_1h["high_20"],
            confidence=0.65,
            tf_setup="1h compression + upper band + 15m revert",
            notes=notes,
        )
