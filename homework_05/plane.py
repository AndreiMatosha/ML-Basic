"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=2000, started=False, fuel=30, fuel_consumption=5.6, cargo=0, max_cargo=12000):
        super().__init__(weight=2000, started=False, fuel=30, fuel_consumption=5.6)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, value):
        new_cargo = self.cargo + value
        if new_cargo > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo = new_cargo

    def remove_all_cargo(self):
        removed_cargo = self.cargo
        self.cargo = 0
        return removed_cargo
