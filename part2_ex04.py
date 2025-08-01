class MyContainer:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"MyContainer({self.data})"
    

obj = MyContainer([1, 2])
print(repr(obj)) # MyContainer([1, 2])