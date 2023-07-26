from flask import abort,flash,render_template,redirect,url_for,Blueprint

from models.usuario import Usuario

from forms.usuario_forms import RegisterForm,LoginForm

usuario_views=Blueprint('usuario',__name__)

@usuario_views.route('/usuarios/registrar/',methods=('GET','POST'))
def registrar():
    form=RegisterForm()

    # Verificar datos: nombre de usuario y contraseña
    if form.validate_on_submit():
        nombreusuario=form.nombreusuario.data
        contrasena=form.contrasena.data
        is_admin=form.is_admin.data

        usuario=Usuario(nombreusuario,contrasena,is_admin)
        usuario.save()

        return redirect(url_for('usuario.login'))
    return render_template('usuario/registrar.html',form=form)

@usuario_views.route('/usuarios/login/',methods=('GET','POST'))
def login():
    form=LoginForm()

    if form.validate_on_submit():
        nombreusuario=form.nombreusuario.data
        contrasena=form.contrasena.data
        usuario=Usuario.get_by_password(nombreusuario,contrasena)
        if not usuario:
            flash('Usuario y/o contraseña incorrectos. Intenta de nuevo.')
        else:
            return render_template('index/indexadmin.html',usuario=usuario)
        return render_template('usuario/inicioSesion.html',form=form)