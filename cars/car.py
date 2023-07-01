class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def accelerate(self):
        return "The car is accelerating."
    
    def brake(self):
        return "The car is braking."