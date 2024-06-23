import cv2
import numpy as np
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ImageProcessor:
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=1)

    async def preprocess_image(self, image):
        loop = asyncio.get_event_loop()
        processed_image = await loop.run_in_executor(self.executor, cv2.resize, image, (150, 150))
        processed_image = processed_image.astype('float32') / 255.0
        return processed_image
