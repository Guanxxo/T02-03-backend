from typing import List, Optional
from app.models import (
    Usuario, Estudiante, Docente, Materia,
    Matricula, Calificacion, Asistencia, PeriodoAcademico
)

# Base de datos simulada en memoria
db_usuarios: List[dict] = []
db_estudiantes: List[dict] = []
db_docentes: List[dict] = []
db_materias: List[dict] = []
db_matriculas: List[dict] = []
db_calificaciones: List[dict] = []
db_asistencias: List[dict] = []
db_periodos: List[dict] = []

# Contador de IDs
contadores = {"usuario": 1, "estudiante": 1, "docente": 1,
              "materia": 1, "matricula": 1, "calificacion": 1,
              "asistencia": 1, "periodo": 1}

# --- USUARIOS ---
def crear_usuario(u: Usuario) -> dict:
    item = u.dict()
    item["id"] = contadores["usuario"]
    contadores["usuario"] += 1
    db_usuarios.append(item)
    return item

def obtener_usuarios() -> List[dict]:
    return db_usuarios

def obtener_usuario(id: int) -> Optional[dict]:
    return next((u for u in db_usuarios if u["id"] == id), None)

# --- ESTUDIANTES ---
def crear_estudiante(e: Estudiante) -> dict:
    item = e.dict()
    item["id"] = contadores["estudiante"]
    contadores["estudiante"] += 1
    db_estudiantes.append(item)
    return item

def obtener_estudiantes() -> List[dict]:
    return db_estudiantes

def obtener_estudiante(id: int) -> Optional[dict]:
    return next((e for e in db_estudiantes if e["id"] == id), None)

# --- DOCENTES ---
def crear_docente(d: Docente) -> dict:
    item = d.dict()
    item["id"] = contadores["docente"]
    contadores["docente"] += 1
    db_docentes.append(item)
    return item

def obtener_docentes() -> List[dict]:
    return db_docentes

# --- PERIODOS ---
def crear_periodo(p: PeriodoAcademico) -> dict:
    item = p.dict()
    item["id"] = contadores["periodo"]
    contadores["periodo"] += 1
    db_periodos.append(item)
    return item

def obtener_periodos() -> List[dict]:
    return db_periodos

# --- MATERIAS ---
def crear_materia(m: Materia) -> dict:
    item = m.dict()
    item["id"] = contadores["materia"]
    contadores["materia"] += 1
    db_materias.append(item)
    return item

def obtener_materias() -> List[dict]:
    return db_materias

def obtener_materia(id: int) -> Optional[dict]:
    return next((m for m in db_materias if m["id"] == id), None)

# --- MATRICULAS ---
def crear_matricula(m: Matricula) -> dict:
    item = m.dict()
    item["id"] = contadores["matricula"]
    contadores["matricula"] += 1
    db_matriculas.append(item)
    return item

def obtener_matriculas() -> List[dict]:
    return db_matriculas

def obtener_matricula(id: int) -> Optional[dict]:
    return next((m for m in db_matriculas if m["id"] == id), None)

def actualizar_estado_matricula(id: int, nuevo_estado: str) -> Optional[dict]:
    for m in db_matriculas:
        if m["id"] == id:
            m["estado"] = nuevo_estado
            return m
    return None

# --- CALIFICACIONES ---
def crear_calificacion(c: Calificacion) -> dict:
    item = c.dict()
    item["id"] = contadores["calificacion"]
    item["promedio"] = round((c.nota1 + c.nota2 + c.examen) / 3, 2)
    item["estado"] = "aprobado" if item["promedio"] >= 7 else "reprobado"
    contadores["calificacion"] += 1
    db_calificaciones.append(item)
    return item

def obtener_calificaciones() -> List[dict]:
    return db_calificaciones

# --- ASISTENCIAS ---
def crear_asistencia(a: Asistencia) -> dict:
    item = a.dict()
    item["id"] = contadores["asistencia"]
    contadores["asistencia"] += 1
    db_asistencias.append(item)
    return item

def obtener_asistencias() -> List[dict]:
    return db_asistencias