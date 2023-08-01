from flask_wtf import FlaskForm
from wtforms import (SelectField,StringField,SubmitField,ValidationError,IntegerField)
from wtforms.validators import DataRequired,Length,EqualTo
from flask_wtf.file import FileField,FileRequired,FileAllowed

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
    categoria=SelectField(u'Categoría',choices=(('8','Aceites'),('1','Cuadro'),('5','Eléctrico'),('4','Freno'),('2','Misceláneo'),('3','Motor'),('6','Suspensión'),('7','Tracción')),
                          validators=[DataRequired()])
    existencias=IntegerField('Existencias',
                            validators=[DataRequired()])
    image=FileField('Imagen',
                    validators=[FileAllowed(['jpg','png','jpeg'],'Solo se admiten imágenes de formato .jpg, .jpeg o .png')])
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
    categoria=SelectField(u'Categoría',choices=(('8','Aceites'),('1','Cuadro'),('5','Eléctrico'),('4','Freno'),('2','Misceláneo'),('3','Motor'),('6','Suspensión'),('7','Tracción')),
                          validators=[DataRequired()])
    existencias=StringField('Existencias',
                            validators=[DataRequired()])
    image=FileField('Imagen',
                    validators=[FileAllowed(['jpg','png','jpeg'],'Solo se admiten imágenes de formato .jpg, .jpeg o .png')])
    submit=SubmitField('Actualizar')

    def validate_cb_field(self,field):
        # Consulta si existe el número en la BD
        if Articulo.check_cb(field.data):
            raise ValidationError('El número del código de barras ya existe. Intente uno nuevo.')