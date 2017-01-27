from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, validators


class CalculatorForm(FlaskForm):

    class Meta:
        csrf = False

    distance = FloatField(label='Distance', validators=[
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

        if self.has_distance():
            filled_fields += 1

        if self.has_tempo():
            filled_fields += 1

        if self.has_time():
            filled_fields += 1

        return filled_fields == 2

    def has_distance(self):
        return self.distance.data is not None

    def has_tempo(self):
        return self.tempo_seconds.data is not None and self.tempo_minutes.data is not None

    def has_time(self):
        return self.time_hours.data is not None and self.time_minutes.data is not None \
            and self.time_seconds.data is not None
