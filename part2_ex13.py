class MyContainer:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        return item in self.data
    

container = MyContainer([1, 2, 3])
print(5 in container)
print(3 in container)
