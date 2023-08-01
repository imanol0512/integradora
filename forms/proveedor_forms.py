from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length

# Formulario de creación del proveedor
class CreateProvForm(FlaskForm):
    nombre=StringField('Nombre',
                          validators=[DataRequired(),
                                      Length(min=3,max=25)])
    apellido=StringField('Apellido',
                          validators=[DataRequired(),
                                      Length(min=3,max=25)])
    telefono=StringField('Teléfono',
                          validators=[DataRequired(),
                                      Length(min=10,max=10)])
    direccion=TextAreaField('Dirección',
                          validators=[DataRequired(),
                                      Length(min=10,max=40)])
    numdireccion=StringField('Número de Dirección',
                          validators=[DataRequired(),
                                      Length(min=1,max=3)])
    colonia=TextAreaField('Colonia',
                          validators=[DataRequired(),
                                      Length(min=5,max=40)])
    municipio=StringField('Municipio',
                          validators=[DataRequired(),
                                      Length(min=5,max=40)])
    estado=StringField('Estado',
                          validators=[DataRequired(),
                                      Length(min=5,max=25)])
    submit=SubmitField('Guardar')

# Formulario de actualización del proveedor
class UpdateProvForm(FlaskForm):
    nombre=StringField('Nombre',
                          validators=[DataRequired(),
                                      Length(min=3,max=25)])
    apellido=StringField('Apellido',
                          validators=[DataRequired(),
                                      Length(min=3,max=25)])
    telefono=StringField('Teléfono',
                          validators=[DataRequired(),
                                      Length(min=10,max=10)])
    direccion=StringField('Dirección',
                          validators=[DataRequired(),
                                      Length(min=10,max=40)])
    numdireccion=StringField('Número de Dirección',
                          validators=[DataRequired(),
                                      Length(min=1,max=3)])
    colonia=StringField('Colonia',
                          validators=[DataRequired(),
                                      Length(min=5,max=40)])
    municipio=StringField('Municipio',
                          validators=[DataRequired(),
                                      Length(min=5,max=40)])
    estado=StringField('Estado',
                          validators=[DataRequired(),
                                      Length(min=5,max=25)])
    submit=SubmitField('Actualizar')