# Sistema de Gestión Académica (SGA)

Backend desarrollado con FastAPI para la materia de Ingeniería de Software 2026.

## Integrantes
- Juan Sebastián Chevez Ullon - Grupo 1

## Tecnologías
- Python 3.14
- FastAPI
- Uvicorn

## Instalación

1. Clonar el repositorio:
   git clone https://github.com/Guanxxo/T02-03-backend.git

2. Instalar dependencias:
   pip install -r requirements.txt

3. Ejecutar el servidor:
   uvicorn main:app --reload

## Documentación
Una vez ejecutado, acceder a:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Módulos
- Usuarios
- Estudiantes
- Docentes
- Periodos Académicos
- Materias
- Matrículas
- Calificaciones
- Asistencias

## Arquitectura
El proyecto sigue el patrón modelo/repositorio/servicio/controlador:
- models: define las entidades del sistema
- repositories: acceso a datos
- services: lógica de negocio
- controllers: endpoints REST

## Enlace del Repositorio
https://github.com/Guanxxo/T02-03-backend

## Endpoints disponibles
- GET/POST /api/usuarios
- GET/POST /api/estudiantes
- GET/POST /api/docentes
- GET/POST /api/periodos
- GET/POST /api/materias
- GET/POST /api/matriculas
- GET/POST /api/calificaciones
- GET/POST /api/asistencias
- GET /api/estadisticas
- GET /api/estudiantes/{id}/resumen
- GET /api/materias/{id}/resumen
- GET /api/matriculas/{id}/asistencia
- GET /api/matriculas/{id}/calificacion
- PUT /api/matriculas/{id}/confirmar
- PUT /api/matriculas/{id}/aprobar
- PUT /api/matriculas/{id}/rechazar
- PUT /api/matriculas/{id}/anular
- PUT /api/matriculas/{id}/completar
- PUT /api/matriculas/{id}/revisar

## Pruebas Unitarias

Para ejecutar las pruebas:
   python -m pytest tests/ -v

Para ver la cobertura:
   python -m pytest tests/ --cov=app --cov-report=term-missing

### Resultados
- Total de pruebas: 122
- Cobertura total: 89%
- models: 100%
- repositories: 100%
- services: 100%
- controllers: 80%