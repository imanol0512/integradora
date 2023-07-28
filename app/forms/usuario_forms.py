from flask_wtf import FlaskForm
from wtforms import (StringField,SelectField,PasswordField,SubmitField,ValidationError)
from wtforms.validators import DataRequired,EqualTo,Length

from models.usuario import Usuario

################# Formulario de Registro ##################
class RegisterForm(FlaskForm):
    nombreusuario = StringField('Nombre de usuario', validators=[DataRequired(),
                                                                 Length(min=4,max=45)])
    is_admin=SelectField(u'Rol del usuario',choices=(('1','Administrador'),('0','Cajero')),
                         validators=[DataRequired()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired(),
                                                        Length(min=5,max=20),
                                                        EqualTo('password_confirm', 
                                                            message='Las contraseñas deben coincidir')])
    confirmar_contrasena = PasswordField('Confirmar contraseña', validators=[DataRequired(),
                                                                            Length(min=5,max=20)])
    submit = SubmitField('Registrar')

    ######## Validar Nombre de usuario Único #########
    def validate_username(self, field):
        ######## Consultar si el nombre de usuario existe en la base de datos #######
        if Usuario.check_username(field.data):
            raise ValidationError('El nombre de usuario ya existe. Escriba uno nuevo.')

################# Formulario de Actualización ##################
class UpdateForm(FlaskForm):
    nombreusuario = StringField('Nombre de usuario', validators=[DataRequired(),
                                                                 Length(min=4,max=45)])
    is_admin=SelectField(u'Rol del usuario',choices=(('1','Administrador'),('0','Cajero')),
                         validators=[DataRequired()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired(),
                                                        Length(min=5,max=20),
                                                        EqualTo('password_confirm', 
                                                            message='Las contraseñas deben coincidir')])
    confirmar_contrasena = PasswordField('Confirmar contraseña', validators=[DataRequired(),
                                                                            Length(min=5,max=20)])
    submit = SubmitField('Registrar')

    ######## Validar Nombre de usuario Único #########
    def validate_username(self, field):
        ######## Consultar si el nombre de usuario existe en la base de datos #######
        if Usuario.check_username(field.data):
            raise ValidationError('El nombre de usuario ya existe. Escriba uno nuevo.')

################# Formulario de Login ##################
class LoginForm(FlaskForm):
    nombreusuario = StringField('Nombre de usuario', validators=[DataRequired()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')