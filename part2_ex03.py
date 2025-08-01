class MyContainer:
    def __init__(self, data):
        self.data = data

    def __str__(self): # str()함수 구현
        return f"MyContainer: {self.data}"
    

print(str(MyContainer([1,2,3]))) # MyContainer: [1, 2, 3]

