from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.controllers import router

app = FastAPI(
    title="Sistema de Gestión Académica (SGA)",
    description="Backend del SGA desarrollado con FastAPI - Ingeniería de Software 2026",
    version="1.0.0"
)

# Manejador global de errores
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Error interno del servidor", "detalle": str(exc)}
    )

app.include_router(router, prefix="/api")

@app.get("/", tags=["Root"])
def root():
    return {
        "mensaje": "Bienvenido al SGA - Sistema de Gestión Académica",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health", tags=["Root"])
def health():
    return {"estado": "activo"}