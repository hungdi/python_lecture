# id로 메모리 주소 비교해보기
class MyClass:
    def __init__(self):
        self.value = 42

a = MyClass()
b = a

print("id(a):", id(a))
print("id(b):", id(b))
print("a is b:", a is b)