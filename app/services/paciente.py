from sqlalchemy.orm import Session
from app.repositories import paciente as repo
from app.schemas.paciente import PacienteCreate

def registrar_paciente(db: Session, paciente: PacienteCreate):
    return repo.crear_paciente(db, paciente)

def listar_pacientes(db: Session, skip: int = 0, limit: int = 10):
    return repo.obtener_pacientes(db, skip=skip, limit=limit)

def obtener_paciente(db: Session, documento: int):
    return repo.obtener_paciente(db, documento=documento)

def eliminar_paciente(db: Session, documento: int):
    return repo.eliminar_paciente(db, documento=documento)
