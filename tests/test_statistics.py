"""Tests unitarios para el módulo statistics."""

import pytest
from src.statistics import Statistics


class TestStatistics:
    """Clase de tests para Statistics."""

    @pytest.fixture
    def statistics(self):
        """Fixture que proporciona una instancia de Statistics para cada test."""
        return Statistics()

    def test_mean_basic(self, statistics):
        """Test para calcular el promedio básico."""
        assert statistics.mean([1, 2, 3, 4, 5]) == 3.0
        assert statistics.mean([10, 20, 30]) == 20.0
        assert statistics.mean([5]) == 5.0

    def test_mean_negative_numbers(self, statistics):
        """Test para promedio con números negativos."""
        assert statistics.mean([-1, 1]) == 0.0
        assert statistics.mean([-5, -10, -15]) == -10.0

    def test_mean_empty_list(self, statistics):
        """Test para verificar que lista vacía lanza error."""
        with pytest.raises(ValueError, match="La lista no puede estar vacía"):
            statistics.mean([])

    def test_median_odd_count(self, statistics):
        """Test para mediana con cantidad impar de números."""
        assert statistics.median([1, 2, 3, 4, 5]) == 3.0
        assert statistics.median([7, 3, 5]) == 5.0

    def test_median_even_count(self, statistics):
        """Test para mediana con cantidad par de números."""
        assert statistics.median([1, 2, 3, 4]) == 2.5
        assert statistics.median([10, 20]) == 15.0

    def test_median_single_element(self, statistics):
        """Test para mediana con un solo elemento."""
        assert statistics.median([42]) == 42.0

    def test_median_empty_list(self, statistics):
        """Test para verificar que lista vacía lanza error."""
        with pytest.raises(ValueError, match="La lista no puede estar vacía"):
            statistics.median([])

    def test_std_dev_basic(self, statistics):
        """Test para desviación estándar básica."""
        result = statistics.std_dev([2, 4, 4, 4, 5, 5, 7, 9])
        assert result == pytest.approx(2.0)

    def test_std_dev_uniform(self, statistics):
        """Test para desviación estándar con valores uniformes."""
        result = statistics.std_dev([5, 5, 5, 5])
        assert result == 0.0

    def test_std_dev_empty_list(self, statistics):
        """Test para verificar que lista vacía lanza error."""
        with pytest.raises(ValueError, match="La lista no puede estar vacía"):
            statistics.std_dev([])

    def test_std_dev_single_element(self, statistics):
        """Test para verificar que un solo elemento lanza error."""
        with pytest.raises(ValueError, match="Se necesitan al menos 2 números"):
            statistics.std_dev([5])

    def test_variance_basic(self, statistics):
        """Test para varianza básica."""
        result = statistics.variance([2, 4, 4, 4, 5, 5, 7, 9])
        assert result == 4.0

    def test_variance_empty_list(self, statistics):
        """Test para verificar que lista vacía lanza error."""
        with pytest.raises(ValueError, match="La lista no puede estar vacía"):
            statistics.variance([])

    def test_operations_with_floats(self, statistics):
        """Test para verificar operaciones con números de punto flotante."""
        assert statistics.mean([1.5, 2.5, 3.5]) == pytest.approx(2.5)
        assert statistics.median([1.1, 2.2, 3.3]) == pytest.approx(2.2)
