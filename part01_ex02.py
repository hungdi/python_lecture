def calculate(*args, **kwargs):
    op = kwargs.get("op", "sum")

    if op == "sum":
        return sum(args)
    elif op == "mul":
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return 0
    
print(calculate(1, 2, 3, 4, op="sum"))
print(calculate(1, 2, 3, 4, op="mul"))
print(calculate(1, 2, 3, 4, 5, op="mul"))




