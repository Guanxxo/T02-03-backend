import pytest
from datetime import date
from app.models import (
    Usuario, Estudiante, Docente, Materia,
    Matricula, Calificacion, Asistencia, PeriodoAcademico,
    RolEnum, EstadoMatriculaEnum, EstadoCalificacionEnum
)

# --- TESTS USUARIO ---
def test_crear_usuario_valido():
    u = Usuario(nombre="Juan", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)
    assert u.nombre == "Juan"
    assert u.rol == RolEnum.estudiante

def test_usuario_email_invalido():
    with pytest.raises(Exception):
        Usuario(nombre="Juan", apellido="Chevez", email="correo-invalido", rol=RolEnum.estudiante)

def test_usuario_nombre_muy_corto():
    with pytest.raises(Exception):
        Usuario(nombre="J", apellido="Chevez", email="juan@gmail.com", rol=RolEnum.estudiante)

# --- TESTS ESTUDIANTE ---
def test_crear_estudiante_valido():
    e = Estudiante(id_usuario=1, codigo="EST001", carrera="Computacion", semestre=3)
    assert e.codigo == "EST001"
    assert e.creditos_aprobados == 0

def test_estudiante_semestre_invalido():
    with pytest.raises(Exception):
        Estudiante(id_usuario=1, codigo="EST001", carrera="Computacion", semestre=11)

def test_estudiante_semestre_minimo():
    with pytest.raises(Exception):
        Estudiante(id_usuario=1, codigo="EST001", carrera="Computacion", semestre=0)

# --- TESTS DOCENTE ---
def test_crear_docente_valido():
    d = Docente(id_usuario=2, titulo="Magister", especialidad="Ingenieria de Software")
    assert d.titulo == "Magister"

def test_docente_titulo_muy_corto():
    with pytest.raises(Exception):
        Docente(id_usuario=2, titulo="M", especialidad="Ingenieria de Software")

# --- TESTS PERIODO ACADEMICO ---
def test_crear_periodo_valido():
    p = PeriodoAcademico(nombre="2026-A", fecha_inicio=date(2026,1,1), fecha_fin=date(2026,6,30))
    assert p.nombre == "2026-A"

def test_periodo_fecha_fin_menor():
    with pytest.raises(Exception):
        PeriodoAcademico(nombre="2026-A", fecha_inicio=date(2026,6,1), fecha_fin=date(2026,1,1))

# --- TESTS MATERIA ---
def test_crear_materia_valida():
    m = Materia(id_docente=1, id_periodo=1, nombre="Programacion", codigo="PRG01", creditos=4, cupo_max=30)
    assert m.nombre == "Programacion"
    assert m.creditos == 4

def test_materia_creditos_invalidos():
    with pytest.raises(Exception):
        Materia(id_docente=1, id_periodo=1, nombre="Programacion", codigo="PRG01", creditos=0, cupo_max=30)

# --- TESTS MATRICULA ---
def test_crear_matricula_valida():
    m = Matricula(id_estudiante=1, id_materia=1, id_periodo=1, fecha=date(2026,1,15))
    assert m.estado == EstadoMatriculaEnum.borrador

def test_matricula_estado_default():
    m = Matricula(id_estudiante=1, id_materia=1, id_periodo=1, fecha=date(2026,1,15))
    assert m.estado == "borrador"

# --- TESTS CALIFICACION ---
def test_crear_calificacion_valida():
    c = Calificacion(id_matricula=1, nota1=8.0, nota2=7.5, examen=9.0)
    assert c.nota1 == 8.0

def test_calificacion_nota_fuera_rango():
    with pytest.raises(Exception):
        Calificacion(id_matricula=1, nota1=11.0, nota2=7.5, examen=9.0)

def test_calificacion_nota_negativa():
    with pytest.raises(Exception):
        Calificacion(id_matricula=1, nota1=-1.0, nota2=7.5, examen=9.0)

# --- TESTS ASISTENCIA ---
def test_crear_asistencia_valida():
    a = Asistencia(id_matricula=1, fecha=date(2026,1,15), presente=True)
    assert a.presente == True
    assert a.justificada == False

def test_asistencia_no_presente():
    a = Asistencia(id_matricula=1, fecha=date(2026,1,15), presente=False, justificada=True)
    assert a.presente == False
    assert a.justificada == True