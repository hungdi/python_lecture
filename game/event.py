

class Event: pass

class GameEvents(Event): pass
class MonsterEvents(Event): pass
class InventoryEvents(Event): pass

class LevelUpEvent(GameEvents):
    def __init__(self, level: int):
        self.level = level


class BossSpawnedEvent(GameEvents):
    def __init__(self):
        pass

class BossEndedEvent(GameEvents):
    def __init__(self):
        pass

class ChangeMapEvent(GameEvents):
    def __init__(self, level):
        self.level = level


#self.bus.emit('MONSTER_KILLED', {'monster_id':m.id, 'kind':m.kind, 'is_boss':m.is_boss})       
class MonsterKilledEvent(MonsterEvents):
    def __init__(self, monster_id: int, kind: str = "Unknown", is_boss: bool = False):
        self.monster_id = monster_id
        self.kind = kind
        self.is_boss = is_boss





