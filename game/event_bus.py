from typing import Generic, TypeVar, Dict, Callable, Type, Any, List
from .event import Event


T = TypeVar('T', bound=Event)

class EventBus(Generic[T]):
    def __init__(self):
        self._subs: Dict[Type[Event], List[Callable[[Event], Any]]] = {}

    def on(self, event_class: Type[T], callback: Callable[[T], Any]):
        self._subs.setdefault(event_class, []).append(callback)

    def emit(self, event_instance: T):
        event_class = type(event_instance)
        callbacks = self._subs.get(event_class, [])
        for cb in callbacks:
            cb(event_instance)




