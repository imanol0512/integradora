from flask_wtf import FlaskForm
from wtforms import (SelectField, StringField, SubmitField, ValidationError, IntegerField)
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed

from models.articulo import Articulo
from models.categoria import Categoria

# Obtener las categorías disponibles para cargar en el formulario
def get_categorias():
    categorias = Categoria.get_all()  # Supongo que tienes un método en tu modelo para obtener todas las categorías
    choices = [(cat.id, cat.nombre) for cat in categorias]
    return choices

class CreateArtForm(FlaskForm):
    cb = StringField('Número de código de barras', validators=[DataRequired(), Length(min=15, max=15)])
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=5, max=50)])
    precio = StringField('Precio', validators=[DataRequired()])
    marca = StringField('Marca', validators=[DataRequired()])
    categoria = SelectField('Categoría', choices=get_categorias(), coerce=int, validators=[DataRequired()])
    existencias = IntegerField('Existencias', validators=[DataRequired()])
    image = FileField('Imagen', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo se admiten imágenes de formato .jpg, .jpeg o .png')])
    submit = SubmitField('Guardar')

    def validate_cb_field(self, field):
        if Articulo.check_cb(field.data):
            raise ValidationError('El número del código de barras ya existe. Intente uno nuevo.')

class UpdateArtForm(FlaskForm):
    cb = StringField('Número de código de barras', validators=[DataRequired(), Length(min=15, max=15)])
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=5, max=50)])
    precio = StringField('Precio', validators=[DataRequired()])
    marca = StringField('Marca', validators=[DataRequired()])
    categoria = SelectField('Categoría', choices=get_categorias(), coerce=int, validators=[DataRequired()])
    existencias = StringField('Existencias', validators=[DataRequired()])
    image = FileField('Imagen', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo se admiten imágenes de formato .jpg, .jpeg o .png')])
    submit = SubmitField('Actualizar')

    def validate_cb_field(self, field):
        if Articulo.check_cb(field.data):
            raise ValidationError('El número del código de barras ya existe. Intente uno nuevo.')
