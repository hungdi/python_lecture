class MyContainer:
    def __init__(self, data):
        self.data = data

    def __setitem__(self, index, value):
        self.data[index] = value


container = MyContainer([1, 2, 3])
container[0] = 100
print(container.data) # [100, 2, 3]


