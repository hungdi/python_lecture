from typing import ParamSpec, TypeVar, Callable

P = ParamSpec('P')
T = TypeVar('T')

def print_args_and_kwargs(func: Callable[P, T]) -> Callable[P, T]:

    def inner(*args: P.args, **kwargs: P.kwargs) -> None:
        print(f"Argument(args): {args}")
        print(f"Keyword Argument(kwargs): {kwargs}")
        return func(*args, **kwargs)
    return inner


@print_args_and_kwargs
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

@print_args_and_kwargs
def calculate_sum(*args, **kwargs) -> int:
    total = 0
    total += sum(args)
    for k, v in kwargs.items():
        total += v
    return total


print(greet("jihye"))
print(calculate_sum(10, b=20))