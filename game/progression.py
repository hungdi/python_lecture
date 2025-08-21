from .event import MonsterKilledEvent, LevelUpEvent, ChangeMapEvent

class Progression:
    def __init__(self, monster_bus, game_bus, character, axe_manager):
        self.monster_bus = monster_bus
        self.game_bus = game_bus
        self.ch = character
        self.axe_manager = axe_manager
        self.kills_since_level = 0

        #bus.on('MONSTER_KILLED', self.on_credit)
        self.monster_bus.on(MonsterKilledEvent, self.on_credit)

    def required_kills(self) -> int:
        return self.ch.level + 2

    def _check_change_map(self):
        if self.ch.level > 10:
            return True
        return False
    
    def on_credit(self, monsterKilledEvent: MonsterKilledEvent):
        
        add = 5 if not monsterKilledEvent.is_boss else 1
        self.kills_since_level += add

        print(f"Progression: on_credit started")
        print(f"kills_since_level: {self.kills_since_level}")
        while self.kills_since_level >= self.required_kills():
            self.kills_since_level -= self.required_kills()
            self.ch.level += 1
            # self.bus.emit('LEVEL_UP', {'level':self.ch.level})
            # self.bus.emit('CHANGE_MAP', {'level':self.ch.level})
            self.game_bus.emit(LevelUpEvent(level=self.ch.level))
            self.game_bus.emit(ChangeMapEvent(level=self.ch.level))
            for axe in self.axe_manager.axes.values():
                axe.axe_power()
