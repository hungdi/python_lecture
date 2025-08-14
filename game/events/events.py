from enum import Enum, auto
from dataclasses import dataclass
from typing import Any

class EventType(Enum):
    ENEMY_DIED = auto()

@dataclass(frozen=True)
class Event:
    type: EventType
    payload: Any = None