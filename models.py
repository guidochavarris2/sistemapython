from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

db = SQLAlchemy()
bcrypt = Bcrypt()

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False)

    def verificar_contrasena(self, contrasena):
        return bcrypt.check_password_hash(self.contrasena, contrasena)

class Computadora(db.Model):
    id = db.Column(db.Integer, primary_key=True)        
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

class Carpeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(30), nullable=False)
    tamaño = db.Column(db.String(30), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

class Silla(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    material = db.Column(db.String(50), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

class Motor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    potencia = db.Column(db.String(50), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
