class DeliveryMethod:
    def deliver(self, user_name, food_name):
        raise NotImplementedError
    
class Bicycle(DeliveryMethod):
    def deliver(self, user_name, food_name):
        print(f"자전거로 {user_name}에게 {food_name}을 느리지만 안전하게 배달중...")

class Motorbike(DeliveryMethod):
    def deliver(self, user_name, food_name):
        print(f"오토바이로 {user_name}에게 {food_name}을 빠르게 배달중...")
    

class Drone(DeliveryMethod):
    def deliver(self, user_name, food_name):
        print(f"드론으로 {user_name}에게 {food_name}을 초고속 배달중...")

