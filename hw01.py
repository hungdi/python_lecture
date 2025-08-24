class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList 클래스
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

    def delete_node(self, node_to_delete):
        if self.head is None or node_to_delete is None:
            return
        
        if self.head == node_to_delete:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next != node_to_delete:
            current = current.next
        
        if current.next:
            current.next = node_to_delete.next

    def get_head(self):
        return self.head
    
# ObjectPool 클래스
class ObjectPool:
    def __init__(self, size=10):
        self.pool = []
        for i in range(size):
            self.pool.append({"id": i, "active": False, "x": 0, "y": 0})

    def get_object(self):
        for obj in self.pool:
            if not obj["active"]:
                obj["active"] = True
                return obj
        return None

    def return_object(self, obj):
        obj["active"] = False

# GameManager 클래스
class GameManager:
    def __init__(self):
        self.pool = ObjectPool(size=5)
        self.active_projectiles = LinkedList()
        self.next_id = 0

    def fire_projectile(self):
        projectile = self.pool.get_object()
        if projectile:
            projectile["x"] = 0
            projectile["y"] = 0
            print(f"발사: 총알 ID {projectile['id']}")
            self.active_projectiles.append(projectile)
        else:
            print("풀이 비어있어 총알을 발사할 수 없습니다.")

    def deactivate_projectile(self, node_to_delete):
        if node_to_delete:
            projectile = node_to_delete.data
            print(f"총알 ID {projectile['id']} 비활성화")
            self.pool.return_object(projectile)
            self.active_projectiles.delete_node(node_to_delete)

    def update(self):
        current_node = self.active_projectiles.get_head()
        while current_node:
            # 총알 위치 업데이트
            current_node.data["x"] += 1
            
            # 총알이 화면 밖으로 나갔는지 확인 (x > 5)
            if current_node.data["x"] > 5:
                # 다음 노드를 미리 저장해두고 현재 노드 삭제
                next_node = current_node.next
                self.deactivate_projectile(current_node)
                current_node = next_node
            else:
                current_node = current_node.next
    
    def display_active(self):
        current_node = self.active_projectiles.get_head()
        print("활성화된 총알: ", end="")
        if current_node:
            while current_node:
                print(f"{current_node.data['id']} -> ", end="")
                current_node = current_node.next
        print("None")


game = GameManager()

print("---1. 총알 3개 발사---")
game.fire_projectile() # ID 0
game.fire_projectile() # ID 1
game.fire_projectile() # ID 2
game.display_active()

print("\n---2. 1회 업데이트 (총알 이동)---")
game.update()
game.display_active()

print("\n---3. 3회 업데이트 (총알 소멸)---")
game.update()
game.update()
game.update()
game.display_active() # ID 0, 1, 2는 화면 밖으로 나가 비활성화됨

print("\n---4. 다시 총알 2개 발사 (풀 재사용)---")
game.fire_projectile() # ID 0 재사용
game.fire_projectile() # ID 1 재사용
game.display_active()
