class MyContainer:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __lt__(self, other):
        #return len(self.data) < len(other)
        return max(self.data) < max(other)
    

container1 = MyContainer([1, 2, 3])
container2 = MyContainer([1, 4])
print(container1 < container2)
    