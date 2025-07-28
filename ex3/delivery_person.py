from delivery_method import DeliveryMethod

class DeliveryPerson:
    def __init__(self, method: DeliveryMethod):
        self.method = method

    def deliver_food(self, user, food_name):
        self.method.deliver(user.user_name, food_name)

