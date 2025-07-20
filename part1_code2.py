class Car:
    def __init__(self, model):
        self.model = model
        self.speed = 0
    
    def accelerate(self):
        self.speed += 10


car1 = Car("소나타")
car1.accelerate()
car1.accelerate()
print(car1.speed)