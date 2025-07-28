from delivery_person import DeliveryPerson
from order import Order

class DeliverySystem:
    def __init__(self):
        self.delivery_list = []


    def receive_order(self, user, food_name, method):
        self.delivery_list.append(Order(user, food_name, method))

    
    def process_order(self, delivery_person):
        for order in self.delivery_list:
            if isinstance(order.method, type(delivery_person.method)):
                delivery_person.deliver_food(order.user, order.food_name)
                self.delivery_list.remove(order)
                return
        


