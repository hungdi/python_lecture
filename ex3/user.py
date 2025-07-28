from delivery_system import DeliverySystem   

class User:
    def __init__(self, user_name):
        self.user_name = user_name

    def order_deliver(self, ds: DeliverySystem, food_name, method):
        ds.receive_order(self, food_name, method)
        print(f"주문이 접수 되었습니다. 음식명:{food_name}")