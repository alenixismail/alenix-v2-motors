from alenix_v2_motors import V2MotorManager

def test_motors():
    test_ohlcv = {
        "4h": [{"close": 45000 + i*10, "high": 45000 + i*10 + 100, "low": 45000 + i*10 - 100} for i in range(200)],
        "1h": [{"close": 45500 + i*2, "high": 45500 + i*2 + 20, "low": 45500 + i*2 - 20} for i in range(200)],
        "15m": [{"close": 45550 + i*0.5, "high": 45550 + i*0.5 + 5, "low": 45550 + i*0.5 - 5} for i in range(200)],
    }
    candidates = V2MotorManager.detect_all("BTCUSDT", test_ohlcv)
    print(f"Found {len(candidates)} candidates")
    assert len(candidates) > 0

if __name__ == "__main__":
    test_motors()
