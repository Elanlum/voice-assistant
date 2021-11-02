class Weather:
    def __init__(self):
        self.target_city = ''
        self.temperature = ''
        self.status = ''

    def set_temperature(self, temperature):
        self.temperature = temperature

    def set_status(self, status):
        self.status = status

    def set_target_city(self, target_city):
        self.target_city = target_city
