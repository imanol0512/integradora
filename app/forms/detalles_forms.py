from flask_wtf import FlaskForm
from wtforms import (HiddenField,IntegerField,SubmitField,ValidationError)
from wtforms.validators import DataRequired


class CantForm(FlaskForm):
    cantidad=IntegerField('Cantidad',
                         validators=[DataRequired()])
    existencias=HiddenField('Existencias',
                            validators=[DataRequired()])
    submit=SubmitField('Guardar')
    
    def validate_cant(self,field):
        print("La cantidad es...")
        print(self.cantidad.data)