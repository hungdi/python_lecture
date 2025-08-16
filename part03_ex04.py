def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

counter = outer()
print(counter()) #1
print(counter()) #2
print(counter()) #3