import pytest
from src.decision_unit import should_save_image

class TestDecisionUnit:
    def test_should_save_image_high_confidence(self):
        """Testet, ob die Entscheidung korrekt getroffen wird, wenn die Konfidenz hoch ist."""
        assert should_save_image(0.9) == True

    def test_should_save_image_low_confidence(self):
        """Testet, ob die Entscheidung korrekt getroffen wird, wenn die Konfidenz niedrig ist."""
        assert should_save_image(0.4) == False

    def test_should_save_image_boundary_condition(self):
        """Testet die Grenzbedingung an der Entscheidungsschwelle."""
        assert should_save_image(0.5) == True
