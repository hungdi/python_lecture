class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    """dict 자료형 구현을 위한 오버라이딩"""
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return isinstance(other, Drink) and self.name == other.name

class OrangeJuice(Drink):
    def __init__(self):
        super().__init__("Orange Juice", 3000)
    

class Water(Drink):
    def __init__(self):
        super().__init__("Water", 1000)
    

class ZeroCoke(Drink):
    def __init__(self):
        super().__init__("Zero콜라", 2000)
    
