import threading, time, random

counter = 0

#lock = threading.Lock()
def worker(n=20000):
    global counter
    for _ in range(n):
        #with lock:
        r = counter
        if random.random() < 0.01:
            time.sleep(0)
        counter = r + 1

ts = [threading.Thread(target=worker) for _ in range(8)]
for t in ts: t.start()
for t in ts: t.join()
print(counter)
