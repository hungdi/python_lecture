from enum import Enum, auto
from dataclasses import dataclass
from typing import Any

class EventType(Enum):
    ENEMY_DIED = auto()
    ENEMY_SPAWNED = auto()

# frozen = True : 불변 객체로 만듬 (한번 만든 후 속성 변경 불가)
# Any (타입제한없이 아무값이나 받을 수 있음), 기본값은 None
# 사용의 예
# event = Event(type=EventType.ENEMY_DIED, payload={"enemy_id": 42})
@dataclass(frozen=True)
class Event:
    type: EventType
    payload: Any = None