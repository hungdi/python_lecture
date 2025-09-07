# part03_ex02.py
class DNode:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class DoublyLinkedList:
    def __init__(self, values=None):
        # head, tail를 초기화하며, 초기값이 있다면 values를 차례로 보관합니다. (push_back이용)
        self.head = None
        self.tail = None
        if values:
            for v in values:
                self.push_back(v)

    def push_front(self, val):
        # 제일 앞쪽(head앞)에 데이터를 추가합니다.
        node = DNode(val)

        node.next = self.head
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        
        self.head = node
        return node

    def push_back(self, val):
        # 새 노드를 만들어 맨 뒤에 추가합니다.
        node = DNode(val)

        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node
        return node

    def insert_after(self, node, val):
        # 주어진 파라미터 node 뒤에 데이터를 추가합니다.
        # prev, next모두 수정 필요
        nxt = node.next
        new_node = DNode(val)
        new_node.prev = node
        new_node.next = nxt
        node.next = new_node
        if nxt:
            nxt.prev = new_node
        else:
            self.tail = new_node
        return new_node


        return new_node

    def insert_before(self, node, val):
        # 주어진 파라미터 node 앞에 데이터를 추가합니다.
        # prev, next모두 수정 필요
        prv = node.prev
        new_node = DNode(val)
        new_node.next = node
        new_node.prev = prv
        node.prev = new_node
        if prv:
            prv.next = new_node
        else:
            self.head = new_node
        return new_node

    def remove(self, node):
        # 주어진 노드를 삭제합니다. 
        # 앞/뒤의 노드 참조를 연결해주고, 현재 노드를 끊어줍니다.
        prv, nxt = node.prev, node.next
        if prv:
            prv.next = nxt
        else:
            self.head = nxt
        if nxt:
            nxt.prev = prv
        else:
            self.tail = prv
        node.prev = None
        node.next = None

    def __iter__(self):
        # 이 객체를 iterable로 인식하기 위한 매직메서드 오버라이딩입니다.
        # 아래와 같은 코드가 가능하게 만들어줍니다.
        # dll = DoublyLinkedList([1, 2, 3])
        # for value in dll: - 이 코드가 가능해짐!
        # 또한, sum(), max(), in, list()등의 내장 함수, 연산자 용이 가능해집니다!
        
        node = self.head
        while node:
            yield node.val
            node = node.next

    def print_forward(self):
        # head부터 tail까지 순회합니다. 
        # 1 -> 3 -> 9 -> 11 과 같은 방식으로 출력합니다.
        node = self.head
        values = []
        while node:
            values.append(str(node.val))
            node = node.next
        print(" -> ".join(values))


    def print_backward(self):
        # tail부터 head까지 순회합니다.
        # 11 -> 9 -> 3 -> 1 과 같은 방식으로 출력합니다.
        node = self.tail
        values = []
        while node:
            values.append(str(node.val))
            node = node.prev
        print(" <- ".join(values))


if __name__ == "__main__":
    dll = DoublyLinkedList([1, 2, 3])
    a = dll.push_front(0)          # 맨 앞에 0 추가
    b = dll.push_back(4)           # 맨 뒤에 4 추가
    c = dll.insert_after(a, 0.5)   # 0 뒤에 0.5 삽입
    dll.remove(b)                  # 4 삭제

    dll.print_forward()   # 0 -> 0.5 -> 1 -> 2 -> 3
    dll.print_backward()  # 3 <- 2 <- 1 <- 0.5 <- 0