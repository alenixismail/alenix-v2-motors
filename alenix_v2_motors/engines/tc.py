from typing import Optional
from ..core.tf_reader import TFReader
from ..core.contracts import MotorCandidate

class TrendContinuationEngine:
    engine_name = "TC"
    
    @staticmethod
    def detect(symbol: str, ohlcv: dict) -> Optional[MotorCandidate]:
        tf_4h = TFReader.read(ohlcv["4h"], "4h")
        tf_1h = TFReader.read(ohlcv["1h"], "1h")
        tf_15m = TFReader.read(ohlcv["15m"], "15m")
        
        notes = [f"4h={tf_4h['state']}", f"1h={tf_1h['state']}", f"15m={tf_15m['state']}"]
        
        if tf_4h["state"] not in ["BULLISH_EXPANSION", "BULLISH_STACKED"]:
            return None
        notes.append("✓ 4h bullish")
        
        if tf_1h["state"] not in ["COMPRESSION", "BULLISH_STACKED"] or tf_1h["price"] >= tf_1h["ema50"]:
            return None
        notes.append("✓ 1h pullback")
        
        if tf_15m["price"] < tf_15m["ema9"]:
            return None
        notes.append("✓ 15m close > EMA9")
        
        return MotorCandidate(
            symbol=symbol,
            engine_name="TC",
            direction="LONG",
            entry_price=tf_15m["price"],
            invalidate=tf_15m["low_20"] - (tf_15m["ema21"] - tf_15m["low_20"]) * 0.5,
            confidence=0.75,
            tf_setup="4h bullish_expansion + 1h pullback + 15m close > EMA9",
            notes=notes,
        )
