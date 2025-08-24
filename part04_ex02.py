from collections import deque

queue = deque()

# enqueue
queue.append(10)
queue.append(20)
queue.append(30)
print(f"현재 큐 상태: {queue}") # deque([10, 20, 30])

# dequeue
dequeued_item = queue.popleft()
print(f"제거된 요소: {dequeued_item}") # 10
print(f"dequeue 후 큐 상태: {queue}") # deque([20, 30])