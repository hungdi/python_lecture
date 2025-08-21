from typing import TypeVar, Generic

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value
    
    def get(self) -> T:
        return self.value
    
apple_box = Box[str]("사과")
print(apple_box.get())

number_box = Box("ㅋㅋ")
print(number_box.get())