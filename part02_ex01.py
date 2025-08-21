from typing import TypeVar, Union

Number = TypeVar('Number', int, float)

def add_numbers(a: Number, b: Number) -> Number:
    return a+b


result1 = add_numbers(1, 2)
result2 = add_numbers(3.5, 4.5)

result3 = add_numbers("apple", "banana")

