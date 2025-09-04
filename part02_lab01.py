# part02_lab01.py
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

def bst_min(node):
    cur = node
    while cur and cur.left:
        cur = cur.left
    return cur.data if cur else None

def bst_max(node):
    cur = node
    while cur and cur.right:
        cur = cur.right
    return cur.data if cur else None


bt = BinaryTree()
for x in [8,3,10,1,6,14,4,7,13]:
    bt.insert(x)

print(bst_min(bt.root), bst_max(bt.root))
