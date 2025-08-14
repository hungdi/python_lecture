from game.events.event_bus import EventBus
from game.events.events import EventType, Event

class ScoreManager:
    def __init__(self, bus: EventBus):
        self.score = 0
        self.bus = bus
        self.bus.subscribe(EventType.ENEMY_DIED, self._on_enemy_died)
        pass

    def _on_enemy_died(self, event: Event) -> None:
        pts = int(event.payload.get("points", 0)) if event.payload else 0
        self.add_score(pts)

    def dispose(self) -> None:
        self.bus.unsubscribe(EventType.ENEMY_DIED, self._on_enemy_died)

    def add_score(self, pts):
        self.score += pts
