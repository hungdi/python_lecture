import threading

counter = 0

def increase():
    global counter
    for _ in range(100000):
        counter += 1

t1 = threading.Thread(target=increase)
t2 = threading.Thread(target=increase)

t1.start()
t2.start()

t1.join()
t2.join()

print("최종 counter 값:", counter)