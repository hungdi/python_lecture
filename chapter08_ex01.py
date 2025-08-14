import threading
import time

def ping():
    for _ in range(5):
        print("ping")
        time.sleep(1)

def pong():
    for _ in range(5):
        print("pong")
        time.sleep(1.5)


t1 = threading.Thread(target=ping)
t2 = threading.Thread(target=pong)

t1.start()
t2.start()

t1.join()
t2.join()
