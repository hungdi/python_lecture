import threading

def greet(name):
    print(f"안녕하세요, {name}입니다")

t = threading.Thread(target=greet, args=("철수",))
t.start()
t.join()