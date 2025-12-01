import random

class SensorReader:
    def read_temperature(self):
        # Replace with real sensor code (DHT11, DHT22, etc.)
        return round(random.uniform(22, 35), 2)

    def read_humidity(self):
        # Replace with real sensor code
        return round(random.uniform(40, 80), 2)
