from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.documentos.Evento import Evento
from utils.servicios.ServicioEvento import registrar_evento
from utils.repositorios.sqlAlchemy.EventoRepositorioImpl import agregar_evento
from utils.repositorios.sqlAlchemy.conexionBd import db
from models.documentos.FabricaDocumento import FabricaDocumento

administrador = Blueprint('administrador', __name__, template_folder='../templates/vista/HTML')

@administrador.route('/dashboard', methods=['GET'])
def dashboard():
    eventos = Evento.query.all()
    return render_template('vista/assets/HTML/admin_eventos.html', eventos=eventos)

@administrador.route('/crear_evento', methods=['POST'])
def crear_evento():
    try:
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        autores = request.form['autores']
        responsables = request.form['responsables']
        
        resumen = request.form['resumen']
        datos = request.form['datos']
        conclusion = request.form['conclusion']
        num_pag = request.form['num_pag']
    
        evento = Evento(
            nombre=nombre,
            descripcion=descripcion,
            autores=autores,
            responsables=responsables
        )
        db.session.add(evento)
        db.session.commit()  
        
        fabrica_documento = FabricaDocumento()
        documento = fabrica_documento.crear_documento(
            resumen=resumen,
            datos=datos,
            conclusion=conclusion,
            num_pag=num_pag,
            evento_id=evento.id 
        )
        db.session.add(documento)
        db.session.commit()
        
        flash('Evento creado exitosamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al crear el evento: {str(e)}', 'error')
    return redirect(url_for(DASHBOARD_URL))

@administrador.route('/crear_evento_form', methods=['GET'])
def crear_evento_form():
    return render_template('vista/assets/HTML/crear_evento.html')

@administrador.route('/editar_evento/<int:id>', methods=['GET', 'POST'])
def editar_evento(id):
    evento = Evento.query.get_or_404(id)
    if request.method == 'POST':
        evento.nombre = request.form['nombre']
        evento.descripcion = request.form['descripcion']
        evento.autores = request.form['autores']
        evento.responsables = request.form['responsables']
        db.session.commit()
        flash('Evento actualizado exitosamente', 'success')
        return redirect(url_for('administrador.dashboard'))
    return render_template('vista/assets/HTML/editar_evento.html', evento=evento)

@administrador.route('/eliminar_evento/<int:id>', methods=['POST'])
def eliminar_evento(id):
    evento = Evento.query.get_or_404(id)
    db.session.delete(evento)
    db.session.commit()
    flash('Evento eliminado exitosamente', 'success')
    return redirect(url_for('administrador.dashboard'))
