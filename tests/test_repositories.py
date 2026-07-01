import pytest
from datetime import date
from app.models import (
    Usuario, Estudiante, Docente, Materia,
    Matricula, Calificacion, Asistencia, PeriodoAcademico,
    RolEnum
)
from app import repositories as repo

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
def test_crear_usuario():
    u = Usuario(nombre="Juan", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)
    resultado = repo.crear_usuario(u)
    assert resultado["id"] == 1
    assert resultado["nombre"] == "Juan"

def test_obtener_usuarios():
    u = Usuario(nombre="Juan", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)
    repo.crear_usuario(u)
    assert len(repo.obtener_usuarios()) == 1

def test_obtener_usuario_por_id():
    u = Usuario(nombre="Juan", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)
    repo.crear_usuario(u)
    resultado = repo.obtener_usuario(1)
    assert resultado["nombre"] == "Juan"

def test_obtener_usuario_inexistente():
    resultado = repo.obtener_usuario(99)
    assert resultado is None

# --- ESTUDIANTES ---
def test_crear_estudiante():
    e = Estudiante(id_usuario=1, codigo="EST001", carrera="Computacion", semestre=3)
    resultado = repo.crear_estudiante(e)
    assert resultado["id"] == 1
    assert resultado["codigo"] == "EST001"

def test_obtener_estudiantes():
    e = Estudiante(id_usuario=1, codigo="EST001", carrera="Computacion", semestre=3)
    repo.crear_estudiante(e)
    assert len(repo.obtener_estudiantes()) == 1

def test_obtener_estudiante_inexistente():
    resultado = repo.obtener_estudiante(99)
    assert resultado is None

# --- DOCENTES ---
def test_crear_docente():
    d = Docente(id_usuario=1, titulo="Magister", especialidad="Software")
    resultado = repo.crear_docente(d)
    assert resultado["id"] == 1

def test_obtener_docentes():
    d = Docente(id_usuario=1, titulo="Magister", especialidad="Software")
    repo.crear_docente(d)
    assert len(repo.obtener_docentes()) == 1

# --- PERIODOS ---
def test_crear_periodo():
    p = PeriodoAcademico(nombre="2026-A", fecha_inicio=date(2026,1,1), fecha_fin=date(2026,6,30))
    resultado = repo.crear_periodo(p)
    assert resultado["id"] == 1

def test_obtener_periodos():
    p = PeriodoAcademico(nombre="2026-A", fecha_inicio=date(2026,1,1), fecha_fin=date(2026,6,30))
    repo.crear_periodo(p)
    assert len(repo.obtener_periodos()) == 1

# --- MATERIAS ---
def test_crear_materia():
    m = Materia(id_docente=1, id_periodo=1, nombre="Programacion", codigo="PRG01", creditos=4, cupo_max=30)
    resultado = repo.crear_materia(m)
    assert resultado["id"] == 1

def test_obtener_materias():
    m = Materia(id_docente=1, id_periodo=1, nombre="Programacion", codigo="PRG01", creditos=4, cupo_max=30)
    repo.crear_materia(m)
    assert len(repo.obtener_materias()) == 1

def test_obtener_materia_inexistente():
    resultado = repo.obtener_materia(99)
    assert resultado is None

# --- MATRICULAS ---
def test_crear_matricula():
    m = Matricula(id_estudiante=1, id_materia=1, id_periodo=1, fecha=date(2026,1,15))
    resultado = repo.crear_matricula(m)
    assert resultado["id"] == 1
    assert resultado["estado"] == "borrador"

def test_actualizar_estado_matricula():
    m = Matricula(id_estudiante=1, id_materia=1, id_periodo=1, fecha=date(2026,1,15))
    repo.crear_matricula(m)
    resultado = repo.actualizar_estado_matricula(1, "pendiente")
    assert resultado["estado"] == "pendiente"

def test_actualizar_estado_matricula_inexistente():
    resultado = repo.actualizar_estado_matricula(99, "pendiente")
    assert resultado is None

# --- CALIFICACIONES ---
def test_crear_calificacion():
    c = Calificacion(id_matricula=1, nota1=8.0, nota2=7.5, examen=9.0)
    resultado = repo.crear_calificacion(c)
    assert resultado["promedio"] == round((8.0 + 7.5 + 9.0) / 3, 2)
    assert resultado["estado"] == "aprobado"

def test_calificacion_reprobado():
    c = Calificacion(id_matricula=1, nota1=4.0, nota2=5.0, examen=3.0)
    resultado = repo.crear_calificacion(c)
    assert resultado["estado"] == "reprobado"

# --- ASISTENCIAS ---
def test_crear_asistencia():
    a = Asistencia(id_matricula=1, fecha=date(2026,1,15), presente=True)
    resultado = repo.crear_asistencia(a)
    assert resultado["id"] == 1
    assert resultado["presente"] == True

def test_obtener_asistencias():
    a = Asistencia(id_matricula=1, fecha=date(2026,1,15), presente=True)
    repo.crear_asistencia(a)
    assert len(repo.obtener_asistencias()) == 1