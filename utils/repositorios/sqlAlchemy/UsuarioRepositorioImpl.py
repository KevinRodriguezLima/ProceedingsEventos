
from utils.repositorios.sqlAlchemy.conexionBd import db
from models.entidades.Usuario import Usuario
from werkzeug.security import check_password_hash

class UsuarioRepositorioImpl:

    def __init__(self, usuario = None):
        self.usuario = usuario

    def agregar_usuario_bd(self):
        db.session.add(self.usuario)
        db.session.commit()

    def verificar_usuario_bd(self):
        usuario_db = db.session.query(Usuario).filter_by(nombres=self.usuario.nombres, 
                                                         apellidos=self.usuario.apellidos, 
                                                         email=self.usuario.email).first()
        return usuario_db is None

    def recuperar_usuario_by_email(self, email):
        self.usuario = db.session.query(Usuario).filter_by(email=email).first()

    def consultar_usuario(self):
        if self.usuario is None:
            return None
        return self.usuario
    
    def verificar_contrasenia(self, contrasenia):
        return check_password_hash(self.usuario.contrasenia, contrasenia)