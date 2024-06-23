import pytest
from unittest.mock import Mock, patch
from src.image_transfer import transfer_image

class TestImageTransfer:
    @patch('src.image_transfer.requests.post')
    def test_transfer_image(self, mock_post):
        """Testet das Übertragen von Bildern."""
        mock_post.return_value.status_code = 200
        result = transfer_image('test_image.jpg', 'http://example.com/upload')
        assert result == True
        mock_post.assert_called_with('http://example.com/upload', files={'file': ('test_image.jpg', 'rb')})
