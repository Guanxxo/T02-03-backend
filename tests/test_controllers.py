import pytest
from fastapi.testclient import TestClient
from main import app
from app import repositories as repo

client = TestClient(app)

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

# --- ROOT ---
def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "SGA" in r.json()["mensaje"]

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["estado"] == "activo"

# --- USUARIOS ---
def test_crear_usuario():
    r = client.post("/api/usuarios", json={"nombre": "Juan", "apellido": "Chevez", "email": "juan@gmail.com", "rol": "estudiante"})
    assert r.status_code == 200
    assert r.json()["nombre"] == "Juan"

def test_listar_usuarios():
    client.post("/api/usuarios", json={"nombre": "Juan", "apellido": "Chevez", "email": "juan@gmail.com", "rol": "estudiante"})
    r = client.get("/api/usuarios")
    assert r.status_code == 200
    assert len(r.json()) == 1

def test_obtener_usuario_por_id():
    client.post("/api/usuarios", json={"nombre": "Juan", "apellido": "Chevez", "email": "juan@gmail.com", "rol": "estudiante"})
    r = client.get("/api/usuarios/1")
    assert r.status_code == 200

def test_obtener_usuario_inexistente():
    r = client.get("/api/usuarios/99")
    assert r.status_code == 404

def test_actualizar_usuario():
    client.post("/api/usuarios", json={"nombre": "Juan", "apellido": "Chevez", "email": "juan@gmail.com", "rol": "estudiante"})
    r = client.put("/api/usuarios/1", json={"nombre": "Pedro", "apellido": "Chevez", "email": "pedro@gmail.com", "rol": "estudiante"})
    assert r.status_code == 200

def test_eliminar_usuario():
    client.post("/api/usuarios", json={"nombre": "Juan", "apellido": "Chevez", "email": "juan@gmail.com", "rol": "estudiante"})
    r = client.delete("/api/usuarios/1")
    assert r.status_code == 200

def test_eliminar_usuario_inexistente():
    r = client.delete("/api/usuarios/99")
    assert r.status_code == 404

# --- ESTUDIANTES ---
def test_crear_estudiante():
    client.post("/api/usuarios", json={"nombre": "Juan", "apellido": "Chevez", "email": "juan@gmail.com", "rol": "estudiante"})
    r = client.post("/api/estudiantes", json={"id_usuario": 1, "codigo": "EST001", "carrera": "Computacion", "semestre": 3})
    assert r.status_code == 200

def test_listar_estudiantes():
    r = client.get("/api/estudiantes")
    assert r.status_code == 200

def test_obtener_estudiante_inexistente():
    r = client.get("/api/estudiantes/99")
    assert r.status_code == 404

def test_eliminar_estudiante():
    client.post("/api/usuarios", json={"nombre": "Juan", "apellido": "Chevez", "email": "juan@gmail.com", "rol": "estudiante"})
    client.post("/api/estudiantes", json={"id_usuario": 1, "codigo": "EST001", "carrera": "Computacion", "semestre": 3})
    r = client.delete("/api/estudiantes/1")
    assert r.status_code == 200

def test_eliminar_estudiante_inexistente():
    r = client.delete("/api/estudiantes/99")
    assert r.status_code == 404

# --- DOCENTES ---
def test_crear_docente():
    client.post("/api/usuarios", json={"nombre": "Maria", "apellido": "Lopez", "email": "maria@gmail.com", "rol": "docente"})
    r = client.post("/api/docentes", json={"id_usuario": 1, "titulo": "Magister", "especialidad": "Software"})
    assert r.status_code == 200

def test_listar_docentes():
    r = client.get("/api/docentes")
    assert r.status_code == 200

# --- PERIODOS ---
def test_crear_periodo():
    r = client.post("/api/periodos", json={"nombre": "2026-A", "fecha_inicio": "2026-01-01", "fecha_fin": "2026-06-30"})
    assert r.status_code == 200

def test_listar_periodos():
    r = client.get("/api/periodos")
    assert r.status_code == 200

# --- MATERIAS ---
def test_crear_materia():
    r = client.post("/api/materias", json={"id_docente": 1, "id_periodo": 1, "nombre": "Programacion", "codigo": "PRG01", "creditos": 4, "cupo_max": 30})
    assert r.status_code == 200

def test_listar_materias():
    r = client.get("/api/materias")
    assert r.status_code == 200

def test_obtener_materia_inexistente():
    r = client.get("/api/materias/99")
    assert r.status_code == 404

def test_eliminar_materia():
    client.post("/api/materias", json={"id_docente": 1, "id_periodo": 1, "nombre": "Programacion", "codigo": "PRG01", "creditos": 4, "cupo_max": 30})
    r = client.delete("/api/materias/1")
    assert r.status_code == 200

def test_eliminar_materia_inexistente():
    r = client.delete("/api/materias/99")
    assert r.status_code == 404

# --- MATRICULAS ---
def test_crear_matricula():
    client.post("/api/usuarios", json={"nombre": "Juan", "apellido": "Chevez", "email": "juan@gmail.com", "rol": "estudiante"})
    client.post("/api/estudiantes", json={"id_usuario": 1, "codigo": "EST001", "carrera": "Computacion", "semestre": 3})
    client.post("/api/materias", json={"id_docente": 1, "id_periodo": 1, "nombre": "Programacion", "codigo": "PRG01", "creditos": 4, "cupo_max": 30})
    r = client.post("/api/matriculas", json={"id_estudiante": 1, "id_materia": 1, "id_periodo": 1, "fecha": "2026-01-15"})
    assert r.status_code == 200
    assert r.json()["estado"] == "borrador"

def test_listar_matriculas():
    r = client.get("/api/matriculas")
    assert r.status_code == 200

def test_obtener_matricula_inexistente():
    r = client.get("/api/matriculas/99")
    assert r.status_code == 404

def test_confirmar_matricula():
    client.post("/api/usuarios", json={"nombre": "Juan", "apellido": "Chevez", "email": "juan@gmail.com", "rol": "estudiante"})
    client.post("/api/estudiantes", json={"id_usuario": 1, "codigo": "EST001", "carrera": "Computacion", "semestre": 3})
    client.post("/api/materias", json={"id_docente": 1, "id_periodo": 1, "nombre": "Programacion", "codigo": "PRG01", "creditos": 4, "cupo_max": 30})
    client.post("/api/matriculas", json={"id_estudiante": 1, "id_materia": 1, "id_periodo": 1, "fecha": "2026-01-15"})
    r = client.put("/api/matriculas/1/confirmar")
    assert r.status_code == 200
    assert r.json()["estado"] == "pendiente"

def test_aprobar_matricula():
    client.post("/api/usuarios", json={"nombre": "Juan", "apellido": "Chevez", "email": "juan@gmail.com", "rol": "estudiante"})
    client.post("/api/estudiantes", json={"id_usuario": 1, "codigo": "EST001", "carrera": "Computacion", "semestre": 3})
    client.post("/api/materias", json={"id_docente": 1, "id_periodo": 1, "nombre": "Programacion", "codigo": "PRG01", "creditos": 4, "cupo_max": 30})
    client.post("/api/matriculas", json={"id_estudiante": 1, "id_materia": 1, "id_periodo": 1, "fecha": "2026-01-15"})
    client.put("/api/matriculas/1/confirmar")
    r = client.put("/api/matriculas/1/aprobar")
    assert r.status_code == 200
    assert r.json()["estado"] == "activa"

def test_rechazar_matricula():
    client.post("/api/usuarios", json={"nombre": "Juan", "apellido": "Chevez", "email": "juan@gmail.com", "rol": "estudiante"})
    client.post("/api/estudiantes", json={"id_usuario": 1, "codigo": "EST001", "carrera": "Computacion", "semestre": 3})
    client.post("/api/materias", json={"id_docente": 1, "id_periodo": 1, "nombre": "Programacion", "codigo": "PRG01", "creditos": 4, "cupo_max": 30})
    client.post("/api/matriculas", json={"id_estudiante": 1, "id_materia": 1, "id_periodo": 1, "fecha": "2026-01-15"})
    r = client.put("/api/matriculas/1/rechazar")
    assert r.status_code == 200

def test_estadisticas():
    r = client.get("/api/estadisticas")
    assert r.status_code == 200
    assert "total_usuarios" in r.json()