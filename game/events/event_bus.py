from typing import Callable, Dict, List, DefaultDict
from collections import defaultdict
from .events import Event, EventType

class EventBus:
    def __init__(self):
        self._handlers: DefaultDict[EventType, List[Callable[[Event], None]]] = defaultdict(list)

    def subscribe(self, event_type: EventType, handler: Callable[[Event], None]) -> None:
        self._handlers[event_type].append(handler)

    def unsubscribe(self, event_type: EventType, handler: Callable[[Event], None]) -> None:
        if handler in self._handlers[event_type]:
            self._handlers[event_type].remove(handler)

    def publish(self, event: Event) -> None:
        for h in list(self._handlers[event.type]):
            h(event)