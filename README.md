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