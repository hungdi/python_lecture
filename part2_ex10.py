class MyContainer:
    def __init__(self, data):
        self.data = tuple(data)
    
    def __getitem__(self, index):
        return self.data[index]
    
container = MyContainer(['a', 'b', 'c'])
print(container[1]) # 출력결과 b
