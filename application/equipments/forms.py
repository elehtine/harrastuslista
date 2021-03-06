from flask_wtf import FlaskForm
from wtforms import StringField, validators

class EquipmentForm(FlaskForm):
    equipment = StringField("Equipment", [validators.Length(min=2, max=35)])

    class Meta:
        csrf = False
