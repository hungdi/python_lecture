class MyContainer:
    def __init__(self, data):
        self.data = data

    def __call__(self):
        return sum(self.data)
    

container = MyContainer([1, 2, 3, 4, 5])
print(container()) # 15