class DecisionUnit:
    def __init__(self, threshold=0.5):
        self.threshold = threshold

    def should_save_image(self, confidence):
        """Entscheidet, ob das Bild gespeichert werden soll, basierend auf der Konfidenz."""
        return confidence >= self.threshold
