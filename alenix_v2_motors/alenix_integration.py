"""
Alenix Integration - V2 Motors as native engine
"""

from .manager import V2MotorManager
from .core.contracts import MotorCandidate

class V2MotorsIntegrationEngine:
    """Alenix-compatible V2Motors wrapper"""
    
    @staticmethod
    def detect_all(symbol: str, ohlcv: dict) -> list[MotorCandidate]:
        """Returns candidates compatible with Alenix's Candidate contract"""
        return V2MotorManager.detect_all(symbol, ohlcv)
