from typing import Callable, TypeVar


T = TypeVar("T")
U = TypeVar("U")

def mapper(xs: list[T], f: Callable[[T], U]) -> list[U]:
    return [f(x) for x in xs]

print(mapper(["1", "2", "3"], int))
