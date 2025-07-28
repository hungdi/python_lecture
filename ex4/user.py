from order import Order

class User:
    def __init__(self, name):
        self.name = name

    def make_orders(self, foods):
        return Order(self, foods)
    
    