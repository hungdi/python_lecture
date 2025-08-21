# part01_lab01.py
from typing import TypeVar, Generic, List

# 1. T라는 타입 변수 정의
T = TypeVar('T')

# 2. 제네릭 스택 클래스 구현
class Stack(Generic[T]):
    def __init__(self):
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

# --- 정답 코드 예시 ---

# 정수 타입 스택
int_stack = Stack[int]()
int_stack.push(10)
int_stack.push(20)
print(int_stack.pop())  # 20 출력
print(int_stack.pop())  # 10 출력

# 문자열 타입 스택
str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
print(str_stack.pop())  # world 출력
print(str_stack.pop())  # hello 출력
