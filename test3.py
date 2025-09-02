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
        while (last.next):
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        
        print("None")
    
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None
    
    def delete_node(self, key):
        current = self.head
        if current is not None and current.data == key: # head인 경우
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

    
