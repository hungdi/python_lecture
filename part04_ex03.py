import queue

q = queue.Queue()

# enqueue (put)
q.put('job1')
q.put('job2')
print(f"큐에 있는 요소 수: {q.qsize()}") # 2

# dequeue (get)
job = q.get()
print(f"처리된 작업: {job}") # job1
print(f"큐에 남은 요소 수: {q.qsize()}") # 1