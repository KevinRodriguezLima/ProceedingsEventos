from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.entidades.Usuario import Usuario
from utils.servicios.ServicioUsuario import UsuarioServicio

inicio_sesion = Blueprint('inicio_sesion', __name__, template_folder='../templates/vista/HTML')

@inicio_sesion.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        contrasenia = request.form['contrasenia']

        servicio_usuario = UsuarioServicio()
        
        if servicio_usuario.loggear_usuario(email, contrasenia):
            session['usuario_id'] = servicio_usuario.obtener_id_usuario()
            if servicio_usuario.es_admin():
                return redirect(url_for('administrador.dashboard'))
            else:
                return redirect(url_for('home.home_page'))
        else:
            flash('Email o contraseña incorrectos')
            return redirect(url_for('inicio_sesion.login'))

    return render_template('vista/assets/HTML/login.html')


@inicio_sesion.route('/logout')
def logout():
    session.pop('usuario_id', None)
    return redirect(url_for('home.home_page'))
