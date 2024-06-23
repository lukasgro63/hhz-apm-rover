import pytest
from datetime import datetime
from src.timestamping import Timestamping

class TestTimestamping:
    @pytest.fixture
    def timestamping(self):
        return Timestamping()

    def test_add_timestamp(self, timestamping):
        """Testet, ob das Hinzufügen eines Zeitstempels das Format und die Aktualität korrekt wiedergibt."""
        test_image_name = "test_image.jpg"
        timestamped_name = timestamping.add_timestamp(test_image_name)
        
        # Überprüfen, ob der Zeitstempel korrekt formatiert ist
        assert datetime.now().strftime("%Y-%m-%d") in timestamped_name
        assert test_image_name.split('.')[0] in timestamped_name
