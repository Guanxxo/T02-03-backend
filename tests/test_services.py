import pytest
from datetime import date
from app.models import (
    Usuario, Estudiante, Docente, Materia,
    Matricula, Calificacion, Asistencia, PeriodoAcademico,
    RolEnum
)
from app import repositories as repo
from app import services as svc

@pytest.fixture(autouse=True)
def limpiar_db():
    repo.db_usuarios.clear()
    repo.db_estudiantes.clear()
    repo.db_docentes.clear()
    repo.db_materias.clear()
    repo.db_matriculas.clear()
    repo.db_calificaciones.clear()
    repo.db_asistencias.clear()
    repo.db_periodos.clear()
    repo.contadores.update({"usuario": 1, "estudiante": 1, "docente": 1,
                            "materia": 1, "matricula": 1, "calificacion": 1,
                            "asistencia": 1, "periodo": 1})

# --- USUARIOS ---
def test_service_crear_usuario():
    u = Usuario(nombre="Juan", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)
    resultado = svc.crear_usuario(u)
    assert resultado["nombre"] == "Juan"

def test_service_listar_usuarios():
    u = Usuario(nombre="Juan", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)
    svc.crear_usuario(u)
    assert len(svc.listar_usuarios()) == 1

# --- ESTUDIANTES ---
def test_service_crear_estudiante_valido():
    u = Usuario(nombre="Juan", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)
    svc.crear_usuario(u)
    e = Estudiante(id_usuario=1, codigo="EST001", carrera="Computacion", semestre=3)
    resultado = svc.crear_estudiante(e)
    assert resultado["codigo"] == "EST001"

def test_service_crear_estudiante_usuario_inexistente():
    e = Estudiante(id_usuario=99, codigo="EST001", carrera="Computacion", semestre=3)
    with pytest.raises(ValueError, match="El usuario no existe"):
        svc.crear_estudiante(e)

def test_service_listar_estudiantes():
    u = Usuario(nombre="Juan", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)
    svc.crear_usuario(u)
    e = Estudiante(id_usuario=1, codigo="EST001", carrera="Computacion", semestre=3)
    svc.crear_estudiante(e)
    assert len(svc.listar_estudiantes()) == 1

# --- DOCENTES ---
def test_service_crear_docente_valido():
    u = Usuario(nombre="Maria", apellido="Lopez", email="maria@gmail.com", rol=RolEnum.docente)
    svc.crear_usuario(u)
    d = Docente(id_usuario=1, titulo="Magister", especialidad="Software")
    resultado = svc.crear_docente(d)
    assert resultado["titulo"] == "Magister"

def test_service_crear_docente_usuario_inexistente():
    d = Docente(id_usuario=99, titulo="Magister", especialidad="Software")
    with pytest.raises(ValueError, match="El usuario no existe"):
        svc.crear_docente(d)

# --- PERIODOS ---
def test_service_crear_periodo():
    p = PeriodoAcademico(nombre="2026-A", fecha_inicio=date(2026,1,1), fecha_fin=date(2026,6,30))
    resultado = svc.crear_periodo(p)
    assert resultado["nombre"] == "2026-A"

def test_service_listar_periodos():
    p = PeriodoAcademico(nombre="2026-A", fecha_inicio=date(2026,1,1), fecha_fin=date(2026,6,30))
    svc.crear_periodo(p)
    assert len(svc.listar_periodos()) == 1

# --- MATERIAS ---
def test_service_crear_materia():
    m = Materia(id_docente=1, id_periodo=1, nombre="Programacion", codigo="PRG01", creditos=4, cupo_max=30)
    resultado = svc.crear_materia(m)
    assert resultado["nombre"] == "Programacion"

def test_service_listar_materias():
    m = Materia(id_docente=1, id_periodo=1, nombre="Programacion", codigo="PRG01", creditos=4, cupo_max=30)
    svc.crear_materia(m)
    assert len(svc.listar_materias()) == 1

# --- MATRICULAS ---
def test_service_crear_matricula_valida():
    u = Usuario(nombre="Juan", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)
    svc.crear_usuario(u)
    e = Estudiante(id_usuario=1, codigo="EST001", carrera="Computacion", semestre=3)
    svc.crear_estudiante(e)
    m = Materia(id_docente=1, id_periodo=1, nombre="Programacion", codigo="PRG01", creditos=4, cupo_max=30)
    svc.crear_materia(m)
    mat = Matricula(id_estudiante=1, id_materia=1, id_periodo=1, fecha=date(2026,1,15))
    resultado = svc.crear_matricula(mat)
    assert resultado["estado"] == "borrador"

def test_service_crear_matricula_estudiante_inexistente():
    mat = Matricula(id_estudiante=99, id_materia=1, id_periodo=1, fecha=date(2026,1,15))
    with pytest.raises(ValueError, match="El estudiante no existe"):
        svc.crear_matricula(mat)

def test_service_crear_matricula_materia_inexistente():
    u = Usuario(nombre="Juan", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)
    svc.crear_usuario(u)
    e = Estudiante(id_usuario=1, codigo="EST001", carrera="Computacion", semestre=3)
    svc.crear_estudiante(e)
    mat = Matricula(id_estudiante=1, id_materia=99, id_periodo=1, fecha=date(2026,1,15))
    with pytest.raises(ValueError, match="La materia no existe"):
        svc.crear_matricula(mat)

def test_service_confirmar_matricula():
    u = Usuario(nombre="Juan", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)
    svc.crear_usuario(u)
    e = Estudiante(id_usuario=1, codigo="EST001", carrera="Computacion", semestre=3)
    svc.crear_estudiante(e)
    m = Materia(id_docente=1, id_periodo=1, nombre="Programacion", codigo="PRG01", creditos=4, cupo_max=30)
    svc.crear_materia(m)
    mat = Matricula(id_estudiante=1, id_materia=1, id_periodo=1, fecha=date(2026,1,15))
    svc.crear_matricula(mat)
    resultado = svc.confirmar_matricula(1)
    assert resultado["estado"] == "pendiente"

def test_service_aprobar_matricula():
    u = Usuario(nombre="Juan", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)
    svc.crear_usuario(u)
    e = Estudiante(id_usuario=1, codigo="EST001", carrera="Computacion", semestre=3)
    svc.crear_estudiante(e)
    m = Materia(id_docente=1, id_periodo=1, nombre="Programacion", codigo="PRG01", creditos=4, cupo_max=30)
    svc.crear_materia(m)
    mat = Matricula(id_estudiante=1, id_materia=1, id_periodo=1, fecha=date(2026,1,15))
    svc.crear_matricula(mat)
    svc.confirmar_matricula(1)
    resultado = svc.aprobar_matricula(1)
    assert resultado["estado"] == "activa"

def test_service_rechazar_matricula():
    u = Usuario(nombre="Juan", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)
    svc.crear_usuario(u)
    e = Estudiante(id_usuario=1, codigo="EST001", carrera="Computacion", semestre=3)
    svc.crear_estudiante(e)
    m = Materia(id_docente=1, id_periodo=1, nombre="Programacion", codigo="PRG01", creditos=4, cupo_max=30)
    svc.crear_materia(m)
    mat = Matricula(id_estudiante=1, id_materia=1, id_periodo=1, fecha=date(2026,1,15))
    svc.crear_matricula(mat)
    resultado = svc.rechazar_matricula(1)
    assert resultado["estado"] == "rechazada"

# --- CALIFICACIONES ---
def test_service_crear_calificacion_valida():
    mat = Matricula(id_estudiante=1, id_materia=1, id_periodo=1, fecha=date(2026,1,15))
    repo.crear_matricula(mat)
    c = Calificacion(id_matricula=1, nota1=8.0, nota2=7.5, examen=9.0)
    resultado = svc.crear_calificacion(c)
    assert resultado["estado"] == "aprobado"

def test_service_crear_calificacion_matricula_inexistente():
    c = Calificacion(id_matricula=99, nota1=8.0, nota2=7.5, examen=9.0)
    with pytest.raises(ValueError, match="La matrícula no existe"):
        svc.crear_calificacion(c)

# --- ASISTENCIAS ---
def test_service_crear_asistencia_valida():
    mat = Matricula(id_estudiante=1, id_materia=1, id_periodo=1, fecha=date(2026,1,15))
    repo.crear_matricula(mat)
    a = Asistencia(id_matricula=1, fecha=date(2026,1,15), presente=True)
    resultado = svc.crear_asistencia(a)
    assert resultado["presente"] == True

def test_service_crear_asistencia_matricula_inexistente():
    a = Asistencia(id_matricula=99, fecha=date(2026,1,15), presente=True)
    with pytest.raises(ValueError, match="La matrícula no existe"):
        svc.crear_asistencia(a)