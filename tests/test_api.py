"""Tests para los endpoints de la API REST."""

import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


class TestRootEndpoints:
    """Tests para endpoints raíz y health."""

    def test_root_endpoint(self):
        """Test para el endpoint raíz."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "Welcome to Math API"
        assert data["version"] == "2.0.0"

    def test_health_check(self):
        """Test para el health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["version"] == "2.0.0"


class TestCalculatorEndpoints:
    """Tests para endpoints de calculadora."""

    def test_add_endpoint(self):
        """Test para endpoint de suma."""
        response = client.post("/calculator/add", json={"a": 10, "b": 5})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 15.0
        assert data["operation"] == "addition"

    def test_subtract_endpoint(self):
        """Test para endpoint de resta."""
        response = client.post("/calculator/subtract", json={"a": 10, "b": 5})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 5.0
        assert data["operation"] == "subtraction"

    def test_multiply_endpoint(self):
        """Test para endpoint de multiplicación."""
        response = client.post("/calculator/multiply", json={"a": 10, "b": 5})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 50.0
        assert data["operation"] == "multiplication"

    def test_divide_endpoint(self):
        """Test para endpoint de división."""
        response = client.post("/calculator/divide", json={"a": 10, "b": 5})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 2.0
        assert data["operation"] == "division"

    def test_divide_by_zero(self):
        """Test para división por cero."""
        response = client.post("/calculator/divide", json={"a": 10, "b": 0})
        assert response.status_code == 400
        assert "No se puede dividir por cero" in response.json()["detail"]

    def test_power_endpoint(self):
        """Test para endpoint de potencia."""
        response = client.post("/calculator/power", json={"a": 2, "b": 3})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 8.0
        assert data["operation"] == "power"


class TestStatisticsEndpoints:
    """Tests para endpoints de estadísticas."""

    def test_mean_endpoint(self):
        """Test para endpoint de promedio."""
        response = client.post(
            "/statistics/mean",
            json={"numbers": [1, 2, 3, 4, 5]}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 3.0
        assert data["operation"] == "mean"
        assert data["count"] == 5

    def test_median_endpoint(self):
        """Test para endpoint de mediana."""
        response = client.post(
            "/statistics/median",
            json={"numbers": [1, 2, 3, 4, 5]}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 3.0
        assert data["operation"] == "median"
        assert data["count"] == 5

    def test_std_dev_endpoint(self):
        """Test para endpoint de desviación estándar."""
        response = client.post(
            "/statistics/std-dev",
            json={"numbers": [2, 4, 4, 4, 5, 5, 7, 9]}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == pytest.approx(2.0)
        assert data["operation"] == "standard_deviation"
        assert data["count"] == 8

    def test_mean_empty_list(self):
        """Test para promedio con lista vacía."""
        response = client.post("/statistics/mean", json={"numbers": []})
        assert response.status_code == 422  # Validation error

    def test_std_dev_insufficient_data(self):
        """Test para desviación estándar con datos insuficientes."""
        response = client.post("/statistics/std-dev", json={"numbers": [1]})
        assert response.status_code == 400
