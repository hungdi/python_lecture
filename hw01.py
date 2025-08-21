from typing import TypeVar, Callable, Dict


T = TypeVar('T')
R = TypeVar('R')

def cache_result(func: Callable[[T], R]) -> Callable[[T], R]:
    cache: Dict[T, R] = {}
    def inner(arg :T):
        if arg not in cache:
            print("caching...")
            cache[arg] = func(arg)
        return cache[arg]
    return inner

@cache_result
def str_to_int(data: str) -> int:
    return int(data)

@cache_result
def fibonacci(n: int) -> int:
    print(f"Calculating fibonacci({n})...")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(str_to_int(3))
print(str_to_int(3))

print(fibonacci(5))
print(fibonacci(5))
    


