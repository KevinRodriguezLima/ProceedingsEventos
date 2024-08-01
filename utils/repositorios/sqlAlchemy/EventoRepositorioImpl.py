from utils.repositorios.sqlAlchemy.conexionBd import db
from models.documentos.Evento import Evento

def agregar_evento(evento):
    try:
        db.session.add(evento)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error al agregar el evento: {str(e)}")

class EventoRepositorioImpl():
    pass