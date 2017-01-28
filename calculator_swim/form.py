from wtforms import FloatField, validators
from calculator.form import CalculatorForm as BaseCalculatorForm


class CalculatorForm(BaseCalculatorForm):
    class UnitLabels(BaseCalculatorForm.UnitLabels):
        distance = 'm'
        tempo = 'min / 100m'

        def __init__(self):
            super()

    distance = FloatField(label='Distance', validators=[
        validators.Optional(),
        validators.NumberRange(min=0)
    ], render_kw={'class': 'form-control', 'aria-label': 'Enter distance in m'})
