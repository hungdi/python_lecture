import threading


ranges = [(1, 1000000), (1000001, 2000000), (2000001, 3000000)]
threads = []
results = []

def sum_range(start, end):
    total = sum(range(start, end+1))
    results.append(total)
    return total


for r in ranges:
    t = threading.Thread(target=sum_range, args=r)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"총합: {sum(results)}")
print(f"sync 총합: {sum_range(1, 3000000)}")
