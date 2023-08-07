from flask import abort, flash, render_template, redirect, url_for, Blueprint, session
from models.usuario import Usuario
from forms.usuario_forms import RegisterForm, LoginForm, UpdateForm

usuario_views = Blueprint('usuario', __name__)

@usuario_views.route('/usuarios/', methods=['GET', 'POST'])
def usuarios():
    usuarios = Usuario.get_all()
    return render_template("usuario/usuarios.html", usuarios=usuarios)

@usuario_views.route('/usuarios/registrar/', methods=['GET', 'POST'])
def registrar():
    form = RegisterForm()

    if form.validate_on_submit():
        nombreusuario = form.nombreusuario.data
        contrasena = form.contrasena.data
        is_admin = form.is_admin.data

        usuario = Usuario(nombreusuario, contrasena, is_admin)
        usuario.save()

        return redirect(url_for('usuario.login'))

    return render_template('usuario/registrar.html', form=form)

@usuario_views.route('/usuario/<int:id>/actualizar/', methods=['GET', 'POST'])
def actualizar(id):
    form = UpdateForm()
    user = Usuario.get_by_id(id)
    if not user:
        abort(404)

    if form.validate_on_submit():
        user.nombreusuario = form.nombreusuario.data
        user.contrasena = form.contrasena.data
        user.is_admin = form.is_admin.data
        user.save()

        return redirect(url_for('usuario.usuarios'))

    form.nombreusuario.data = user.nombreusuario
    form.contrasena.data = user.contrasena
    form.is_admin.data = user.is_admin

    return render_template('usuario/registrar.html', form=form)