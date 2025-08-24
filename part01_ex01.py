class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)


    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "스택이 비어있습니다."
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "스택이 비어있습니다."
        
    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    
my_stack = Stack()

print(f"스택이 비어 있나요?: {my_stack.is_empty()}") # True
print(f"현재 스택 크기: {my_stack.size()}") # 0

# 스택에 데이터 추가 (push)
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print(f"현재 스택 상태: {my_stack.items}") # [10, 20, 30]

# 스택의 가장 위쪽 요소 확인 (peek)
print(f"스택의 가장 위 요소: {my_stack.peek()}") # 30

# 스택에서 데이터 제거 (pop)
popped_item = my_stack.pop()
print(f"제거된 요소: {popped_item}") # 30
print(f"pop 후 스택 상태: {my_stack.items}") # [10, 20]

popped_item2 = my_stack.pop()
print(f"제거된 요소: {popped_item2}") # 20
print(f"pop 후 스택 상태: {my_stack.items}") # [10]

print(f"현재 스택 크기: {my_stack.size()}") # 1
print(f"스택이 비어 있나요?: {my_stack.is_empty()}") # False

my_stack.pop()
my_stack.pop() # 스택이 비어 있으므로 '스택이 비어 있습니다.' 반환