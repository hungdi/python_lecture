from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "멍멍"
    

class Cat(Animal):
    def make_sound(self):
        return "냐옹"
    

dog = Dog()
cat = Cat()
print(dog.make_sound())
print(cat.make_sound())