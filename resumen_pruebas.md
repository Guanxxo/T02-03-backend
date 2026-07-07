# Resumen de Pruebas Unitarias - T02.04

## Herramientas utilizadas
- Pytest 9.1.1
- Coverage.py 7.14.3
- httpx 0.28.1 (TestClient de FastAPI)

## Archivos de prueba
| Archivo | Pruebas | Descripción |
|---------|---------|-------------|
| test_models.py | 19 | Validaciones de modelos Pydantic |
| test_repositories.py | 21 | Operaciones CRUD en base de datos |
| test_services.py | 28 | Lógica de negocio y validaciones |
| test_controllers.py | 42 | Endpoints REST de la API |
| test_integracion.py | 2 | Flujos completos del sistema |
| **Total** | **122** | |

## Cobertura por módulo
| Módulo | Cobertura |
|--------|-----------|
| models | 100% |
| repositories | 100% |
| services | 100% |
| controllers | 80% |
| **Total** | **89%** |

## Casos de prueba destacados
- Validación de email con expresión regular
- Ciclo de vida completo de matrícula (borrador → pendiente → activa)
- Cálculo automático de promedio y estado de calificación
- Verificación de porcentaje de asistencia
- Manejo de errores 404 para recursos inexistentes