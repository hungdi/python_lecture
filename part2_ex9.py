class Parent:
    def __init__(self):
        self.parent_attr = "부모 속성"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attr = "자식 속성"

c = Child()

print("Child 인스턴스의 __dict__")
print(c.__dict__) # 자식 객체는 부모속성도 가지고있음!