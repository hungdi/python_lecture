def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

counterA = make_counter()
print(counterA())  # 결과: 1
print(counterA())  # 결과: 2

counterB = make_counter()
print(counterB())  # 결과: 1 (새로운 클로저이기 때문)