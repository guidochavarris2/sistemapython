from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from models import db, Usuario, Computadora, Carpeta, Silla, Motor
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos y bcrypt
db.init_app(app)
bcrypt = Bcrypt(app)

# Configurar LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/dashboard')
@login_required
def dashboard():
    total_computadoras = Computadora.query.count()
    total_carpetas = Carpeta.query.count()
    total_sillas = Silla.query.count()
    total_motores = Motor.query.count()
    
    return render_template('dashboard2.html', 
                           nombre=current_user.nombre,
                           total_computadoras=total_computadoras,
                           total_carpetas=total_carpetas,
                           total_sillas=total_sillas,
                           total_motores=total_motores)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')
        usuario = Usuario.query.filter_by(correo=correo).first()

        if usuario and bcrypt.check_password_hash(usuario.contrasena, contrasena):
            login_user(usuario)
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Inicio de sesión fallido. Verifica tus credenciales.', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('index'))

# Vistas CRUD para Computadoras
@app.route('/computadoras')
@login_required
def lista_computadoras():
    computadoras = Computadora.query.all()
    return render_template('computadoras.html', computadoras=computadoras)

@app.route('/computadora/<int:id>')
@login_required
def ver_computadora(id):
    computadora = Computadora.query.get_or_404(id)
    return render_template('ver_computadora.html', computadora=computadora)

@app.route('/agregar_computadora', methods=['GET', 'POST'])
@login_required
def agregar_computadora():
    if request.method == 'POST':
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        cantidad = request.form.get('cantidad')

        nueva_computadora = Computadora(marca=marca, modelo=modelo, cantidad=cantidad)
        db.session.add(nueva_computadora)
        db.session.commit()
        flash('Computadora agregada exitosamente', 'success')
        return redirect(url_for('lista_computadoras'))

    return render_template('agregar_computadora.html')

@app.route('/editar_computadora/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_computadora(id):
    computadora = Computadora.query.get_or_404(id)

    if request.method == 'POST':
        computadora.marca = request.form.get('marca')
        computadora.modelo = request.form.get('modelo')
        computadora.cantidad = request.form.get('cantidad')

        db.session.commit()
        flash('Computadora actualizada exitosamente', 'success')
        return redirect(url_for('lista_computadoras'))

    return render_template('editar_computadora.html', computadora=computadora)

@app.route('/eliminar_computadora/<int:id>', methods=['POST'])
@login_required
def eliminar_computadora(id):
    computadora = Computadora.query.get_or_404(id)
    db.session.delete(computadora)
    db.session.commit()
    flash('Computadora eliminada exitosamente', 'success')
    return redirect(url_for('lista_computadoras'))

# Vistas CRUD para Carpetas
@app.route('/carpetas')
@login_required
def lista_carpetas():
    carpetas = Carpeta.query.all()
    return render_template('carpetas.html', carpetas=carpetas)

@app.route('/carpeta/<int:id>')
@login_required
def ver_carpeta(id):
    carpeta = Carpeta.query.get_or_404(id)
    return render_template('ver_carpeta.html', carpeta=carpeta)

@app.route('/agregar_carpeta', methods=['GET', 'POST'])
@login_required
def agregar_carpeta():
    if request.method == 'POST':
        color = request.form.get('color')
        tamaño = request.form.get('tamaño')
        cantidad = request.form.get('cantidad')

        nueva_carpeta = Carpeta(color=color, tamaño=tamaño, cantidad=cantidad)
        db.session.add(nueva_carpeta)
        db.session.commit()
        flash('Carpeta agregada exitosamente', 'success')
        return redirect(url_for('lista_carpetas'))

    return render_template('agregar_carpeta.html')

@app.route('/editar_carpeta/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_carpeta(id):
    carpeta = Carpeta.query.get_or_404(id)

    if request.method == 'POST':
        carpeta.color = request.form.get('color')
        carpeta.tamaño = request.form.get('tamaño')
        carpeta.cantidad = request.form.get('cantidad')

        db.session.commit()
        flash('Carpeta actualizada exitosamente', 'success')
        return redirect(url_for('lista_carpetas'))

    return render_template('editar_carpeta.html', carpeta=carpeta)

@app.route('/eliminar_carpeta/<int:id>', methods=['POST'])
@login_required
def eliminar_carpeta(id):
    carpeta = Carpeta.query.get_or_404(id)
    db.session.delete(carpeta)
    db.session.commit()
    flash('Carpeta eliminada exitosamente', 'success')
    return redirect(url_for('lista_carpetas'))

# Vistas CRUD para Sillas
@app.route('/sillas')
@login_required
def lista_sillas():
    sillas = Silla.query.all()
    return render_template('sillas.html', sillas=sillas)

@app.route('/silla/<int:id>')
@login_required
def ver_silla(id):
    silla = Silla.query.get_or_404(id)
    return render_template('ver_silla.html', silla=silla)

@app.route('/agregar_silla', methods=['GET', 'POST'])
@login_required
def agregar_silla():
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        material = request.form.get('material')
        cantidad = request.form.get('cantidad')

        nueva_silla = Silla(tipo=tipo, material=material, cantidad=cantidad)
        db.session.add(nueva_silla)
        db.session.commit()
        flash('Silla agregada exitosamente', 'success')
        return redirect(url_for('lista_sillas'))

    return render_template('agregar_silla.html')

@app.route('/editar_silla/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_silla(id):
    silla = Silla.query.get_or_404(id)

    if request.method == 'POST':
        silla.tipo = request.form.get('tipo')
        silla.material = request.form.get('material')
        silla.cantidad = request.form.get('cantidad')

        db.session.commit()
        flash('Silla actualizada exitosamente', 'success')
        return redirect(url_for('lista_sillas'))

    return render_template('editar_silla.html', silla=silla)

@app.route('/eliminar_silla/<int:id>', methods=['POST'])
@login_required
def eliminar_silla(id):
    silla = Silla.query.get_or_404(id)
    db.session.delete(silla)
    db.session.commit()
    flash('Silla eliminada exitosamente', 'success')
    return redirect(url_for('lista_sillas'))

# Vistas CRUD para Motores
@app.route('/motores')
@login_required
def lista_motores():
    motores = Motor.query.all()
    return render_template('motores.html', motores=motores)

@app.route('/motor/<int:id>')
@login_required
def ver_motor(id):
    motor = Motor.query.get_or_404(id)
    return render_template('ver_motor.html', motor=motor)

@app.route('/agregar_motor', methods=['GET', 'POST'])
@login_required
def agregar_motor():
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        potencia = request.form.get('potencia')
        cantidad = request.form.get('cantidad')

        nuevo_motor = Motor(tipo=tipo, potencia=potencia, cantidad=cantidad)
        db.session.add(nuevo_motor)
        db.session.commit()
        flash('Motor agregado exitosamente', 'success')
        return redirect(url_for('lista_motores'))

    return render_template('agregar_motor.html')

@app.route('/editar_motor/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_motor(id):
    motor = Motor.query.get_or_404(id)

    if request.method == 'POST':
        motor.tipo = request.form.get('tipo')
        motor.potencia = request.form.get('potencia')
        motor.cantidad = request.form.get('cantidad')

        db.session.commit()
        flash('Motor actualizado exitosamente', 'success')
        return redirect(url_for('lista_motores'))

    return render_template('editar_motor.html', motor=motor)

@app.route('/eliminar_motor/<int:id>', methods=['POST'])
@login_required
def eliminar_motor(id):
    motor = Motor.query.get_or_404(id)
    db.session.delete(motor)
    db.session.commit()
    flash('Motor eliminado exitosamente', 'success')
    return redirect(url_for('lista_motores'))

# Vistas CRUD para Usuarios
@app.route('/usuarios')
@login_required
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/usuario/<int:id>')
@login_required
def ver_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return render_template('ver_usuario.html', usuario=usuario)

@app.route('/usuarios/crear', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')
        rol = 'usuario'  # Puedes cambiar esto según la lógica de tu aplicación

        # Encriptar la contraseña con bcrypt
        hashed_password = bcrypt.generate_password_hash(contrasena).decode('utf-8')

        # Crear el nuevo usuario
        nuevo_usuario = Usuario(nombre=nombre, correo=correo, contrasena=hashed_password, rol=rol)

        # Guardar el usuario en la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('Usuario registrado exitosamente', 'success')
        return redirect(url_for('listar_usuarios'))

    return render_template('agregar_usuario.html')

@app.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)

    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.correo = request.form['correo']

        # Solo actualizar la contraseña si se ha ingresado una nueva
        nueva_contrasena = request.form.get('contrasena')
        if nueva_contrasena:
            usuario.contrasena = bcrypt.generate_password_hash(nueva_contrasena).decode('utf-8')

        usuario.rol = request.form.get('rol')

        try:
            db.session.commit()
            flash('Usuario actualizado exitosamente.')
            return redirect(url_for('listar_usuarios'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar el usuario: {str(e)}')

    return render_template('editar_usuario.html', usuario=usuario)

@app.route('/usuarios/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado exitosamente', 'success')
    return redirect(url_for('listar_usuarios'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
