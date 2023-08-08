from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, login_required
from forms.usuario_forms import LoginForm
from models.db import get_connection
from models.usuario import Usuario

app = Flask(__name__)
app.secret_key = 'B!1w8NAt1T^%kvhUI*S^'
csrf = CSRFProtect(app)
db = get_connection()
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(idusuario):
    return Usuario.get_by_id(idusuario)

@app.route('/')
def index():
    return render_template('index/index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        nombreusuario = form.nombreusuario.data
        contrasena = form.contrasena.data
        usuario = Usuario.get_by_password(nombreusuario, contrasena)

        if not usuario:
            flash('Usuario y/o contraseña incorrectos. Intenta de nuevo.', 'error')
            return redirect(url_for('login'))

        login_user(usuario)
        if usuario.is_admin:
            return redirect(url_for('indexadmin'))
        else:
            return redirect(url_for('indexcajero'))

    return render_template('usuario/inicioSesion.html', form=form)

@app.route('/indexadmin/')
@login_required
def indexadmin():
    return render_template('index/indexadmin.html')

@app.route('/indexcajero/')
@login_required
def indexcajero():
    return render_template('index/indexcajero.html')

# Resto de las rutas y funciones...

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)
