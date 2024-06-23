import pytest
from src.decision_unit import DecisionUnit

class TestDecisionUnit:
    @pytest.fixture
    def decision_unit(self):
        return DecisionUnit()

    def test_should_save_image_high_confidence(self, decision_unit):
        """Testet, ob die Entscheidung korrekt getroffen wird, wenn die Konfidenz hoch ist."""
        assert decision_unit.should_save_image(0.9) == True

    def test_should_save_image_low_confidence(self, decision_unit):
        """Testet, ob die Entscheidung korrekt getroffen wird, wenn die Konfidenz niedrig ist."""
        assert decision_unit.should_save_image(0.4) == False

    def test_should_save_image_boundary_condition(self, decision_unit):
        """Testet die Grenzbedingung an der Entscheidungsschwelle."""
        assert decision_unit.should_save_image(0.5) == True
