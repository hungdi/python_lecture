class Animal:
    def speak(self):
        print("동물이 소리를 냅니다")

class Cat(Animal):
    def speak(self):
        print("고양이가 야옹~하고 웁니다.")


a = Animal()
c = Cat()
a.speak()
c.speak()
