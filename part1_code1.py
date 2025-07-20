
car_model = "소나타"
car_speed = 0

def accelerate():
    global car_speed
    car_speed += 10

accelerate()
accelerate()
print(car_speed)