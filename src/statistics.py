"""
Módulo de estadísticas básicas.

Este módulo proporciona funciones para calcular métricas estadísticas
comunes sobre conjuntos de datos numéricos.
"""

from typing import List


class Statistics:
    """Clase que implementa operaciones estadísticas básicas."""

    def mean(self, numbers: List[float]) -> float:
        """
        Calcula el promedio (media aritmética) de una lista de números.

        Args:
            numbers: Lista de números para calcular el promedio

        Returns:
            El promedio de los números

        Raises:
            ValueError: Si la lista está vacía

        Example:
            >>> stats = Statistics()
            >>> stats.mean([1, 2, 3, 4, 5])
            3.0
        """
        if not numbers:
            raise ValueError("La lista no puede estar vacía")
        return sum(numbers) / len(numbers)

    def median(self, numbers: List[float]) -> float:
        """
        Calcula la mediana de una lista de números.

        Args:
            numbers: Lista de números para calcular la mediana

        Returns:
            La mediana de los números

        Raises:
            ValueError: Si la lista está vacía

        Example:
            >>> stats = Statistics()
            >>> stats.median([1, 2, 3, 4, 5])
            3.0
            >>> stats.median([1, 2, 3, 4])
            2.5
        """
        if not numbers:
            raise ValueError("La lista no puede estar vacía")
        
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        
        if n % 2 == 0:
            # Si hay un número par de elementos, promediamos los dos del medio
            return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
        else:
            # Si hay un número impar, tomamos el del medio
            return sorted_numbers[n // 2]

    def std_dev(self, numbers: List[float]) -> float:
        """
        Calcula la desviación estándar de una lista de números.

        Args:
            numbers: Lista de números para calcular la desviación estándar

        Returns:
            La desviación estándar de los números

        Raises:
            ValueError: Si la lista está vacía o tiene un solo elemento

        Example:
            >>> stats = Statistics()
            >>> stats.std_dev([2, 4, 4, 4, 5, 5, 7, 9])
            2.0
        """
        if not numbers:
            raise ValueError("La lista no puede estar vacía")
        
        if len(numbers) < 2:
            raise ValueError("Se necesitan al menos 2 números para calcular la desviación estándar")
        
        # Calcular la media
        mean_value = self.mean(numbers)
        
        # Calcular la varianza (promedio de las diferencias al cuadrado)
        variance = sum((x - mean_value) ** 2 for x in numbers) / len(numbers)
        
        # La desviación estándar es la raíz cuadrada de la varianza
        return variance ** 0.5

    def variance(self, numbers: List[float]) -> float:
        """
        Calcula la varianza de una lista de números.

        Args:
            numbers: Lista de números para calcular la varianza

        Returns:
            La varianza de los números

        Raises:
            ValueError: Si la lista está vacía o tiene un solo elemento

        Example:
            >>> stats = Statistics()
            >>> stats.variance([2, 4, 4, 4, 5, 5, 7, 9])
            4.0
        """
        if not numbers:
            raise ValueError("La lista no puede estar vacía")
        
        if len(numbers) < 2:
            raise ValueError("Se necesitan al menos 2 números para calcular la varianza")
        
        mean_value = self.mean(numbers)
        return sum((x - mean_value) ** 2 for x in numbers) / len(numbers)
