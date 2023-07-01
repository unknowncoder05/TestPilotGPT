# Testing using pytest
from cars import Car, SportsCar, SUV
import pytest

def test_car():
    car = Car("Generic", "Car")
    assert car.accelerate() == "The car is accelerating."
    assert car.brake() == "The car is braking."

def test_sports_car():
    sports_car = SportsCar("Ferrari", "F50", 320)
    assert sports_car.accelerate() == "The sports car is accelerating."
    assert sports_car.brake() == "The sports car is braking."

def test_suv():
    suv = SUV("Ford", "Explorer", 7)
    assert suv.accelerate() == "The SUV is accelerating."
    assert suv.brake() == "The SUV is braking."
