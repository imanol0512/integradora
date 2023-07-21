from flask_wtf import FlaskForm
from wtforms import (StringField,PasswordField,SubmitField,ValidationError)
from wtforms.validators import DataRequired,EqualTo,Length

from models.usuario import Usuario

################# Formulario de Registro ##################
class RegisterForm(FlaskForm):
    nombreusuario = StringField('Nombre de usuario', validators=[DataRequired()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired(),
                                                    EqualTo('password_confirm', 
                                                            message='Las contraseñas deben coincidir')])
    confirmar_contrasena = PasswordField('Confirmar contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrar')

    ######## Validar Username Único #########
    def validate_username(self, field):
        ######## Consultar si el username existe en la base de datos #######
        if Usuario.check_username(field.data):
            raise ValidationError('El nombre de usuario ya existe. Escriba uno nuevo.')
        
################# Formulario de Login ##################
class LoginForm(FlaskForm):
    nombreusuario = StringField('Nombre de usuario', validators=[DataRequired()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')