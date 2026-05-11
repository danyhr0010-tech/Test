"""Tests unitarios para el módulo calculator."""

import pytest
from src.calculator import Calculator


class TestCalculator:
    """Clase de tests para Calculator."""

    @pytest.fixture
    def calculator(self):
        """Fixture que proporciona una instancia de Calculator para cada test."""
        return Calculator()

    def test_add(self, calculator):
        """Test para la operación de suma."""
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0
        assert calculator.add(-1, -1) == -2
        assert calculator.add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract(self, calculator):
        """Test para la operación de resta."""
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(3, 5) == -2
        assert calculator.subtract(0, 0) == 0
        assert calculator.subtract(-5, -3) == -2

    def test_multiply(self, calculator):
        """Test para la operación de multiplicación."""
        assert calculator.multiply(2, 3) == 6
        assert calculator.multiply(-2, 3) == -6
        assert calculator.multiply(-2, -3) == 6
        assert calculator.multiply(0, 100) == 0

    def test_divide(self, calculator):
        """Test para la operación de división."""
        assert calculator.divide(6, 2) == 3
        assert calculator.divide(5, 2) == 2.5
        assert calculator.divide(-6, 2) == -3
        assert calculator.divide(-6, -2) == 3

    def test_divide_by_zero(self, calculator):
        """Test para verificar que la división por cero lanza un error."""
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            calculator.divide(5, 0)

    def test_power(self, calculator):
        """Test para la operación de potenciación."""
        assert calculator.power(2, 3) == 8
        assert calculator.power(5, 2) == 25
        assert calculator.power(2, 0) == 1
        assert calculator.power(10, -1) == 0.1
        assert calculator.power(-2, 2) == 4
        assert calculator.power(-2, 3) == -8

    def test_operations_with_floats(self, calculator):
        """Test para verificar operaciones con números de punto flotante."""
        assert calculator.add(1.5, 2.5) == 4.0
        assert calculator.multiply(0.1, 10) == pytest.approx(1.0)
        assert calculator.divide(1, 3) == pytest.approx(0.3333333333333333)
