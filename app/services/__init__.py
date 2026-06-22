from app import repositories as repo
from app.models import (
    Usuario, Estudiante, Docente, Materia,
    Matricula, Calificacion, Asistencia, PeriodoAcademico
)

# --- USUARIOS ---
def crear_usuario(u: Usuario):
    return repo.crear_usuario(u)

def listar_usuarios():
    return repo.obtener_usuarios()

# --- ESTUDIANTES ---
def crear_estudiante(e: Estudiante):
    usuario = repo.obtener_usuario(e.id_usuario)
    if not usuario:
        raise ValueError("El usuario no existe")
    return repo.crear_estudiante(e)

def listar_estudiantes():
    return repo.obtener_estudiantes()

# --- DOCENTES ---
def crear_docente(d: Docente):
    usuario = repo.obtener_usuario(d.id_usuario)
    if not usuario:
        raise ValueError("El usuario no existe")
    return repo.crear_docente(d)

def listar_docentes():
    return repo.obtener_docentes()

# --- PERIODOS ---
def crear_periodo(p: PeriodoAcademico):
    return repo.crear_periodo(p)

def listar_periodos():
    return repo.obtener_periodos()

# --- MATERIAS ---
def crear_materia(m: Materia):
    return repo.crear_materia(m)

def listar_materias():
    return repo.obtener_materias()

# --- MATRICULAS ---
def crear_matricula(m: Matricula):
    estudiante = repo.obtener_estudiante(m.id_estudiante)
    if not estudiante:
        raise ValueError("El estudiante no existe")
    materia = repo.obtener_materia(m.id_materia)
    if not materia:
        raise ValueError("La materia no existe")
    return repo.crear_matricula(m)

def listar_matriculas():
    return repo.obtener_matriculas()

def aprobar_matricula(id: int):
    matricula = repo.obtener_matricula(id)
    if not matricula:
        raise ValueError("Matrícula no encontrada")
    if matricula["estado"] != "pendiente":
        raise ValueError("Solo se pueden aprobar matrículas en estado pendiente")
    return repo.actualizar_estado_matricula(id, "activa")

def rechazar_matricula(id: int):
    matricula = repo.obtener_matricula(id)
    if not matricula:
        raise ValueError("Matrícula no encontrada")
    return repo.actualizar_estado_matricula(id, "rechazada")

def confirmar_matricula(id: int):
    matricula = repo.obtener_matricula(id)
    if not matricula:
        raise ValueError("Matrícula no encontrada")
    if matricula["estado"] != "borrador":
        raise ValueError("Solo se pueden confirmar matrículas en estado borrador")
    return repo.actualizar_estado_matricula(id, "pendiente")

# --- CALIFICACIONES ---
def crear_calificacion(c: Calificacion):
    matricula = repo.obtener_matricula(c.id_matricula)
    if not matricula:
        raise ValueError("La matrícula no existe")
    return repo.crear_calificacion(c)

def listar_calificaciones():
    return repo.obtener_calificaciones()

# --- ASISTENCIAS ---
def crear_asistencia(a: Asistencia):
    matricula = repo.obtener_matricula(a.id_matricula)
    if not matricula:
        raise ValueError("La matrícula no existe")
    return repo.crear_asistencia(a)

def listar_asistencias():
    return repo.obtener_asistencias()