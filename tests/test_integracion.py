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

def test_flujo_completo_matricula():
    # 1. Crear usuario estudiante
    u = client.post("/api/usuarios", json={"nombre": "Juan", "apellido": "Chevez", "email": "juan@gmail.com", "rol": "estudiante"})
    assert u.status_code == 200

    # 2. Crear estudiante
    e = client.post("/api/estudiantes", json={"id_usuario": 1, "codigo": "EST001", "carrera": "Computacion", "semestre": 3})
    assert e.status_code == 200

    # 3. Crear periodo
    p = client.post("/api/periodos", json={"nombre": "2026-A", "fecha_inicio": "2026-01-01", "fecha_fin": "2026-06-30"})
    assert p.status_code == 200

    # 4. Crear materia
    m = client.post("/api/materias", json={"id_docente": 1, "id_periodo": 1, "nombre": "Programacion", "codigo": "PRG01", "creditos": 4, "cupo_max": 30})
    assert m.status_code == 200

    # 5. Crear matricula
    mat = client.post("/api/matriculas", json={"id_estudiante": 1, "id_materia": 1, "id_periodo": 1, "fecha": "2026-01-15"})
    assert mat.status_code == 200
    assert mat.json()["estado"] == "borrador"

    # 6. Confirmar matricula
    conf = client.put("/api/matriculas/1/confirmar")
    assert conf.json()["estado"] == "pendiente"

    # 7. Aprobar matricula
    apr = client.put("/api/matriculas/1/aprobar")
    assert apr.json()["estado"] == "activa"

    # 8. Registrar asistencia
    a = client.post("/api/asistencias", json={"id_matricula": 1, "fecha": "2026-01-15", "presente": True})
    assert a.status_code == 200

    # 9. Registrar calificacion
    c = client.post("/api/calificaciones", json={"id_matricula": 1, "nota1": 8.0, "nota2": 7.5, "examen": 9.0})
    assert c.status_code == 200
    assert c.json()["estado"] == "aprobado"

    # 10. Verificar estadisticas
    est = client.get("/api/estadisticas")
    assert est.json()["total_matriculas"] == 1
    assert est.json()["matriculas_por_estado"]["activa"] == 1

def test_flujo_rechazo_matricula():
    # 1. Crear usuario y estudiante
    client.post("/api/usuarios", json={"nombre": "Pedro", "apellido": "Lopez", "email": "pedro@gmail.com", "rol": "estudiante"})
    client.post("/api/estudiantes", json={"id_usuario": 1, "codigo": "EST002", "carrera": "Computacion", "semestre": 2})
    client.post("/api/materias", json={"id_docente": 1, "id_periodo": 1, "nombre": "Matematicas", "codigo": "MAT01", "creditos": 3, "cupo_max": 25})

    # 2. Crear y rechazar matricula
    client.post("/api/matriculas", json={"id_estudiante": 1, "id_materia": 1, "id_periodo": 1, "fecha": "2026-01-15"})
    r = client.put("/api/matriculas/1/rechazar")
    assert r.json()["estado"] == "rechazada"

    # 3. Verificar estadisticas
    est = client.get("/api/estadisticas")
    assert est.json()["matriculas_por_estado"]["rechazada"] == 1