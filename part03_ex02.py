class Power:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x ** self.n

square = Power(2)
cube = Power(3)
print(list(map(square, [1, 2, 3])))
print(list(map(cube, [1, 2, 3])))
