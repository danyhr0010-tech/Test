"""
Módulo de calculadora simple.

Este módulo proporciona funciones básicas de calculadora para realizar
operaciones matemáticas comunes.
"""


class Calculator:
    """Clase que implementa operaciones matemáticas básicas."""

    def add(self, a: float, b: float) -> float:
        """
        Suma dos números. Pueden ser enteros o decimales.

        Args:
            a: Primer número
            b: Segundo número

        Returns:
            La suma de a y b

        Example:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5.0
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Resta dos números.

        Args:
            a: Número del que se resta
            b: Número a restar

        Returns:
            La diferencia entre a y b

        Example:
            >>> calc = Calculator()
            >>> calc.subtract(5, 3)
            2.0
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Multiplica dos números.

        Args:
            a: Primer número
            b: Segundo número

        Returns:
            El producto de a y b

        Example:
            >>> calc = Calculator()
            >>> calc.multiply(4, 3)
            12.0
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Divide dos números.

        Args:
            a: Dividendo
            b: Divisor

        Returns:
            El cociente de a entre b

        Raises:
            ValueError: Si b es 0

        Example:
            >>> calc = Calculator()
            >>> calc.divide(10, 2)
            5.0
        """
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """
        Calcula la potencia de un número.

        Args:
            base: Número base
            exponent: Exponente

        Returns:
            base elevado a exponent

        Example:
            >>> calc = Calculator()
            >>> calc.power(2, 3)
            8.0
        """
        return base ** exponent
