from fastapi import FastAPI
from app.routers import paciente
from app.routers import cita

app = FastAPI(title="Medical Office API")

app.include_router(paciente.router, prefix="/api", tags=["Pacientes"])
app.include_router(cita.router, prefix="/api", tags=["Citas"])
