# ProceedingsEventos

# Laboratorio 9(CLEAN CODE)
En este laboratorio, hemos implementado varias características siguiendo las convenciones y prácticas de codificación legible. A continuación se describen las prácticas aplicadas y se proporcionan fragmentos de código que ilustran su uso.

## Prácticas de Codificación Legible Aplicadas

1. Nombres Descriptivos:
Utilizamos nombres de variables y funciones que son descriptivos y reflejan claramente su propósito.

```python

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

```
2. Funciones Claras y Concisas:
Las funciones se diseñaron para realizar una única tarea y se mantuvieron lo más breves y concisas posible.

Funciones dentro de registrarse.py, son entendibles y cada una hace cosas diferentes.

```python

@registrarse_bp.route('/enviarRegistro', methods=['POST'])
def registro():
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    email = request.form['email']
    contrasenia = generate_password_hash(request.form['contrasenia'])

    nuevo_usuario = Usuario(nombres=nombres, apellidos=apellidos, email=email, contrasenia=contrasenia)

    try:
        if registrar_usuario(nuevo_usuario):
            session['usuario_id'] = nuevo_usuario.id
            return redirect(url_for('home_bp.home'))
        else:
            flash('El usuario ya existe', 'error')
            return redirect(url_for('registrarse_bp.register'))
    except Exception as e:
        flash(f'Ocurrió un error: {str(e)}', 'error')
        return redirect(url_for('registrarse_bp.register'))
```

## Convenciones de Codificación


Las convenciones de codificación de Python se han aplicado en todo el código, incluyendo:

Indentación: Se utiliza una indentación de 4 espacios.

Espacios en Blanco: Se dejan espacios en blanco alrededor de los operadores y después de las comas para mejorar la legibilidad.

Nombres de Clases y Métodos: Las clases usan el estilo PascalCase y los métodos usan el estilo snake_case.


# Laboratorio 10(SOLID)

Para este laboratorio, hemos aplicado tres principios SOLID en la implementación de nuestro código. A continuación se describen los principios aplicados y se proporcionan fragmentos de código que ilustran su uso.

## Principios SOLID Aplicados

1. Single Responsibility Principle (SRP):

Cada clase tiene una única responsabilidad y encapsula una parte bien definida de la lógica de la aplicación.

```python

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombres = db.Column(db.String(80))
    apellidos = db.Column(db.String(80))
    email = db.Column(db.String(120))
    fecha_nacimiento = db.Column(db.Date)
    nacionalidad = db.Column(db.String(120))
    contrasenia = db.Column(db.String(120))

    def __init__(self, nombres, apellidos, email, contrasenia):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.contrasenia = contrasenia

```

Cada modulo y clase en nuestro proyecto tiene una unica responsabilidad. Por ejemplo, index.py se encarga solo de cargar el proyecto.

2. Open/Closed Principle (OCP):

El código está diseñado para ser extensible sin necesidad de modificar las clases existentes.

```python

def registrar_usuario(usuario):
    try:
        existente = Usuario.query.filter_by(email=usuario.email).first()
        if existente:
            return False
        db.session.add(usuario)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(f"Error registrando usuario: {e}")
        return False

```
3. Dependency Inversion Principle (DIP):

El código depende de abstracciones y no de concreciones.

```python

@registrarse_bp.route('/enviarRegistro', methods=['POST'])
def registro():
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    email = request.form['email']
    contrasenia = generate_password_hash(request.form['contrasenia'])

    nuevo_usuario = Usuario(nombres=nombres, apellidos=apellidos, email=email, contrasenia=contrasenia)

    try:
        if registrar_usuario(nuevo_usuario):
            session['usuario_id'] = nuevo_usuario.id
            return redirect(url_for('home_bp.home'))
        else:
            flash('El usuario ya existe', 'error')
            return redirect(url_for('registrarse_bp.register'))
    except Exception as e:
        flash(f'Ocurrió un error: {str(e)}', 'error')
        return redirect(url_for('registrarse_bp.register'))

```

# Laboratorio 11

En este laboratorio, hemos aplicado tres estilos de programación diferentes. A continuación se describen los estilos aplicados y se proporcionan fragmentos de código que ilustran su uso.

## Estilos de Programación Aplicados

1. Error/Exception Handling:

Manejo de errores y excepciones para asegurar que el código se comporte correctamente incluso en condiciones inesperadas.

```python

def login():
    if request.method == 'POST':
        email = request.form['email']
        contrasenia = request.form['contrasenia']

        try:
            usuario = Usuario.query.filter_by(email=email).first()

            if usuario and check_password_hash(usuario.contrasenia, contrasenia):
                session['usuario_id'] = usuario.id
                return redirect(url_for('home_bp.home'))
            else:
                flash('Email o contraseña incorrectos', 'error')
        except Exception as e:
            flash(f'Ocurrió un error: {str(e)}', 'error')
            return redirect(url_for('inicio_sesion_bp.login'))

    return render_template('login.html')

```
2. Persistent-Tables:

Uso de tablas persistentes en una base de datos SQLAlchemy para almacenar y gestionar datos de usuarios.

```python

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombres = db.Column(db.String(80))
    apellidos = db.Column(db.String(80))
    email = db.Column(db.String(120))
    fecha_nacimiento = db.Column(db.Date)
    nacionalidad = db.Column(db.String(120))
    contrasenia = db.Column(db.String(120))

```
3. Cookbook:
Uso de un estilo de programación orientado a recetas o patrones bien definidos, como el patrón Blueprint de Flask para la organización de rutas y vistas.

```python

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.entidades.Usuario import Usuario
from utils.servicios.ServicioUsuario import registrar_usuario
from utils.repositorios.sqlAlchemy.conexionBd import db
from werkzeug.security import generate_password_hash

registrarse_bp = Blueprint('registrarse_bp', __name__, template_folder='../templates/vista/HTML')

@registrarse_bp.route('/')
def register():
    return render_template('registro.html')

@registrarse_bp.route('/enviarRegistro', methods=['POST'])
def registro():
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    email = request.form['email']
    contrasenia = generate_password_hash(request.form['contrasenia'])

    nuevo_usuario = Usuario(nombres=nombres, apellidos=apellidos, email=email, contrasenia=contrasenia)

    try:
        if registrar_usuario(nuevo_usuario):
            session['usuario_id'] = nuevo_usuario.id
            return redirect(url_for('home_bp.home'))
        else:
            flash('El usuario ya existe', 'error')
            return redirect(url_for('registrarse_bp.register'))
    except Exception as e:
        flash(f'Ocurrió un error: {str(e)}', 'error')
        return redirect(url_for('registrarse_bp.register'))

```

# Corrección de Bugs, Code Smells y Vulnerabilidades

Utilizamos la extensión/plugin SonarLint en nuestro IDE para identificar y corregir bugs, code smells y vulnerabilidades. Aseguramos que el código sea limpio y eficiente siguiendo las recomendaciones de SonarLint.





