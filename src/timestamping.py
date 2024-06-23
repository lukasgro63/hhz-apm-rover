from datetime import datetime

class Timestamping:
    def add_timestamp(self, image_name):
        """Fügt dem Bildnamen einen Zeitstempel hinzu."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name, ext = image_name.rsplit('.', 1)
        return f"{name}_{timestamp}.{ext}"
