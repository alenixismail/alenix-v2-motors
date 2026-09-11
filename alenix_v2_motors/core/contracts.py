from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class MotorCandidate:
    symbol: str
    engine_name: str
    direction: str
    entry_price: float
    invalidate: float
    confidence: float
    tf_setup: str
    notes: list = field(default_factory=list)
    generated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
