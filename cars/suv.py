from .car import Car

class SUV(Car):
    def __init__(self, brand, model, num_seats):
        super().__init__(brand, model)
        self.num_seats = num_seats
    
    def accelerate(self):
        return "The SUV is accelerating."
    
    def brake(self):
        return "The SUV is braking."
