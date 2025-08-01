class MyContainer:
    def __init__(self, data):
        self.data = tuple(data)
    
    def __len__(self):
        return len(self.data)
    
print(len(MyContainer([1,2,3]))) # 출력결과=3
