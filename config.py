import os

class Config:
    SECRET_KEY = 'f3e4b2c6e1a7b8d9c0a1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3'  # Clave secreta generada
    SQLALCHEMY_DATABASE_URI = 'mysql://ud9xqngyeotcnadg:M2LL7HY2UNl8NaDyMevu@b2y6evewizmxjaq6f4tf-mysql.services.clever-cloud.com:3306/b2y6evewizmxjaq6f4tf'  # Cambiar según la configuración de tu BD
    SQLALCHEMY_TRACK_MODIFICATIONS = False