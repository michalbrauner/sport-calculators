from calculator.form import CalculatorForm
from calculator.calculator import Calculator as BaseCalculator


class Calculator(BaseCalculator):
    def __init__(self, form: CalculatorForm):
        super(Calculator, self).__init__(form)

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
