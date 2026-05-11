"""
Script para generar el archivo OpenAPI spec desde la aplicación FastAPI.

Este script importa la aplicación FastAPI y exporta su especificación
OpenAPI a un archivo JSON que puede ser utilizado por herramientas de
documentación como Mintlify.

Uso:
    python scripts/generate_openapi.py
"""

import json
import sys
from pathlib import Path

# Añadir el directorio raíz al path para importar módulos
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from src.api.main import app


def generate_openapi():
    """
    Genera el archivo openapi.json desde la aplicación FastAPI.
    
    El archivo se guarda en la carpeta docs/ para que Mintlify
    pueda encontrarlo y generar la documentación automáticamente.
    """
    # Obtener el schema OpenAPI de la aplicación
    openapi_schema = app.openapi()
    
    # Crear directorio docs si no existe
    docs_dir = root_dir / "docs"
    docs_dir.mkdir(exist_ok=True)
    
    # Guardar el schema en formato JSON
    output_file = docs_dir / "openapi.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(openapi_schema, f, indent=2, ensure_ascii=False)
    
    print(f"[OK] OpenAPI spec generado exitosamente en: {output_file}")
    print(f"[INFO] Total de endpoints: {len(openapi_schema.get('paths', {}))}")
    print(f"[INFO] Version de la API: {openapi_schema.get('info', {}).get('version', 'N/A')}")
    print(f"\n[INFO] Puedes usar este archivo con Mintlify para generar documentacion interactiva.")
    
    return output_file


if __name__ == "__main__":
    try:
        generate_openapi()
    except Exception as e:
        print(f"[ERROR] Error al generar OpenAPI spec: {e}")
        sys.exit(1)
