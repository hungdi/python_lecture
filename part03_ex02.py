import threading, time, random

def run_trial(n_threads=8, iters=5000, use_lock=False):
    global counter
    counter = 0
    lock = threading.Lock()
    barrier = threading.Barrier(n_threads)

    def worker():
        global counter
        barrier.wait()
        for _ in range(iters):
            if use_lock:
                with lock:
                    tmp = counter
                    if random.random() < 0.001:
                        time.sleep(0)
                    counter = tmp + 1
            else:
                tmp = counter
                if random.random() < 0.001:
                    time.sleep(0)
                counter = tmp + 1

    threads = [threading.Thread(target=worker) for _ in range(n_threads)]
    for t in threads: t.start()
    for t in threads: t.join()
    return counter

if __name__ == "__main__":
    random.seed()
    total = 0
    trials = 20
    n_threads = 8
    iters = 5000
    expected = n_threads * iters

    print("=== Without Lock ===")
    fails = 0
    results = []
    for i in range(trials):
        res = run_trial(n_threads, iters, use_lock=False)
        results.append(res)
        ok = "OK" if res == expected else "FAIL"
        if res != expected: fails += 1
        print(f"trial {i+1:02d}: {res} / {expected} -> {ok}")
    print(f"fails: {fails} / {trials}")

    print("\n=== With Lock ===")
    res = run_trial(n_threads, iters, use_lock=True)
    print(f"locked result: {res} / {expected}")