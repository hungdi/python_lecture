class MyContainer:
    def __init__(self, data):
        self.data = tuple(data)
    
    def __hash__(self):
        return hash(self.data)
    

a = MyContainer([1, 2])
b = MyContainer([1, 2])
print(set([a, b]))