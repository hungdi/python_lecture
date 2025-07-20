class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name}가 멍멍 짖어요")

mydog = Dog("가을이")
mydog.bark()
