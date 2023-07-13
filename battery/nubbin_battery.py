from abc import ABC
from car import Car


class NubbinBattery(Car, ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        battery_service_date = self.current_date - self.last_service_date
        if battery_service_date < 4:
            return True
        else:
            return False
