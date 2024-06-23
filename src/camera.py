import picamera
import asyncio
from concurrent.futures import ThreadPoolExecutor

class Camera:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.executor = ThreadPoolExecutor(max_workers=1)

    async def capture_image(self, filepath):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(self.executor, self.camera.capture, filepath)

    def start_preview(self):
        self.camera.start_preview()

    def stop_preview(self):
        self.camera.stop_preview()
