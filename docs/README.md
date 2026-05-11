# Documentación - Mintlify

Esta carpeta contiene el archivo `openapi.json` generado automáticamente desde el código Python usando FastAPI.

## Archivo Generado

- **openapi.json**: Especificación OpenAPI 3.0 con toda la documentación de la API
  - 10 endpoints totales
  - 5 endpoints de calculadora
  - 3 endpoints de estadísticas
  - 2 endpoints de utilidad (root, health)

## Cómo Conectar con Mintlify

### Opción 1: Desde la Página de Mintlify (Recomendado)

1. Ve a [mintlify.com](https://mintlify.com)
2. Conecta tu repositorio de GitHub
3. Mintlify detectará automáticamente el archivo `openapi.json`
4. Crea tu configuración `mint.json` desde el dashboard de Mintlify

### Opción 2: Configuración Manual

Si prefieres configurar Mintlify manualmente, necesitarás crear un archivo `mint.json` en esta carpeta con la siguiente estructura mínima:

```json
{
  "name": "Math API",
  "logo": {
    "light": "/logo/light.svg",
    "dark": "/logo/dark.svg"
  },
  "favicon": "/favicon.png",
  "colors": {
    "primary": "#3B82F6",
    "light": "#60A5FA",
    "dark": "#2563EB"
  },
  "topbarLinks": [
    {
      "name": "GitHub",
      "url": "https://github.com/your-repo"
    }
  ],
  "navigation": [
    {
      "group": "Get Started",
      "pages": [
        "introduction",
        "quickstart"
      ]
    },
    {
      "group": "API Reference",
      "pages": [
        "api-reference/introduction",
        {
          "group": "Calculator",
          "pages": [
            "api-reference/calculator/add",
            "api-reference/calculator/subtract",
            "api-reference/calculator/multiply",
            "api-reference/calculator/divide",
            "api-reference/calculator/power"
          ]
        },
        {
          "group": "Statistics",
          "pages": [
            "api-reference/statistics/mean",
            "api-reference/statistics/median",
            "api-reference/statistics/std-dev"
          ]
        }
      ]
    }
  ],
  "openapi": "openapi.json"
}
```

## Regenerar openapi.json

Si realizas cambios en el código de la API, regenera el archivo ejecutando:

```bash
python scripts/generate_openapi.py
```

## Características del OpenAPI Generado

El archivo `openapi.json` incluye:

- **Metadata completa**: título, descripción, versión, contacto, licencia
- **Schemas de datos**: modelos Pydantic convertidos a JSON Schema
- **Endpoints documentados**: con descripciones, parámetros, ejemplos
- **Respuestas de error**: códigos HTTP y mensajes de error
- **Ejemplos de uso**: request/response bodies de ejemplo
- **Tags organizados**: agrupación por Calculator y Statistics

## Versionado

La API actual está en la versión **2.0.0**, que incluye:
- Calculadora (v1.0 features)
- Estadísticas (nuevo en v2.0)

Para documentar múltiples versiones en Mintlify, puedes:
1. Crear carpetas `v1.0/` y `v2.0/`
2. Configurar el versionado en `mint.json` usando el campo `versions`

## Próximos Pasos

1. Conecta este repositorio con Mintlify
2. Mintlify generará automáticamente la documentación desde `openapi.json`
3. Personaliza la apariencia desde el dashboard de Mintlify
4. Agrega páginas MDX adicionales para guías y tutoriales

## Estructura Sugerida para Documentación Completa

```
docs/
├── mint.json                    # Configuración de Mintlify
├── openapi.json                 # Especificación OpenAPI (generado)
├── introduction.mdx             # Página de introducción
├── quickstart.mdx               # Guía de inicio rápido
├── api-reference/
│   ├── introduction.mdx         # Intro a la API
│   ├── calculator/
│   │   └── *.mdx               # Docs de endpoints (opcional, Mintlify los genera)
│   └── statistics/
│       └── *.mdx               # Docs de endpoints (opcional)
└── guides/
    ├── installation.mdx
    ├── examples.mdx
    └── troubleshooting.mdx
```

## Notas Importantes

- ⚠️ **NO modifiques manualmente** el archivo `openapi.json`, se regenera automáticamente
- 📝 Los cambios en docstrings de Python se reflejan en `openapi.json` después de regenerar
- 🔄 Mintlify actualiza automáticamente la documentación cuando detecta cambios en GitHub
- 🎨 La personalización visual se hace desde `mint.json` o el dashboard de Mintlify
