from cars import Car, SportsCar, SUV

car = Car("Generic", "Car")
sports_car = SportsCar("Ferrari", "F50", 320)
suv = SUV("Ford", "Explorer", 7)

# Polymorphism in action
cars = [car, sports_car, suv]

for car in cars:
    print(car.accelerate())
    print(car.brake())
    print("---------")