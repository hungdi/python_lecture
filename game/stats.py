from collections import defaultdict
from .event import MonsterKilledEvent

class KillCounter:
    def __init__(self, monster_bus):
        self.total_kills = 0
        self.kills_by_kind = defaultdict(int)
        monster_bus.on(MonsterKilledEvent, self.on_killed)

    def on_killed(self, monsterKilledEvent: MonsterKilledEvent):
        print(f"KillCounter:on_killed 호출")
        is_boss = monsterKilledEvent.is_boss
        # kind = monsterKilledEvent.kind
        add = 5 if is_boss else 1
        self.total_kills += add
        print(f"total_kills :{self.total_kills}")
