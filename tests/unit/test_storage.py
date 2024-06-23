import pytest
from unittest.mock import Mock, patch
from src.storage import save_image

class TestStorage:
    @patch('builtins.open', new_callable=Mock)
    @patch('src.storage.os')
    def test_save_image(self, mock_os, mock_open):
        """Testet das Speichern von Bildern."""
        save_image('test_image.jpg', 'image_data')
        mock_os.path.exists.assert_called_once()
        mock_os.makedirs.assert_called()
        mock_open.assert_called_with('test_image.jpg', 'wb')
