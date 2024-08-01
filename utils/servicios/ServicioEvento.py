from utils.repositorios.sqlAlchemy.EventoRepositorioImpl import agregar_evento
from utils.repositorios.sqlAlchemy.conexionBd import db

def registrar_evento(evento):
    try:
        agregar_evento(evento)
        return "Evento guardado exitosamente"
    except Exception as e:
        db.session.rollback()
        return f"Error al guardar el evento: {str(e)}"