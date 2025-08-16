def make_power(n):
    def power(x):
        return x ** n
    return power

square = make_power(2)
cube = make_power(3)

print(list(map(square, [1, 2, 3])))
print(list(map(cube, [1, 2, 3])))