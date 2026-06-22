from fastapi import FastAPI
from app.controllers import router

app = FastAPI(
    title="Sistema de Gestión Académica (SGA)",
    description="Backend del SGA desarrollado con FastAPI - Ingeniería de Software 2026",
    version="1.0.0"
)

app.include_router(router, prefix="/api")

@app.get("/", tags=["Root"])
def root():
    return {"mensaje": "Bienvenido al SGA - Sistema de Gestión Académica"}