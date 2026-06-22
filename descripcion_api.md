# Descripción de Endpoints - SGA API

## Base URL
http://127.0.0.1:8000/api

## Usuarios
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /usuarios | Lista todos los usuarios |
| POST | /usuarios | Crea un nuevo usuario |
| GET | /usuarios/{id} | Obtiene un usuario por ID |
| PUT | /usuarios/{id} | Actualiza un usuario |
| DELETE | /usuarios/{id} | Elimina un usuario |

## Estudiantes
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /estudiantes | Lista todos los estudiantes |
| POST | /estudiantes | Crea un nuevo estudiante |
| GET | /estudiantes/{id} | Obtiene un estudiante por ID |
| PUT | /estudiantes/{id} | Actualiza un estudiante |
| DELETE | /estudiantes/{id} | Elimina un estudiante |
| GET | /estudiantes/{id}/matriculas | Lista matrículas de un estudiante |

## Docentes
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /docentes | Lista todos los docentes |
| POST | /docentes | Crea un nuevo docente |
| GET | /docentes/{id}/materias | Lista materias de un docente |

## Periodos Académicos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /periodos | Lista todos los periodos |
| POST | /periodos | Crea un nuevo periodo |
| GET | /periodos/{id}/materias | Lista materias de un periodo |

## Materias
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /materias | Lista todas las materias |
| POST | /materias | Crea una nueva materia |
| GET | /materias/{id} | Obtiene una materia por ID |
| PUT | /materias/{id} | Actualiza una materia |
| DELETE | /materias/{id} | Elimina una materia |

## Matrículas
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /matriculas | Lista todas las matrículas |
| POST | /matriculas | Crea una nueva matrícula |
| GET | /matriculas/{id} | Obtiene una matrícula por ID |
| PUT | /matriculas/{id}/confirmar | Confirma una matrícula |
| PUT | /matriculas/{id}/aprobar | Aprueba una matrícula |
| PUT | /matriculas/{id}/rechazar | Rechaza una matrícula |
| DELETE | /matriculas/{id} | Elimina una matrícula |
| GET | /matriculas/{id}/asistencia | Reporte de asistencia |
| GET | /matriculas/{id}/calificacion | Reporte de calificaciones |

## Calificaciones
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /calificaciones | Lista todas las calificaciones |
| POST | /calificaciones | Crea una calificación |

## Asistencias
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /asistencias | Lista todas las asistencias |
| POST | /asistencias | Registra una asistencia |

## Estadísticas
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /estadisticas | Resumen general del sistema |