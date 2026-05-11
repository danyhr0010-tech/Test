"""
Rutas de la API para operaciones estadísticas.

Este módulo define los endpoints REST para realizar cálculos
estadísticos utilizando la clase Statistics.
"""

from fastapi import APIRouter, HTTPException
from src.statistics import Statistics
from src.api.schemas import StatisticsRequest, StatisticsResponse, ErrorResponse

router = APIRouter(
    prefix="/statistics",
    tags=["Statistics"],
    responses={400: {"model": ErrorResponse}}
)

stats = Statistics()


@router.post(
    "/mean",
    response_model=StatisticsResponse,
    summary="Calcula el promedio",
    description="Calcula la media aritmética de una lista de números.",
    response_description="El promedio de los números proporcionados"
)
async def calculate_mean(request: StatisticsRequest) -> StatisticsResponse:
    """
    Calcula el promedio (media aritmética) de una lista de números.
    
    Args:
        request: Objeto con la lista de números
        
    Returns:
        StatisticsResponse con el promedio calculado
        
    Raises:
        HTTPException: Si la lista está vacía
        
    Example:
        Request body:
        ```json
        {
            "numbers": [1.0, 2.0, 3.0, 4.0, 5.0]
        }
        ```
        
        Response:
        ```json
        {
            "result": 3.0,
            "operation": "mean",
            "count": 5
        }
        ```
    """
    try:
        result = stats.mean(request.numbers)
        return StatisticsResponse(
            result=result,
            operation="mean",
            count=len(request.numbers)
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/median",
    response_model=StatisticsResponse,
    summary="Calcula la mediana",
    description="Calcula la mediana de una lista de números.",
    response_description="La mediana de los números proporcionados"
)
async def calculate_median(request: StatisticsRequest) -> StatisticsResponse:
    """
    Calcula la mediana de una lista de números.
    
    Args:
        request: Objeto con la lista de números
        
    Returns:
        StatisticsResponse con la mediana calculada
        
    Raises:
        HTTPException: Si la lista está vacía
        
    Example:
        Request body:
        ```json
        {
            "numbers": [1.0, 2.0, 3.0, 4.0, 5.0]
        }
        ```
        
        Response:
        ```json
        {
            "result": 3.0,
            "operation": "median",
            "count": 5
        }
        ```
    """
    try:
        result = stats.median(request.numbers)
        return StatisticsResponse(
            result=result,
            operation="median",
            count=len(request.numbers)
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/std-dev",
    response_model=StatisticsResponse,
    summary="Calcula la desviación estándar",
    description="Calcula la desviación estándar de una lista de números.",
    response_description="La desviación estándar de los números proporcionados"
)
async def calculate_std_dev(request: StatisticsRequest) -> StatisticsResponse:
    """
    Calcula la desviación estándar de una lista de números.
    
    Args:
        request: Objeto con la lista de números
        
    Returns:
        StatisticsResponse con la desviación estándar calculada
        
    Raises:
        HTTPException: Si la lista está vacía o tiene menos de 2 elementos
        
    Example:
        Request body:
        ```json
        {
            "numbers": [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
        }
        ```
        
        Response:
        ```json
        {
            "result": 2.0,
            "operation": "standard_deviation",
            "count": 8
        }
        ```
    """
    try:
        result = stats.std_dev(request.numbers)
        return StatisticsResponse(
            result=result,
            operation="standard_deviation",
            count=len(request.numbers)
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
