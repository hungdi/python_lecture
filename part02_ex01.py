# part02_ex01.py
# 이진 트리 노드 클래스 구현
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 이진 트리 클래스 (간단한 탐색 및 삽입 예제)
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """트리에 새 노드를 삽입합니다."""
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert(node.right, data)
    
    def search(self, data):
        """트리에서 데이터를 검색합니다."""
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None or node.data == data:
            return node
        
        if data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)
        

my_tree = BinaryTree()

# 트리 노드 삽입
my_tree.insert(50)
my_tree.insert(30)
my_tree.insert(70)
my_tree.insert(20)
my_tree.insert(40)
my_tree.insert(60)
my_tree.insert(80)

# 트리 탐색
found_node = my_tree.search(40)
if found_node:
    print(f"값 40을 찾았습니다: {found_node.data}") # 40
else:
    print("값을 찾을 수 없습니다.")

not_found = my_tree.search(90)
if not_found:
    print(f"값 90을 찾았습니다: {not_found.data}")
else:
    print("값을 찾을 수 없습니다.") # 값을 찾을 수 없습니다.