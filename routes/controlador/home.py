# routes/controlador/home.py
from flask import Blueprint, render_template
from models.documentos.Evento import Evento
from models.documentos.Noticias import Noticias

home = Blueprint('home', __name__, template_folder='../templates/vista/HTML')

@home.route('/')
def home_page():
    eventos = Evento.query.all()  # Obtener todos los eventos
    noticias = Noticias.query.all()
    return render_template('vista/assets/HTML/home.html', eventos=eventos, noticias=noticias)

@home.route('/evento/<int:evento_id>')
def detalle_evento(evento_id):
    evento = Evento.query.get(evento_id)
    if evento:
        return render_template('vista/assets/HTML/detalle_evento.html', evento=evento)
    else:
        return "Evento no encontrado", 404

        