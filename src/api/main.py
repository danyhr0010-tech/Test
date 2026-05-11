"""
Servidor principal de la API REST.

Este módulo configura y ejecuta el servidor FastAPI con todos los
endpoints de calculadora y estadísticas.
"""

import sys
from pathlib import Path

# Añadir el directorio raíz al path para importar módulos
root_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(root_dir))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import calculator, statistics

# Crear instancia de FastAPI con metadata
app = FastAPI(
    title="Math API",
    description="""
    API REST para operaciones matemáticas y estadísticas.
    
    Esta API proporciona endpoints para:
    * **Calculadora**: Operaciones matemáticas básicas (suma, resta, multiplicación, división, potencia)
    * **Estadísticas**: Cálculos estadísticos (promedio, mediana, desviación estándar)
    
    ## Versiones
    
    ### v2.0 (Actual)
    - Operaciones de calculadora (5 endpoints)
    - Operaciones estadísticas (3 endpoints)
    - Soporte para CORS
    
    ### v1.0 (Deprecada)
    - Solo operaciones de calculadora
    
    ## Autenticación
    
    Esta API no requiere autenticación actualmente.
    
    ## Rate Limiting
    
    No hay límites de tasa configurados actualmente.
    """,
    version="2.0.0",
    contact={
        "name": "Math API Team",
        "url": "https://github.com/test-repository/test",
        "email": "support@example.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(calculator.router)
app.include_router(statistics.router)


@app.get("/", tags=["Root"])
async def root():
    """
    Endpoint raíz de la API.
    
    Returns:
        Mensaje de bienvenida con información de la API
    """
    return {
        "message": "Welcome to Math API",
        "version": "2.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
        "openapi": "/openapi.json"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Endpoint de health check.
    
    Returns:
        Estado de salud del servicio
    """
    return {
        "status": "healthy",
        "version": "2.0.0"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
