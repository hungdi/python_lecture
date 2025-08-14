from typing import Callable, Dict, List, DefaultDict
from collections import defaultdict
from .events import Event, EventType

class EventBus:
    def __init__(self):
        # 핸들러의 타입을 DefaultDict타입으로 정의한것, 비어있어도 defaultdict(list)로 처리.
        # List[Callable[[Event], None]] : 값이 함수로 되어있다는 것을 정의한 것. 
        # Callable[[Event], None] : 인자로 Event를 하나 받고, 반환값이 없는 함수. (generic의 상세구현을 의미함)
        self._handlers: DefaultDict[EventType, List[Callable[[Event], None]]] = defaultdict(list)

    # 이벤트 핸들러 등록하기
    # event_type에 해당하는 이벤트가 발생하면, 실행할 함수를 등록.
    # 예: 고블린이 죽으면, on_enemy_died 함수를 호출해서 ScoreManager가 점수 +처리
    def subscribe(self, event_type: EventType, handler: Callable[[Event], None]) -> None:
        self._handlers[event_type].append(handler)

    def unsubscribe(self, event_type: EventType, handler: Callable[[Event], None]) -> None:
        if handler in self._handlers[event_type]:
            self._handlers[event_type].remove(handler)

    def publish(self, event: Event) -> None:
        for h in list(self._handlers[event.type]):
            h(event)