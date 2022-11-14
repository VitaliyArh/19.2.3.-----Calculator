import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):       # метод умножения
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self):       # метод деления
        assert  self.calc.division(self, 6, 2) == 3

    def test_subtraction_calculate_correctly(self):    # метод вычитания
        assert  self.calc.subtraction(self, 5, 2) == 3

    def test_adding_calculate_correctly(self):         # метод сложения
        assert  self.calc.adding(self, 4, 2) == 6

    def test_adding_failed(self):                      # метод сложения - негативный
        assert self.calc.adding(self, 2, 2) == 5
