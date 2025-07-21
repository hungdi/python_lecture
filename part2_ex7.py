class Parent:
    def greet(self):
        print("안녕, 나는 부모야")

class Child(Parent):
    def greet(self):
        print("안녕, 나는 자식이야.")

obj = Child()
obj.greet()

for cls in Child.__mro__:
    print(cls)