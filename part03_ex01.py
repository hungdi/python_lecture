# part03_ex01.py
from typing import Protocol

# Speakable 프로토콜 정의
class Speakable(Protocol):
    def speak(self) -> str:
        ... # ...은 구현체가 아니라, 메서드의 시그니처만 정의한다는 의미

# Dog 클래스는 명시적으로 Speakable을 상속받지 않았지만, speak 메서드를 가지고 있으므로 프로토콜을 따릅니다.
class Dog:
    def speak(self) -> str:
        return "Woof!"

# Cat 클래스도 Speakable 프로토콜을 따릅니다.
class Cat:
    def speak(self) -> str:
        return "Meow!"

# speak_to_pet 함수는 Speakable 프로토콜을 따르는 모든 객체를 인자로 받습니다.
def speak_to_pet(pet: Speakable) -> None:
    print(f"Pet says: {pet.speak()}")

# 사용 예시
my_dog = Dog()
my_cat = Cat()

speak_to_pet(my_dog)  # 출력: Pet says: Woof!
speak_to_pet(my_cat)  # 출력: Pet says: Meow!