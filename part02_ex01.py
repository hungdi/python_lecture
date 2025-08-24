from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        # 요소를 큐에 추가합니다.
        self.items.append(item)

    def dequeue(self):
        # 큐의 가장 앞쪽 요소를 제거하고 반환합니다.
        if not self.is_empty():
            return self.items.popleft()
        else:
            return "큐가 비어 있습니다."

    def front(self):
        # 큐의 가장 앞쪽 요소를 반환합니다. (제거하지 않음)
        if not self.is_empty():
            return self.items[0]
        else:
            return "큐가 비어 있습니다."

    def is_empty(self):
        # 큐가 비어 있는지 확인합니다.
        return len(self.items) == 0

    def size(self):
        # 큐의 크기를 반환합니다.
        return len(self.items)



my_queue = Queue()

print(f"큐가 비어 있나요?: {my_queue.is_empty()}") # True
print(f"현재 큐 크기: {my_queue.size()}") # 0

# 큐에 데이터 추가 (enqueue)
my_queue.enqueue("작업1")
my_queue.enqueue("작업2")
my_queue.enqueue("작업3")
print(f"현재 큐 상태: {list(my_queue.items)}") # ['작업1', '작업2', '작업3']

# 큐의 가장 앞쪽 요소 확인 (front)
print(f"큐의 가장 앞 요소: {my_queue.front()}") # 작업1

# 큐에서 데이터 제거 (dequeue)
dequeued_item = my_queue.dequeue()
print(f"제거된 요소: {dequeued_item}") # 작업1
print(f"dequeue 후 큐 상태: {list(my_queue.items)}") # ['작업2', '작업3']

print(f"현재 큐 크기: {my_queue.size()}") # 2
print(f"큐가 비어 있나요?: {my_queue.is_empty()}") # False