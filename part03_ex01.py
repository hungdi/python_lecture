class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def search(self, key):
        # 주어진 값을 찾아 해당 노드를 반환함
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next
        return None
    
    def delete_node(self, key):
        
        current = self.head
        if current is not None and current.data == key:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            return
        
        prev.next = current.next
        current = None


my_list = LinkedList()

# 요소 추가
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.print_list() # 1 -> 2 -> 3 -> None

# 요소 탐색
found_node = my_list.search(2)
if found_node:
    print(f"값 2를 찾았습니다: {found_node.data}")
else:
    print("값을 찾을 수 없습니다.")

# 요소 삭제
my_list.delete_node(2)
my_list.print_list() # 1 -> 3 -> None