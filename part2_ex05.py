class MyContainer:
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        return self.data == other.data
    

container1 = MyContainer([1, 2])
container2 = MyContainer([1, 2])

print(container1 == container2)