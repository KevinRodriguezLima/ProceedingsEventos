from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from utils.servicios.ServicioUsuario import UsuarioServicio
from utils.repositorios.sqlAlchemy.conexionBd import db
from models.entidades.FabricaUsuario import FabricaUsuario  # Importa la fábrica

registrarse = Blueprint('registrarse', __name__, template_folder='../templates/vista/HTML')

@registrarse.route('/')
def home_register():
    return render_template('vista/assets/HTML/registro.html')

@registrarse.route('/enviarRegistro', methods=['POST'])
def registro():
    try:
        nombres = request.form['nombres'].strip()
        apellidos = request.form['apellidos'].strip()
        email = request.form['email'].strip()
        contrasenia = request.form['contrasenia'].strip()

        nuevo_usuario = FabricaUsuario.crear_usuario(nombres, apellidos, email, contrasenia)
        servicio_usuario = UsuarioServicio(nuevo_usuario)

        if not servicio_usuario.registrar_usuario():
            flash('El usuario ya existe')
            return redirect(url_for('registrarse.home_register'))
        
        session['usuario_id'] = servicio_usuario.obtener_id_usuario()
        return redirect(url_for('home.home_page'))

    except Exception as e:
        flash(f'Ocurrió un error: {str(e)}')
        return redirect(url_for('registrarse.home_register'))
