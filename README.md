# Alenix V2 Motors

TC, RMR, SHORT engines for Alenix Personal Trader.

## Installation

```bash
pip install -e .
```

## Usage

```python
from alenix_v2_motors import V2MotorManager

candidates = V2MotorManager.detect_all(symbol, ohlcv)
for c in candidates:
    print(f"{c.engine_name}: {c.direction} @ {c.entry_price}")
```

## Motors

- **TC** (Trend Continuation): 4h bullish + 1h pullback + 15m close > EMA9 → LONG
- **RMR** (Range Mean Reversion): 1h compression + upper band + 15m revert → SHORT
- **SHORT** (Short Downtrend): 4h downtrend + bounce + 1h bearish → SHORT
