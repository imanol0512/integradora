from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from models.db import get_connection  # Corregimos la importación del módulo db
from models.usuario import Usuario

app = Flask(__name__)
app.secret_key = 'B!1w8NAt1T^%kvhUI*S^'

csrf = CSRFProtect(app)
db = get_connection()  # Obtenemos la conexión a la base de datos

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(idusuario):
    return Usuario.__get__(idusuario)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombreusuario = request.form.get('nombreusuario')
        contrasena = request.form.get('contrasena')
        
        # Verificar si se enviaron los campos requeridos
        if not nombreusuario or not contrasena:
            flash('Por favor, ingresa el nombre de usuario y contraseña.', 'error')
            return redirect(url_for('login'))

        usuario = Usuario.get_by_password(nombreusuario, contrasena)

        if not usuario:
            flash('Usuario y/o contraseña incorrectos. Intenta de nuevo.', 'error')
            return redirect(url_for('login'))

        login_user(usuario)
        return redirect(url_for('home'))
    else:
        return render_template('usuario/inicioSesion.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(debug=True)
