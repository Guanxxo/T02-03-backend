from pydantic import BaseModel, Field, field_validator
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
    nombre: str = Field(..., min_length=2, max_length=100)
    apellido: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    rol: RolEnum

class Estudiante(BaseModel):
    id: Optional[int] = None
    id_usuario: int
    codigo: str = Field(..., min_length=3, max_length=20)
    carrera: str = Field(..., min_length=3, max_length=100)
    semestre: int = Field(..., ge=1, le=10)
    creditos_aprobados: int = Field(default=0, ge=0)

class Docente(BaseModel):
    id: Optional[int] = None
    id_usuario: int
    titulo: str = Field(..., min_length=2, max_length=50)
    especialidad: str = Field(..., min_length=2, max_length=100)

class PeriodoAcademico(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(..., min_length=3, max_length=50)
    fecha_inicio: date
    fecha_fin: date

    @field_validator("fecha_fin")
    def fecha_fin_mayor(cls, v, info):
        if "fecha_inicio" in info.data and v <= info.data["fecha_inicio"]:
            raise ValueError("La fecha de fin debe ser mayor a la fecha de inicio")
        return v

class Materia(BaseModel):
    id: Optional[int] = None
    id_docente: int
    id_periodo: int
    nombre: str = Field(..., min_length=3, max_length=100)
    codigo: str = Field(..., min_length=2, max_length=20)
    creditos: int = Field(..., ge=1, le=10)
    cupo_max: int = Field(..., ge=1, le=100)

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
    nota1: float = Field(..., ge=0, le=10)
    nota2: float = Field(..., ge=0, le=10)
    examen: float = Field(..., ge=0, le=10)
    promedio: Optional[float] = None
    estado: EstadoCalificacionEnum = EstadoCalificacionEnum.pendiente

class Asistencia(BaseModel):
    id: Optional[int] = None
    id_matricula: int
    fecha: date
    presente: bool
    justificada: bool = False
    observacion: Optional[str] = Field(default=None, max_length=255)