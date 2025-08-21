from typing import Callable

# process_data 함수 작성
def process_data(data: list[int], callback: Callable[[int], None]) -> None:
    for item in data:
        callback(item)

# 콜백 함수 구현
def print_squared(x: int) -> None:
    print(f"{x}의 제곱은 {x*x}입니다.")

numbers = [1, 2, 3, 4, 5]
process_data(numbers, print_squared)