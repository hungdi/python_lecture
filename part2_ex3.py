class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def speak(self):
        print("강아지가 멍멍!")

class Cat(Animal):
    def speak(self):
        print("고양이가 야옹~")

def make_it_speak(animal):
    animal.speak()

animals = [Dog(), Cat(), Animal()]
for a in animals: # 객체지향으로 구현하면, 이렇게 여러 객체를 하나의 for문에 사용할 수 있음(부모타입으로)
    make_it_speak(a)