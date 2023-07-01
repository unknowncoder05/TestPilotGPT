from .car import Car

class SportsCar(Car):
    def __init__(self, brand, model, max_speed):
        super().__init__(brand, model)
        self.max_speed = max_speed
    
    def accelerate(self):
        return "The sports car is accelerating."
    
    def brake(self):
        return "The sports car is braking."