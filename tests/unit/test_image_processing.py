import pytest
import numpy as np
from src.image_processing import preprocess_image

class TestImageProcessing:
    def test_preprocess_image(self):
        """Testet, ob die Bildvorverarbeitung korrekte Ausmaße und Typen zurückgibt."""
        # Beispielbild (schwarz, 100x100 Pixel)
        test_image = np.zeros((100, 100, 3), dtype=np.uint8)
        # Angenommene Vorverarbeitungsfunktion, die Bild auf 28x28 skaliert
        processed_image = preprocess_image(test_image)

        # Überprüfen, ob die Größe und der Typ des verarbeiteten Bildes korrekt sind
        assert processed_image.shape == (28, 28, 3)
        assert processed_image.dtype == np.float32
