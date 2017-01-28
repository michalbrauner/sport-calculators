from calculator_run.form import CalculatorForm


class Calculator:
    def __init__(self, form: CalculatorForm):
        self.form = form

    def calculate(self):
        field_to_calculate = self.get_field_to_calculate()

        if field_to_calculate == 'time':
            return self.calculate_time()
        elif field_to_calculate == 'tempo':
            return self.calculate_tempo()
        elif field_to_calculate == 'distance':
            return self.calculate_distance()

        raise RuntimeError('Could not find out what to calculate')

    def get_field_to_calculate(self):
        if self.form.has_distance() and self.form.has_tempo():
            return 'time'

        elif self.form.has_distance() and self.form.has_time():
            return 'tempo'

        else:
            return 'distance'

    def calculate_time(self):
        distance = self.form.distance.data
        tempo_normalized_to_seconds = self.get_tempo_normalized_to_seconds()

        return distance * tempo_normalized_to_seconds / 100

    def calculate_tempo(self):
        distance = self.form.distance.data
        time_normalized_to_seconds = self.get_time_normalized_to_seconds()

        return round((time_normalized_to_seconds * 100) / distance, 0)

    def calculate_distance(self):
        tempo_normalized_to_seconds = self.get_tempo_normalized_to_seconds()
        time_normalized_to_seconds = self.get_time_normalized_to_seconds()

        return round(100 * time_normalized_to_seconds / tempo_normalized_to_seconds, 3)

    def get_tempo_normalized_to_seconds(self):
        tempo_minutes = self.form.tempo_minutes.data
        tempo_seconds = self.form.tempo_seconds.data

        return tempo_minutes * 60 + tempo_seconds

    def get_time_normalized_to_seconds(self):
        time_hours = self.form.time_hours.data
        time_minutes = self.form.time_minutes.data
        time_seconds = self.form.time_seconds.data

        return time_hours * 60 * 60 + time_minutes * 60 + time_seconds
