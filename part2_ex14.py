class MyContainer:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self): 
        self.index = 0
        return self # __iter__()는 iterator를 반환해야함
    
    # MyContainer는 __next__를 구현했기 때문에 'iterator'임
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

container = MyContainer([1, 2, 3, 4, 5])
for item in container: 
    print(item) 
#1, 2, 3, 4, 5 순차 출력