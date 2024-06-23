import pytest
import numpy as np
from src.image_processing import ImageProcessor

class TestImageProcessing:
    @pytest.fixture
    def image_processor(self):
        return ImageProcessor()

    @pytest.mark.asyncio
    async def test_preprocess_image(self, image_processor):
        """Testet, ob die Bildvorverarbeitung korrekte Ausmaße und Typen zurückgibt."""
        # Beispielbild (schwarz, 100x100 Pixel)
        test_image = np.zeros((100, 100, 3), dtype=np.uint8)
        # Angenommene Vorverarbeitungsfunktion, die Bild auf 150x150 skaliert
        processed_image = await image_processor.preprocess_image(test_image)

        # Überprüfen, ob die Größe und der Typ des verarbeiteten Bildes korrekt sind
        assert processed_image.shape == (150, 150, 3)
        assert processed_image.dtype == np.float32
