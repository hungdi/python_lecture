def add(*args, **kwargs):
    total = 0

    for num in args:
        total += num

    for key, value in kwargs.items():
        total += value
    
    return total


def add_use_args(*args):
    total = 0
    for num in args:
        total += num
    
    return total


print(add(1, 2, 3))
print(add(1, 2, x=3, y=4))
print(add(a=100,b=200))
print(add())

print(add_use_args(1, 2, 3, 4))