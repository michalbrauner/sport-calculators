from wtforms import Form, StringField, validators


class CalculatorForm(Form):
    distance = StringField(label='Distance', validators=[
        validators.Optional(),
        validators.Regexp("^[0-9]+([.]{1}[0-9]+){1}$")
    ])

    validator_numeric = validators.Regexp("^[0-9]+$")

    tempo_minutes = StringField(label='Tempo', validators=[
        validators.Optional(),
        validator_numeric,
        validators.NumberRange(min=0)
    ])

    tempo_seconds = StringField(label='Tempo', validators=[
        validators.Optional(),
        validator_numeric,
        validators.NumberRange(min=0, max=59)
    ])

    time_hours = StringField(label='Time', validators=[
        validators.Optional(),
        validator_numeric,
        validators.NumberRange(min=0)
    ])

    time_minutes = StringField(label='Time', validators=[
        validators.Optional(),
        validator_numeric,
        validators.NumberRange(min=0, max=59)
    ])

    time_seconds = StringField(label='Time', validators=[
        validators.Optional(),
        validator_numeric,
        validators.NumberRange(min=0, max=59)
    ])
