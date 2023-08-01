from flask_wtf import FlaskForm
from wtforms import (IntegerField,SubmitField)
from wtforms.validators import DataRequired


class CantForm(FlaskForm):
    cantidad=IntegerField('Cantidad',
                         validators=[DataRequired()])
    submit=SubmitField('Guardar')