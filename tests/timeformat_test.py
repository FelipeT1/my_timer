import pytest
from my_timer.TimeFormat import TimeFormat

class TestTimeFormat:

    def test_empty_string(self):
        with pytest.raises(ValueError):
            TimeFormat.parse("")

    def test_negative(self):
        with pytest.raises(ValueError):
            TimeFormat.parse("-1h")

    def test_minute_input(self):
        with pytest.raises(ValueError):
            TimeFormat.parse("1h50mm")

    def test_second_input(self):
        with pytest.raises(ValueError):
            TimeFormat.parse("1h50m50ss")

    def test_valid_input(self):
        assert TimeFormat.parse("1h00m") == float(3600)
