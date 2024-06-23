import pytest
from datetime import datetime
from src.timestamping import add_timestamp

class TestTimestamping:
    def test_add_timestamp(self):
        """Testet, ob das Hinzufügen eines Zeitstempels das Format und die Aktualität korrekt wiedergibt."""
        test_image_name = "test_image.jpg"
        timestamped_name = add_timestamp(test_image_name)
        assert datetime.now().strftime("%Y-%m-%d") in timestamped_name
        assert test_image_name in timestamped_name
