count = 0

def increment():
    global count
    count += 1
    return count

print(increment())
print(increment())
print(increment())