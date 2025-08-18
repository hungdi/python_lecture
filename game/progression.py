class Progression:
    def __init__(self, bus, character, axe_manager):
        self.bus = bus
        self.ch = character
        self.axe_manager = axe_manager
        self.kills_since_level = 0

        bus.on('MONSTER_KILLED', self.on_credit)

    def required_kills(self) -> int:
        return self.ch.level + 2

    def _check_change_map(self):
        if self.ch.level > 10:
            return True
        return False
    
    def on_credit(self, data):
        add = 5 if data.get('is_boss', False) else 1
        self.kills_since_level += add

        while self.kills_since_level >= self.required_kills():
            self.kills_since_level -= self.required_kills()
            self.ch.level += 1
            # self.bus.emit('LEVEL_UP', {'new_level': self.ch.level})
            self.bus.emit('LEVEL_UP', {'level':self.ch.level})
            self.bus.emit('CHANGE_MAP', {'level':self.ch.level})
            for axe in self.axe_manager.axes.values():
                axe.axe_power()
