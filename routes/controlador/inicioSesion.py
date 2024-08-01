# routes/controlador/inicioSesion.py
from flask import Blueprint, render_template, request, redirect, url_for, session
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
            return redirect(url_for('home.home_page'))

    return render_template('vista/assets/HTML/login.html')

@inicio_sesion.route('/logout')
def logout():
    session.pop('usuario_id', None)
    return redirect(url_for('home.home_page'))
