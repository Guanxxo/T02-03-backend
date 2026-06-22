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

# --- ELIMINACIONES ---
@router.delete("/usuarios/{id}", tags=["Usuarios"])
def eliminar_usuario(id: int):
    from app import repositories as repo
    usuario = repo.obtener_usuario(id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    repo.db_usuarios.remove(usuario)
    return {"mensaje": "Usuario eliminado correctamente"}

@router.delete("/estudiantes/{id}", tags=["Estudiantes"])
def eliminar_estudiante(id: int):
    from app import repositories as repo
    estudiante = repo.obtener_estudiante(id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    repo.db_estudiantes.remove(estudiante)
    return {"mensaje": "Estudiante eliminado correctamente"}

@router.delete("/materias/{id}", tags=["Materias"])
def eliminar_materia(id: int):
    from app import repositories as repo
    materia = repo.obtener_materia(id)
    if not materia:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    repo.db_materias.remove(materia)
    return {"mensaje": "Materia eliminada correctamente"}

@router.delete("/matriculas/{id}", tags=["Matriculas"])
def eliminar_matricula(id: int):
    from app import repositories as repo
    matricula = repo.obtener_matricula(id)
    if not matricula:
        raise HTTPException(status_code=404, detail="Matricula no encontrada")
    repo.db_matriculas.remove(matricula)
    return {"mensaje": "Matricula eliminada correctamente"}

# --- ACTUALIZACIONES ---
@router.put("/usuarios/{id}", tags=["Usuarios"])
def actualizar_usuario(id: int, u: Usuario):
    from app import repositories as repo
    usuario = repo.obtener_usuario(id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario.update(u.dict(exclude_unset=True))
    return usuario

@router.put("/estudiantes/{id}", tags=["Estudiantes"])
def actualizar_estudiante(id: int, e: Estudiante):
    from app import repositories as repo
    estudiante = repo.obtener_estudiante(id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    estudiante.update(e.dict(exclude_unset=True))
    return estudiante

@router.put("/materias/{id}", tags=["Materias"])
def actualizar_materia(id: int, m: Materia):
    from app import repositories as repo
    materia = repo.obtener_materia(id)
    if not materia:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    materia.update(m.dict(exclude_unset=True))
    return materia

# --- ESTADISTICAS ---
@router.get("/estadisticas", tags=["Estadisticas"])
def obtener_estadisticas():
    from app import repositories as repo
    return {
        "total_usuarios": len(repo.db_usuarios),
        "total_estudiantes": len(repo.db_estudiantes),
        "total_docentes": len(repo.db_docentes),
        "total_materias": len(repo.db_materias),
        "total_matriculas": len(repo.db_matriculas),
        "total_calificaciones": len(repo.db_calificaciones),
        "total_asistencias": len(repo.db_asistencias),
        "matriculas_por_estado": {
            "borrador": len([m for m in repo.db_matriculas if m["estado"] == "borrador"]),
            "pendiente": len([m for m in repo.db_matriculas if m["estado"] == "pendiente"]),
            "activa": len([m for m in repo.db_matriculas if m["estado"] == "activa"]),
            "rechazada": len([m for m in repo.db_matriculas if m["estado"] == "rechazada"]),
            "completada": len([m for m in repo.db_matriculas if m["estado"] == "completada"]),
            "anulada": len([m for m in repo.db_matriculas if m["estado"] == "anulada"])
        }
    }
    
    # --- REPORTES ---
@router.get("/matriculas/{id}/asistencia", tags=["Reportes"])
def reporte_asistencia(id: int):
    from app import repositories as repo
    matricula = repo.obtener_matricula(id)
    if not matricula:
        raise HTTPException(status_code=404, detail="Matricula no encontrada")
    asistencias = [a for a in repo.db_asistencias if a["id_matricula"] == id]
    total = len(asistencias)
    presentes = len([a for a in asistencias if a["presente"]])
    porcentaje = round((presentes / total * 100), 2) if total > 0 else 0
    return {
        "id_matricula": id,
        "total_clases": total,
        "clases_asistidas": presentes,
        "clases_faltadas": total - presentes,
        "porcentaje_asistencia": porcentaje,
        "estado": "aprobado" if porcentaje >= 70 else "reprobado"
    }

@router.get("/matriculas/{id}/calificacion", tags=["Reportes"])
def reporte_calificacion(id: int):
    from app import repositories as repo
    matricula = repo.obtener_matricula(id)
    if not matricula:
        raise HTTPException(status_code=404, detail="Matricula no encontrada")
    calificaciones = [c for c in repo.db_calificaciones if c["id_matricula"] == id]
    if not calificaciones:
        raise HTTPException(status_code=404, detail="No hay calificaciones para esta matricula")
    return {
        "id_matricula": id,
        "calificaciones": calificaciones
    }
    
    # --- BUSQUEDAS ESPECIALES ---
@router.get("/periodos/{id}/materias", tags=["Periodos"])
def materias_por_periodo(id: int):
    from app import repositories as repo
    materias = [m for m in repo.db_materias if m["id_periodo"] == id]
    if not materias:
        raise HTTPException(status_code=404, detail="No hay materias para este periodo")
    return materias

@router.get("/estudiantes/{id}/matriculas", tags=["Estudiantes"])
def matriculas_por_estudiante(id: int):
    from app import repositories as repo
    estudiante = repo.obtener_estudiante(id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    matriculas = [m for m in repo.db_matriculas if m["id_estudiante"] == id]
    return {
        "estudiante": estudiante,
        "matriculas": matriculas,
        "total": len(matriculas)
    }

@router.get("/docentes/{id}/materias", tags=["Docentes"])
def materias_por_docente(id: int):
    from app import repositories as repo
    materias = [m for m in repo.db_materias if m["id_docente"] == id]
    if not materias:
        raise HTTPException(status_code=404, detail="No hay materias para este docente")
    return materias