"""
Rutas de la API para operaciones de calculadora.

Este módulo define los endpoints REST para realizar operaciones
matemáticas básicas utilizando la clase Calculator.
"""

from fastapi import APIRouter, HTTPException
from src.calculator import Calculator
from src.api.schemas import CalculatorRequest, CalculatorResponse, ErrorResponse

router = APIRouter(
    prefix="/calculator",
    tags=["Calculator"],
    responses={400: {"model": ErrorResponse}}
)

calc = Calculator()


@router.post(
    "/add",
    response_model=CalculatorResponse,
    summary="Suma dos números",
    description="Realiza la suma de dos números y devuelve el resultado.",
    response_description="El resultado de la suma"
)
async def add(request: CalculatorRequest) -> CalculatorResponse:
    """
    Suma dos números.
    
    Args:
        request: Objeto con los dos números a sumar (a y b)
        
    Returns:
        CalculatorResponse con el resultado de la suma
        
    Example:
        Request body:
        ```json
        {
            "a": 10.0,
            "b": 5.0
        }
        ```
        
        Response:
        ```json
        {
            "result": 15.0,
            "operation": "addition"
        }
        ```
    """
    result = calc.add(request.a, request.b)
    return CalculatorResponse(result=result, operation="addition")


@router.post(
    "/subtract",
    response_model=CalculatorResponse,
    summary="Resta dos números",
    description="Realiza la resta de dos números y devuelve el resultado.",
    response_description="El resultado de la resta"
)
async def subtract(request: CalculatorRequest) -> CalculatorResponse:
    """
    Resta dos números.
    
    Args:
        request: Objeto con los dos números (a - b)
        
    Returns:
        CalculatorResponse con el resultado de la resta
        
    Example:
        Request body:
        ```json
        {
            "a": 10.0,
            "b": 5.0
        }
        ```
        
        Response:
        ```json
        {
            "result": 5.0,
            "operation": "subtraction"
        }
        ```
    """
    result = calc.subtract(request.a, request.b)
    return CalculatorResponse(result=result, operation="subtraction")


@router.post(
    "/multiply",
    response_model=CalculatorResponse,
    summary="Multiplica dos números",
    description="Realiza la multiplicación de dos números y devuelve el resultado.",
    response_description="El resultado de la multiplicación"
)
async def multiply(request: CalculatorRequest) -> CalculatorResponse:
    """
    Multiplica dos números.
    
    Args:
        request: Objeto con los dos números a multiplicar (a * b)
        
    Returns:
        CalculatorResponse con el resultado de la multiplicación
        
    Example:
        Request body:
        ```json
        {
            "a": 10.0,
            "b": 5.0
        }
        ```
        
        Response:
        ```json
        {
            "result": 50.0,
            "operation": "multiplication"
        }
        ```
    """
    result = calc.multiply(request.a, request.b)
    return CalculatorResponse(result=result, operation="multiplication")


@router.post(
    "/divide",
    response_model=CalculatorResponse,
    summary="Divide dos números",
    description="Realiza la división de dos números y devuelve el resultado. Lanza error si se intenta dividir por cero.",
    response_description="El resultado de la división"
)
async def divide(request: CalculatorRequest) -> CalculatorResponse:
    """
    Divide dos números.
    
    Args:
        request: Objeto con los dos números (a / b)
        
    Returns:
        CalculatorResponse con el resultado de la división
        
    Raises:
        HTTPException: Si b es 0 (división por cero)
        
    Example:
        Request body:
        ```json
        {
            "a": 10.0,
            "b": 5.0
        }
        ```
        
        Response:
        ```json
        {
            "result": 2.0,
            "operation": "division"
        }
        ```
    """
    try:
        result = calc.divide(request.a, request.b)
        return CalculatorResponse(result=result, operation="division")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/power",
    response_model=CalculatorResponse,
    summary="Calcula la potencia de un número",
    description="Eleva un número base a un exponente y devuelve el resultado.",
    response_description="El resultado de la potenciación"
)
async def power(request: CalculatorRequest) -> CalculatorResponse:
    """
    Calcula la potencia de un número.
    
    Args:
        request: Objeto con base (a) y exponente (b)
        
    Returns:
        CalculatorResponse con el resultado de a^b
        
    Example:
        Request body:
        ```json
        {
            "a": 2.0,
            "b": 3.0
        }
        ```
        
        Response:
        ```json
        {
            "result": 8.0,
            "operation": "power"
        }
        ```
    """
    result = calc.power(request.a, request.b)
    return CalculatorResponse(result=result, operation="power")
