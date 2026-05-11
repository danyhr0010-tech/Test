"""
Esquemas de datos (modelos Pydantic) para la API.

Este módulo define los modelos de datos que se utilizan para validar
las peticiones y respuestas de la API.
"""

from typing import List
from pydantic import BaseModel, Field


class CalculatorRequest(BaseModel):
    """
    Modelo para peticiones de operaciones de calculadora con dos operandos.
    
    Attributes:
        a: Primer operando
        b: Segundo operando
    """
    a: float = Field(..., description="Primer número de la operación", example=10.0)
    b: float = Field(..., description="Segundo número de la operación", example=5.0)


class CalculatorResponse(BaseModel):
    """
    Modelo para respuestas de operaciones de calculadora.
    
    Attributes:
        result: Resultado de la operación
        operation: Nombre de la operación realizada
    """
    result: float = Field(..., description="Resultado de la operación", example=15.0)
    operation: str = Field(..., description="Operación realizada", example="addition")


class StatisticsRequest(BaseModel):
    """
    Modelo para peticiones de operaciones estadísticas.
    
    Attributes:
        numbers: Lista de números para calcular estadísticas
    """
    numbers: List[float] = Field(
        ..., 
        description="Lista de números para el cálculo estadístico",
        example=[1.0, 2.0, 3.0, 4.0, 5.0],
        min_length=1
    )


class StatisticsResponse(BaseModel):
    """
    Modelo para respuestas de operaciones estadísticas.
    
    Attributes:
        result: Resultado del cálculo estadístico
        operation: Nombre de la operación realizada
        count: Cantidad de números procesados
    """
    result: float = Field(..., description="Resultado del cálculo", example=3.0)
    operation: str = Field(..., description="Operación realizada", example="mean")
    count: int = Field(..., description="Cantidad de números procesados", example=5)


class ErrorResponse(BaseModel):
    """
    Modelo para respuestas de error.
    
    Attributes:
        error: Mensaje de error
        detail: Detalles adicionales del error
    """
    error: str = Field(..., description="Tipo de error", example="ValueError")
    detail: str = Field(..., description="Descripción del error", example="Division by zero")
