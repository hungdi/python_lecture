#part2_ex6.py
class Parent:
    def __init__(self):
        self.a = 10

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.b = 20

c = Child()
