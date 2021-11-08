"""
Weather objects which contains:
- target_city name
- temperature
- general weather status
"""


class Weather:
    def __init__(self):
        self.target_city = ''
        self.temperature = ''
        self.status = ''

    def set_temperature(self, temperature: str):
        self.temperature = temperature

    def set_status(self, status: str):
        self.status = status

    def set_target_city(self, target_city: str):
        self.target_city = target_city
