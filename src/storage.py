import os

class Storage:
    def __init__(self, storage_dir='images'):
        self.storage_dir = storage_dir
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

    def save_image(self, image_path, image_data):
        """Speichert das Bild an einem bestimmten Pfad."""
        full_path = os.path.join(self.storage_dir, image_path)
        with open(full_path, 'wb') as f:
            f.write(image_data)
        return full_path
