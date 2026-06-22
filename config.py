from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Sistema de Gestión Académica (SGA)"
    version: str = "1.0.0"
    descripcion: str = "Backend del SGA desarrollado con FastAPI"
    nota_minima_aprobacion: float = 7.0
    porcentaje_asistencia_minimo: float = 70.0
    creditos_maximos_por_periodo: int = 25

settings = Settings()