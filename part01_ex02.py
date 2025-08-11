import threading

def intro(name, age):
    print(f"{name}, {age}")

t = threading.Thread(target=intro, args=("민수",), kwargs={"age": 40})

t.start()
t.join()
