from collections import deque
from enum import Enum

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "큐가 비어있습니다."

class Event(Enum):
    MOVE = "move"
    ATTACK = "attack"
    HEAL = "heal"


# GameEventQueue 클래스
class GameEventQueue:
    def __init__(self):
        self.event_queue = Queue()

    def add_event(self, event):
        # 이벤트를 큐에 추가합니다.
        print(f"이벤트 '{event}'를 큐에 추가합니다.")
        self.event_queue.enqueue(event)

    def process_event(self):
        # 큐에서 이벤트를 꺼내 처리합니다.
        if not self.event_queue.is_empty():
            event = self.event_queue.dequeue()
            if event == Event.MOVE.value:
                print("캐릭터 이동")
            elif event == Event.ATTACK.value:
                print("몬스터 공격")
            elif event == Event.HEAL.value:
                print("체력 회복")
            else:
                print("알 수 없는 이벤트")
        else:
            print("처리할 이벤트가 없습니다.")

    def process_event_match_case(self):
        # match-case 이용
        if not self.event_queue.is_empty():
            event = self.event_queue.dequeue()
            match event:
                case Event.MOVE.value:
                    print("캐릭터 이동")
                case Event.ATTACK.value:
                    print("몬스터 공격")
                case Event.HEAL.value:
                    print("체력 회복")
                case _:
                    print("알 수 없는 이벤트")
        else:
            print("처리할 이벤트가 없습니다.")


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