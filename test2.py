# part02_lab01.py
# Queue 클래스 (collections.deque 활용)
from collections import deque
from enum import Enum

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
    

class Event(Enum):
    MOVE = "move"
    ATTACK = "attack"
    HEAL = "heal"

# GameEventQueue 클래스
class GameEventQueue:
    def __init__(self):
        self.event_queue = Queue()

    def add_event(self, evt):
        print(f"이벤트 '{evt}'를 큐에 추가합니다.")
        self.event_queue.enqueue(evt)
    
    def process_event(self):
        if not self.event_queue.is_empty():
            cur_evt = self.event_queue.dequeue()
            print(self._processing(cur_evt))
        

    def _processing(self, evt):
        match evt:
            case Event.MOVE.value:
                return "캐릭터 이동"
            case Event.ATTACK.value:
                return "몬스터 공격"
            case Event.HEAL.value:
                return "체력 회복"
            case _:
                return "알 수 없는 이벤트"




# GameEventQueue 클래스 사용 예제
game_queue = GameEventQueue()

# 1. 이벤트 추가
game_queue.add_event("move")
game_queue.add_event("attack")
game_queue.add_event("heal")
game_queue.add_event("jump")

# 2. 이벤트 처리
print("\n=== 이벤트 처리 시작 ===")
game_queue.process_event()
game_queue.process_event()
game_queue.process_event()
game_queue.process_event()
game_queue.process_event() # 큐가 비어있는 경우
print("=== 이벤트 처리 종료 ===")