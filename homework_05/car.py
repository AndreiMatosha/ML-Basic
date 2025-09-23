"""
Создайте класс `Car`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.engine import Engine

class Car(Vehicle):
    def __init__(self, engine, weight=2000, started=False, fuel=30, fuel_consumption=5.6):
        super().__init__(weight=2000, started=False, fuel=30, fuel_consumption=5.6)
        self.engine = engine

    def set_engine(self, engine: Engine) -> None:
        self.engine = engine
