from collections import deque

stack = deque()

# push
stack.append('A')
stack.append('B')
stack.append('C')
print(f"현재 스택 상태: {stack}") # deque(['A', 'B', 'C'])

# pop
popped_item = stack.pop()
print(f"제거된 요소: {popped_item}") # C
print(f"pop 후 스택 상태: {stack}") # deque(['A', 'B'])