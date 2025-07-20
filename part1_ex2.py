class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"안녕하세요! 저는 {self.name}이고 나이는 {self.age}살이에요.")


p1 = Person("지혜", 36)
p1.greet()