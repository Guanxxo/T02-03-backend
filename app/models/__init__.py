from pydantic import BaseModel
from typing import Optional
from datetime import date
from enum import Enum

# ENUMs
class RolEnum(str, Enum):
    estudiante = "estudiante"
    docente = "docente"
    admin = "admin"

class EstadoMatriculaEnum(str, Enum):
    borrador = "borrador"
    en_revision = "en_revision"
    pendiente = "pendiente"
    activa = "activa"
    rechazada = "rechazada"
    completada = "completada"
    anulada = "anulada"

class EstadoCalificacionEnum(str, Enum):
    aprobado = "aprobado"
    reprobado = "reprobado"
    pendiente = "pendiente"

# Modelos
class Usuario(BaseModel):
    id: Optional[int] = None
    nombre: str
    apellido: str
    email: str
    rol: RolEnum

class Estudiante(BaseModel):
    id: Optional[int] = None
    id_usuario: int
    codigo: str
    carrera: str
    semestre: int
    creditos_aprobados: int = 0

class Docente(BaseModel):
    id: Optional[int] = None
    id_usuario: int
    titulo: str
    especialidad: str

class PeriodoAcademico(BaseModel):
    id: Optional[int] = None
    nombre: str
    fecha_inicio: date
    fecha_fin: date

class Materia(BaseModel):
    id: Optional[int] = None
    id_docente: int
    id_periodo: int
    nombre: str
    codigo: str
    creditos: int
    cupo_max: int

class Matricula(BaseModel):
    id: Optional[int] = None
    id_estudiante: int
    id_materia: int
    id_periodo: int
    fecha: date
    estado: EstadoMatriculaEnum = EstadoMatriculaEnum.borrador

class Calificacion(BaseModel):
    id: Optional[int] = None
    id_matricula: int
    nota1: float
    nota2: float
    examen: float
    promedio: Optional[float] = None
    estado: EstadoCalificacionEnum = EstadoCalificacionEnum.pendiente

class Asistencia(BaseModel):
    id: Optional[int] = None
    id_matricula: int
    fecha: date
    presente: bool
    justificada: bool = False
    observacion: Optional[str] = None