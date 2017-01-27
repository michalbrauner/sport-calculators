from flask_wtf import FlaskForm
from wtforms import IntegerField, validators


class CalculatorForm(FlaskForm):
    distance = IntegerField(label='Distance', validators=[
        validators.Optional(),
        validators.NumberRange(min=0)
    ])

    tempo_minutes = IntegerField(label='Tempo', validators=[
        validators.Optional(),
        validators.NumberRange(min=0)
    ])

    tempo_seconds = IntegerField(label='Tempo', validators=[
        validators.Optional(),
        validators.NumberRange(min=0, max=59)
    ])

    time_hours = IntegerField(label='Time', validators=[
        validators.Optional(),
        validators.NumberRange(min=0)
    ])

    time_minutes = IntegerField(label='Time', validators=[
        validators.Optional(),
        validators.NumberRange(min=0, max=59)
    ])

    time_seconds = IntegerField(label='Time', validators=[
        validators.Optional(),
        validators.NumberRange(min=0, max=59)
    ])

    def validate_on_submit(self):

        validation_result = super().validate_on_submit()

        if validation_result:

            if not self.has_all_fields_to_calculate():
                self.errors["global"] = "You have to enter at least 2 of 3 fields in the form."
                return False

            return True

        return False

    def has_all_fields_to_calculate(self):
        filled_fields = 0

        if self.distance.data is not None:
            filled_fields += 1

        if self.tempo_seconds.data is not None and self.tempo_minutes.data is not None:
            filled_fields += 1

        if self.time_hours.data is not None and self.time_minutes.data is not None \
                and self.time_seconds.data is not None:

            filled_fields += 1

        return filled_fields == 2
