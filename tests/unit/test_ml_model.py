import pytest
import numpy as np
from unittest.mock import Mock, patch
from src.ml_model import load_model, predict

class TestMLModel:
    @pytest.fixture
    def mock_model(self):
        with patch('src.ml_model.tf.lite.Interpreter') as mock:
            mock.return_value.get_output_details.return_value = [{'index': 0}]
            mock.return_value.tensor.return_value = lambda x: np.array([])
            yield mock

    def test_load_model(self, mock_model):
        """Testet, ob das Modell korrekt geladen wird."""
        model = load_model('model.tflite')
        mock_model.assert_called_with('model.tflite')

    def test_predict(self, mock_model):
        """Testet die Vorhersagefunktionalität des ML-Modells."""
        # Angenommen, predict erwartet ein vorverarbeitetes Bild und gibt Wahrscheinlichkeiten zurück
        mock_model.return_value.invoke.return_value = None
        mock_model.return_value.tensor.return_value = lambda x: np.array([[0.1, 0.9]])
        prediction = predict(np.zeros((28, 28, 3)))
        assert prediction == 0.9  # Angenommen, das Modell gibt die Wahrscheinlichkeit für Klasse 1 zurück
