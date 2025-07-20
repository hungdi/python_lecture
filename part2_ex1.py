class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}이(가) 소리를 냅니다.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name}이(가) 멍멍 짖습니다.")

dog = Dog("초코")
dog.speak() # 초코이(가) 소리를 냅니다.
dog.bark() # 초코이(가) 멍멍 짖습니다.