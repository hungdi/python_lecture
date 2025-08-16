def outer(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

# @outer
def hello():
    print("Hello!")

# hello() 
decorator = outer(hello)
decorator()