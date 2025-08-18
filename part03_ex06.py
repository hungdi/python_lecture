class Logger:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(f"[LOG] Calling {self.func.__name__} with {args}, {kwargs}")
        return self.func(*args, **kwargs)
    

@Logger
def add(a, b):
    return a+b

@Logger
def add_kw(*args, **kwargs):
    total = 0
    total += sum(args)
    for key,value in kwargs.items():
        total += value
    return total


print(add_kw(3, 5, a=100, b=300))