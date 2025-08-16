def greet(name):
    def message():
        return "Hello"
    return f"{message()}, {name}!"

print(greet("Alice"))
# 결과: Hello, Alice!