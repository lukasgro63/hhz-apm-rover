import pytest
from unittest.mock import Mock, patch
from src.camera import Camera

class TestCamera:
    @pytest.fixture
    def camera(self):
        return Camera()

    @pytest.fixture
    def mock_picamera(self):
        with patch('src.camera.picamera.PiCamera') as mock:
            yield mock

    def test_init_camera(self, mock_picamera, camera):
        """Testet, ob die Kamera-Initialisierung wie erwartet funktioniert."""
        assert camera is not None
        mock_picamera.assert_called_once()

    def test_capture_image(self, mock_picamera, camera):
        """Testet, ob das Erfassen eines Bildes korrekt funktioniert."""
        camera.capture_image('test.jpg')
        mock_picamera.return_value.capture.assert_called_with('test.jpg')

    def test_start_preview(self, mock_picamera, camera):
        """Testet das Starten der Kameravorschau."""
        camera.start_preview()
        mock_picamera.return_value.start_preview.assert_called_once()

    def test_stop_preview(self, mock_picamera, camera):
        """Testet das Stoppen der Kameravorschau."""
        camera.stop_preview()
        mock_picamera.return_value.stop_preview.assert_called_once()
