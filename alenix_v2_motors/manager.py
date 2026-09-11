from .engines.tc import TrendContinuationEngine
from .engines.rmr import RangeMeanReversionEngine
from .engines.short import ShortDowntrendEngine

class V2MotorManager:
    engines = [
        TrendContinuationEngine,
        RangeMeanReversionEngine,
        ShortDowntrendEngine,
    ]
    
    @classmethod
    def detect_all(cls, symbol: str, ohlcv: dict) -> list:
        candidates = []
        for engine in cls.engines:
            try:
                candidate = engine.detect(symbol, ohlcv)
                if candidate:
                    candidates.append(candidate)
            except Exception as e:
                print(f"Motor {engine.engine_name} error: {e}")
        return candidates
