import pytest
from unittest.mock import Mock, patch
import sys

# Mock picamera import if not on Raspberry Pi
if not sys.platform.startswith('linux'):
    sys.modules['picamera'] = Mock()

from src.camera import Camera

class TestCamera:
    @pytest.fixture
    def camera(self):
        return Camera()

    @pytest.fixture
    def mock_picamera(self):
        with patch('src.camera.picamera.PiCamera') as mock:
            yield mock

    def test_init_camera(self, mock_picamera):
        """Testet, ob die Kamera-Initialisierung wie erwartet funktioniert."""
        camera = Camera()
        assert camera is not None
        mock_picamera.assert_called_once()

    @pytest.mark.asyncio
    async def test_capture_image(self, mock_picamera):
        """Testet, ob das Erfassen eines Bildes korrekt funktioniert."""
        camera = Camera()
        await camera.capture_image('test.jpg')
        mock_picamera.return_value.capture.assert_called_with('test.jpg')

    def test_start_preview(self, mock_picamera):
        """Testet das Starten der Kameravorschau."""
        camera = Camera()
        camera.start_preview()
        mock_picamera.return_value.start_preview.assert_called_once()

    def test_stop_preview(self, mock_picamera):
        """Testet das Stoppen der Kameravorschau."""
        camera = Camera()
        camera.stop_preview()
        mock_picamera.return_value.stop_preview.assert_called_once()
