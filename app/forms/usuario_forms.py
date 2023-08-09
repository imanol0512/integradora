from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo

from models.usuario import Usuario

class RegisterForm(FlaskForm):
    nombreusuario = StringField('Nombre de usuario', validators=[DataRequired(), Length(min=4, max=45)])
    is_admin = SelectField('Rol del usuario', choices=[('1', 'Administrador'), ('0', 'Cajero')], validators=[DataRequired()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired(), Length(min=5, max=20), EqualTo('confirmar_contrasena', message='Las contraseñas deben coincidir')])
    confirmar_contrasena = PasswordField('Confirmar contraseña', validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField('Registrar')

    def validate_nombreusuario(self, field):
        if Usuario.check_username(field.data):
            raise ValidationError('El nombre de usuario ya existe. Por favor, elige otro.')

class UpdateForm(FlaskForm):
    nombreusuario = StringField('Nombre de usuario', validators=[DataRequired(), Length(min=4, max=45)])
    is_admin = SelectField('Rol del usuario', choices=[('1', 'Administrador'), ('0', 'Cajero')], validators=[DataRequired()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired(), Length(min=5, max=20), EqualTo('confirmar_contrasena', message='Las contraseñas deben coincidir')])
    confirmar_contrasena = PasswordField('Confirmar contraseña', validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField('Actualizar')

    def validate_nombreusuario(self, field):
        if Usuario.check_username(field.data):
            raise ValidationError('El nombre de usuario ya existe. Por favor, elige otro.')



class LoginForm(FlaskForm):
    nombreusuario = StringField('Nombre de usuario', validators=[DataRequired()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')
