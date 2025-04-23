import pytest
from main import get_weather

def test_get_weather_valid_city():
    data = get_weather("İstanbul")
    assert data is not None
    assert "main" in data
    assert "temp" in data["main"]

def test_get_weather_invalid_city():
    data = get_weather("xxyyzzşş")  # geçersiz şehir adı
    assert data is None
