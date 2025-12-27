from project import format_output, calc_local_time, get_emoji
import pytest
from datetime import datetime, timezone, timedelta

def test_calc_local_time():
    utc_now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    assert calc_local_time(0) == utc_now
    result = calc_local_time(3600)
    assert len(result) == 16

def test_get_emoji():
    assert get_emoji("clear sky") == "☀️"
    assert get_emoji("scattered clouds") == "☁️"
    assert get_emoji("light rain") == "🌧️"
    assert get_emoji("somthing else") == "🏙️"

def test_format_output():
    fake_data = {"main": {"temp": 25, "humidity": 50},
                 "weather": [{"description": "clear sky"}],
                 "timezone": 3600
                 }

    output = format_output(fake_data, "Tehran")
    assert "Weather in Tehran" in output
    assert "Local Time" in output
    assert "🌡️  25°C" in output
