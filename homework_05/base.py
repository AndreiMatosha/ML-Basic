"""
Доработайте класс `Vehicle`
"""
from homework_05.exceptions import LowFuelError, NotEnoughFuel
from abc import ABC


class Vehicle(ABC):

    def __init__(self, weight=2000, started=False, fuel=30, fuel_consumption=5.6):

        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        """
        starts car engine
        :return: None or LowFuelError
        """
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance: float) -> float or NotEnoughFuel:
        """
        Calculates the rest of fuel or raise NotEnoughFuel exception
        :return: float or NotEnoughFuel
        """
        if self.fuel_consumption * distance <= self.fuel:
            return self.fuel - self.fuel_consumption * distance
        else:
            raise NotEnoughFuel

