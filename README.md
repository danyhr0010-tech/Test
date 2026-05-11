# Math API - Proyecto de Ejemplo

Proyecto de ejemplo para demostrar documentación técnica de APIs con generación automática usando FastAPI y Mintlify.

## Descripción

Este proyecto implementa una API REST con operaciones matemáticas y estadísticas. Su propósito principal es servir como ejemplo de:
- **Generación automática de documentación** desde código Python
- **Versionado de APIs** (v1.0 y v2.0)
- **Buenas prácticas** en estructura de código y testing
- **Integración con herramientas de documentación** como Mintlify

## Características

### Módulos de Lógica
- **Calculadora**: Operaciones matemáticas básicas (suma, resta, multiplicación, división, potencia)
- **Estadísticas**: Cálculos estadísticos (promedio, mediana, desviación estándar, varianza)

### API REST (v2.0)
- **10 endpoints** totalmente documentados
- **Validación automática** con Pydantic
- **Especificación OpenAPI 3.0** generada automáticamente
- **Documentación interactiva** con Swagger UI
- **Manejo de errores** completo

## Estructura del Proyecto

```
Test/
├── src/                           # Código fuente
│   ├── calculator.py             # Módulo de calculadora
│   ├── statistics.py             # Módulo de estadísticas (nuevo en v2.0)
│   ├── main.py                   # Script de demostración
│   └── api/                      # API REST con FastAPI
│       ├── main.py               # Servidor FastAPI
│       ├── schemas.py            # Modelos Pydantic
│       └── routes/
│           ├── calculator.py     # 5 endpoints de calculadora
│           └── statistics.py     # 3 endpoints de estadísticas
├── tests/                         # Tests unitarios (34 tests)
│   ├── test_calculator.py
│   ├── test_statistics.py
│   └── test_api.py
├── docs/                          # Documentación
│   ├── openapi.json              # Spec OpenAPI (generado automáticamente)
│   └── README.md                 # Instrucciones para Mintlify
├── scripts/
│   └── generate_openapi.py       # Script para generar openapi.json
├── requirements.txt
├── pyproject.toml
└── README.md                      # Este archivo
```

## Requisitos

- Python 3.10 o superior
- FastAPI y Uvicorn
- Pytest (para tests)

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd Test
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### 1. Ejecutar la API REST

```bash
# Opción 1: Usando uvicorn directamente
uvicorn src.api.main:app --reload

# Opción 2: Ejecutando el script main.py
python src/api/main.py
```

La API estará disponible en:
- **Servidor**: http://localhost:8000
- **Documentación Swagger**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### 2. Usar los Módulos Directamente

```python
from src.calculator import Calculator
from src.statistics import Statistics

# Calculadora
calc = Calculator()
print(calc.add(10, 5))        # 15.0
print(calc.divide(10, 2))     # 5.0

# Estadísticas
stats = Statistics()
print(stats.mean([1, 2, 3, 4, 5]))           # 3.0
print(stats.median([1, 2, 3, 4, 5]))         # 3.0
print(stats.std_dev([2, 4, 4, 4, 5, 5, 7, 9]))  # 2.0
```

### 3. Ejecutar el Script de Demostración

```bash
python src/main.py
```

## Ejemplos de Uso de la API

### Calculadora

```bash
# Suma
curl -X POST "http://localhost:8000/calculator/add" \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 5}'

# Respuesta: {"result": 15.0, "operation": "addition"}
```

### Estadísticas

```bash
# Promedio
curl -X POST "http://localhost:8000/statistics/mean" \
  -H "Content-Type: application/json" \
  -d '{"numbers": [1, 2, 3, 4, 5]}'

# Respuesta: {"result": 3.0, "operation": "mean", "count": 5}
```

## Tests

El proyecto incluye **34 tests** que cubren:
- Tests unitarios para Calculator
- Tests unitarios para Statistics  
- Tests de integración para API endpoints

```bash
# Ejecutar todos los tests
pytest

# Con verbose
pytest -v

# Con cobertura
pytest --cov=src tests/
```

**Resultado actual**: ✅ 34 tests pasando

## Generación Automática de Documentación

### Generar OpenAPI Spec

El proyecto incluye un script para generar automáticamente la especificación OpenAPI desde el código:

```bash
python scripts/generate_openapi.py
```

Esto crea/actualiza el archivo `docs/openapi.json` con:
- Toda la metadata de la API
- Documentación de los 10 endpoints
- Esquemas de datos (request/response)
- Ejemplos de uso
- Manejo de errores

### Integración con Mintlify

El archivo `docs/openapi.json` está listo para usar con Mintlify:

1. Conecta tu repositorio de GitHub con Mintlify
2. Mintlify detectará automáticamente `docs/openapi.json`
3. La documentación se generará automáticamente

Ver `docs/README.md` para instrucciones detalladas.

## Versionado de la API

### v1.0 (Deprecada)
- 5 endpoints de calculadora
- Operaciones matemáticas básicas

### v2.0 (Actual)
- 5 endpoints de calculadora
- **3 endpoints de estadísticas** (NUEVO)
- Mejoras en documentación
- Validación mejorada con Pydantic

## Endpoints Disponibles

### Calculator (5 endpoints)
- `POST /calculator/add` - Suma dos números
- `POST /calculator/subtract` - Resta dos números
- `POST /calculator/multiply` - Multiplica dos números
- `POST /calculator/divide` - Divide dos números
- `POST /calculator/power` - Calcula potencia

### Statistics (3 endpoints)
- `POST /statistics/mean` - Calcula promedio
- `POST /statistics/median` - Calcula mediana
- `POST /statistics/std-dev` - Calcula desviación estándar

### Utilidades (2 endpoints)
- `GET /` - Información de la API
- `GET /health` - Health check

## Contribuir

Ver `docs/CONTRIBUTING.md` para guías de contribución.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
