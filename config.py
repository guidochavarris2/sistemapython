import os

class Config:
    SECRET_KEY = 'mi_secreto_super_secreto'  # Clave secreta para Flask (modificar para producción)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/inventario_instituto'  # Cambiar según la configuración de tu BD
    SQLALCHEMY_TRACK_MODIFICATIONS = False