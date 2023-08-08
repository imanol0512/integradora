from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
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
    return Usuario.__get__(idusuario)

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
            session['user_role'] = 'admin'
            return redirect(url_for('indexadmin'))
        else:
            session['user_role'] = 'cajero'
            return redirect(url_for('indexcajero'))
    else:
        return render_template('usuario/inicioSesion.html',form=form)

@app.route('/indexadmin/')
def indexadmin():
    if 'user_role' in session and session['user_role'] == 'admin':
        return render_template('indexadmin.html')
    else:
        abort(403)

@app.route('/usuarios/indexcajero/')
def indexcajero():
    if 'user_role' in session and session['user_role'] == 'cajero':
        return render_template('indexcajero.html')
    else:
        abort(403)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.errorhandler(404)
def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)
