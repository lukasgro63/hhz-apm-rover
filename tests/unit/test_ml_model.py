import pytest
import numpy as np
from unittest.mock import patch, MagicMock
from src.ml_model import MLModel

class TestMLModel:
    @pytest.fixture
    def ml_model(self):
        return MLModel()

    @pytest.mark.asyncio
    async def test_load_model(self, ml_model):
        """Testet, ob das Modell korrekt geladen wird."""
        with patch.object(ml_model, '_create_interpreter', autospec=True) as mock_create_interpreter:
            mock_interpreter = MagicMock()
            mock_create_interpreter.return_value = mock_interpreter
            await ml_model.load_model('model/stone_detection_model.tflite')
            mock_create_interpreter.assert_called_once_with('model/stone_detection_model.tflite')
            assert ml_model.interpreter is not None

    @pytest.mark.asyncio
    async def test_predict(self, ml_model):
        """Testet die Vorhersagefunktionalität des ML-Modells."""
        with patch.object(ml_model, '_create_interpreter', autospec=True) as mock_create_interpreter:
            mock_interpreter = MagicMock()
            mock_create_interpreter.return_value = mock_interpreter
            await ml_model.load_model('model/stone_detection_model.tflite')
            mock_interpreter.get_output_details.return_value = [{'index': 0}]
            mock_interpreter.tensor.side_effect = lambda idx: np.zeros((1, 150, 150, 3)).astype(np.float32) / 255.0
            mock_interpreter.get_tensor.return_value = np.array([[0.9]])

            prediction = await ml_model.predict(np.zeros((150, 150, 3)))
            assert prediction == 0.9  # Angenommen, das Modell gibt die Wahrscheinlichkeit für Klasse 1 zurück
