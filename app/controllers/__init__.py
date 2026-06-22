from fastapi import APIRouter, HTTPException
from app.models import (
    Usuario, Estudiante, Docente, Materia,
    Matricula, Calificacion, Asistencia, PeriodoAcademico
)
from app import services as svc

router = APIRouter()

# --- USUARIOS ---
@router.post("/usuarios", tags=["Usuarios"])
def crear_usuario(u: Usuario):
    return svc.crear_usuario(u)

@router.get("/usuarios", tags=["Usuarios"])
def listar_usuarios():
    return svc.listar_usuarios()

# --- ESTUDIANTES ---
@router.post("/estudiantes", tags=["Estudiantes"])
def crear_estudiante(e: Estudiante):
    try:
        return svc.crear_estudiante(e)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/estudiantes", tags=["Estudiantes"])
def listar_estudiantes():
    return svc.listar_estudiantes()

# --- DOCENTES ---
@router.post("/docentes", tags=["Docentes"])
def crear_docente(d: Docente):
    try:
        return svc.crear_docente(d)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/docentes", tags=["Docentes"])
def listar_docentes():
    return svc.listar_docentes()

# --- PERIODOS ---
@router.post("/periodos", tags=["Periodos"])
def crear_periodo(p: PeriodoAcademico):
    return svc.crear_periodo(p)

@router.get("/periodos", tags=["Periodos"])
def listar_periodos():
    return svc.listar_periodos()

# --- MATERIAS ---
@router.post("/materias", tags=["Materias"])
def crear_materia(m: Materia):
    return svc.crear_materia(m)

@router.get("/materias", tags=["Materias"])
def listar_materias():
    return svc.listar_materias()

# --- MATRICULAS ---
@router.post("/matriculas", tags=["Matriculas"])
def crear_matricula(m: Matricula):
    try:
        return svc.crear_matricula(m)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/matriculas", tags=["Matriculas"])
def listar_matriculas():
    return svc.listar_matriculas()

@router.put("/matriculas/{id}/confirmar", tags=["Matriculas"])
def confirmar_matricula(id: int):
    try:
        return svc.confirmar_matricula(id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/matriculas/{id}/aprobar", tags=["Matriculas"])
def aprobar_matricula(id: int):
    try:
        return svc.aprobar_matricula(id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/matriculas/{id}/rechazar", tags=["Matriculas"])
def rechazar_matricula(id: int):
    try:
        return svc.rechazar_matricula(id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# --- CALIFICACIONES ---
@router.post("/calificaciones", tags=["Calificaciones"])
def crear_calificacion(c: Calificacion):
    try:
        return svc.crear_calificacion(c)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/calificaciones", tags=["Calificaciones"])
def listar_calificaciones():
    return svc.listar_calificaciones()

# --- ASISTENCIAS ---
@router.post("/asistencias", tags=["Asistencias"])
def crear_asistencia(a: Asistencia):
    try:
        return svc.crear_asistencia(a)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/asistencias", tags=["Asistencias"])
def listar_asistencias():
    return svc.listar_asistencias()

# --- BUSQUEDAS POR ID ---
@router.get("/usuarios/{id}", tags=["Usuarios"])
def obtener_usuario(id: int):
    from app import repositories as repo
    usuario = repo.obtener_usuario(id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.get("/estudiantes/{id}", tags=["Estudiantes"])
def obtener_estudiante(id: int):
    from app import repositories as repo
    estudiante = repo.obtener_estudiante(id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante

@router.get("/materias/{id}", tags=["Materias"])
def obtener_materia(id: int):
    from app import repositories as repo
    materia = repo.obtener_materia(id)
    if not materia:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return materia

@router.get("/matriculas/{id}", tags=["Matriculas"])
def obtener_matricula(id: int):
    from app import repositories as repo
    matricula = repo.obtener_matricula(id)
    if not matricula:
        raise HTTPException(status_code=404, detail="Matricula no encontrada")
    return matricula