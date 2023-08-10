from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from forms.usuario_forms import LoginForm

from views.articulo_views import articulo_views
from views.index_views import index_views
from views.proveedor_views import proveedor_views
from views.error_views import error_views
from views.usuario_views import usuario_views
from views.venta_views import venta_views

from models.db import get_connection
from models.usuario import Usuario

app = Flask(__name__)
app.secret_key = 'B!1w8NAt1T^%kvhUI*S^'

db = get_connection()
login_manager = LoginManager(app)

app.register_blueprint(articulo_views)
app.register_blueprint(index_views)
app.register_blueprint(proveedor_views)
app.register_blueprint(error_views)
app.register_blueprint(usuario_views)
app.register_blueprint(venta_views)

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

        usuario = Usuario.get_by_username(nombreusuario)
        print(usuario)

        if usuario is None:
            flash('Usuario y/o contraseña incorrectos. Intenta de nuevo.', 'error')
            return redirect(url_for('login'))

        if usuario.verify_password(contrasena):
            login_user(usuario)
            if usuario.is_admin:
                return redirect(url_for('index.indexadmin'))
            else:
                return redirect(url_for('indexcajero'))
        else:
            flash('Usuario y/o contraseña incorrectos. Intenta de nuevo.', 'error')
            return redirect(url_for('login'))
    return render_template('usuario/inicioSesion.html', form=form)

# Agrega otras rutas y funciones aquí si es necesario

if __name__ == '__main__':
    csrf = CSRFProtect(app)  # Inicializa CSRFProtect aquí
    app.run(debug=True)
