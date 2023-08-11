from flask import abort, flash, render_template, redirect, url_for, Blueprint, session
from models.usuario import Usuario
from forms.usuario_forms import RegisterForm, UpdateForm

usuario_views = Blueprint('usuario', __name__)

@usuario_views.route('/usuarios/')
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

        return redirect(url_for('usuario.usuarios'))

    return render_template('usuario/agregarUsuario.html', form=form)

@usuario_views.route('/usuario/<int:idusuario>/actualizar/', methods=['GET', 'POST'])
def actualizar(idusuario):
    form = UpdateForm()
    usuario = Usuario.get_by_id(idusuario)
    if not usuario:
        abort(404)
    if form.validate_on_submit():
        usuario.nombreusuario = form.nombreusuario.data
        usuario.contrasena = form.contrasena.data
        usuario.is_admin = form.is_admin.data
        usuario.save()
        return redirect(url_for('usuario.usuarios'))
    form.nombreusuario.data = usuario.nombreusuario
    form.contrasena.data = usuario.contrasena
    form.is_admin.data = usuario.is_admin
    return render_template('usuario/actualizar_usuario.html', form=form)

@usuario_views.route("/usuario/<int:idusuario>/eliminar/",methods=('POST',))
def eliminar(idusuario):
    usuario=Usuario.get_by_id(idusuario)
    usuario.delete()
    return redirect(url_for('usuario.usuarios'))