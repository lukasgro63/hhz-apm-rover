import tensorflow as tf
import asyncio
from concurrent.futures import ThreadPoolExecutor

class MLModel:
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.interpreter = None

    async def load_model(self, model_path):
        loop = asyncio.get_event_loop()
        self.interpreter = await loop.run_in_executor(self.executor, self._create_interpreter, model_path)
        await loop.run_in_executor(self.executor, self.interpreter.allocate_tensors)

    def _create_interpreter(self, model_path):
        return tf.lite.Interpreter(model_path=model_path)

    async def predict(self, image):
        loop = asyncio.get_event_loop()
        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()
        self.interpreter.set_tensor(input_details[0]['index'], [image])
        await loop.run_in_executor(self.executor, self.interpreter.invoke)
        output_data = self.interpreter.get_tensor(output_details[0]['index'])
        return output_data[0][0]
