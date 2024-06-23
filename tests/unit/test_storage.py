import pytest
from unittest.mock import mock_open, patch
from src.storage import Storage
import os

class TestStorage:
    @pytest.fixture
    def storage(self):
        return Storage()

    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_image(self, mock_open, mock_makedirs, storage):
        """Testet das Speichern von Bildern."""
        image_path = 'test_image.jpg'
        image_data = b'test_image_data'

        saved_path = storage.save_image(image_path, image_data)
        
        mock_open.assert_called_with(os.path.join(storage.storage_dir, image_path), 'wb')
        mock_open().write.assert_called_once_with(image_data)
        assert saved_path == os.path.join(storage.storage_dir, image_path)
