from flask_wtf import FlaskForm
from wtforms import (SelectField,StringField,SubmitField,ValidationError)
from wtforms.validators import DataRequired,Length,EqualTo

from models.articulo import Articulo

# Formulario de creación de artículo
class CreateArtForm(FlaskForm):
    cb=StringField('Número de código de barras',
                   validators=[DataRequired(),
                               Length(min=15,max=15)])
    nombre=StringField('Nombre',
                       validators=[DataRequired(),
                                   Length(min=5,max=50)])
    precio=StringField('Precio',
                       validators=[DataRequired()])
    marca=StringField('Marca',
                      validators=[DataRequired()])
    categoria=SelectField(u'Categoría',choices=(('1','Categoría 1'),('2','Categoría 2')),
                          validators=[DataRequired()])
    existencias=StringField('Existencias',
                            validators=[DataRequired()])
    submit=SubmitField('Guardar')

    def validate_cb_field(self,field):
        # Consulta si existe el número en la BD
        if Articulo.check_cb(field.data):
            raise ValidationError('El número del código de barras ya existe. Intente uno nuevo.')

# Formulario de actualización de artículo
class UpdateArtForm(FlaskForm):
    cb=StringField('Número de código de barras',
                   validators=[DataRequired(),
                               Length(min=15,max=15)])
    nombre=StringField('Nombre',
                       validators=[DataRequired(),
                                   Length(min=5,max=50)])
    precio=StringField('Precio',
                       validators=[DataRequired()])
    marca=StringField('Marca',
                      validators=[DataRequired()])
    categoria=SelectField(u'Categoría',choices=(('1','Categoría 1'),('2','Categoría 2')),
                          validators=[DataRequired()])
    existencias=StringField('Existencias',
                            validators=[DataRequired()])
    submit=SubmitField('Actualizar')

    def validate_cb_field(self,field):
        # Consulta si existe el número en la BD
        if Articulo.check_cb(field.data):
            raise ValidationError('El número del código de barras ya existe. Intente uno nuevo.')