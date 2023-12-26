
from flask_wtf import FlaskForm
from wtforms import Field, SelectField, FieldList
from wtforms.widgets import Select, TextInput
from wtforms.validators import DataRequired, Length

ALL_NATIONS = ['USA', 'Great Britain', 'FEC', 'ANZAC', 'KMT', 'KMT Major Power', 'France',
        'CCP', 'Russia', 'Spanish Republicans', 'Spanish Nationalists', 'Germany',
        'Italy', 'Japan', 'Vichy France']

BASE_UNITS = [
	'Militia', 'Infantry', 'Airbourne Infantry', 'Elite Airbourne Infantry', 'Marine', 'Mountain Infantry']

class BattleSimulator(FlaskForm):
	attacker = SelectField('Attacking Nation', choices=ALL_NATIONS, validators=[DataRequired()])
	attacker_army = FieldList(SelectField('Attacking Unit', choices=BASE_UNITS,
        validate_choice=False), min_entries=1, validators=[Length(min=1)])
	defender = SelectField('Defending Nation', choices=ALL_NATIONS, validators=[DataRequired()])
	defender_army = FieldList(SelectField('Defending Unit', choices=BASE_UNITS,
        validate_choice=False), min_entries=1, validators=[Length(min=1)])

class UnitField(Field):
	unit = Select()
	quantity = TextInput()

def get_unit_list_for_nation(nation):
	unit_list = BASE_UNITS
	if nation == 'FEC':
		unit_list.append('Gurkha')

	return sorted(unit_list)
