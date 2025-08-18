class BossRules:
    def __init__(self, bus, mammoth_manager):
        self.bus = bus
        self.mam = mammoth_manager
        self.total_kills_for_boss = 0
        self.boss_active = False

        bus.on('MONSTER_KILLED', self.on_killed)

    def start_boss_phase(self):
        self.boss_active = True
        self.mam.spawn_normals = False
        self.mam.despawn_normals()
        self.mam.spawn_boss()
        self.bus.emit('BOSS_SPAWNED', {})

    def end_boss_phase(self):
        self.boss_active = False
        self.mam.spawn_normals = True
        self.total_kills_for_boss = 0
        self.bus.emit('BOSS_ENDED', {})

    def on_killed(self, data):
        is_boss = data.get('is_boss', False)

        credit = 5 if is_boss else 1
        self.bus.emit('KILL_CREDIT', {'amount': credit, 'source': 'boss' if is_boss else 'normal'})

        if not self.boss_active:
            if not is_boss:
                self.total_kills_for_boss += 1
                if self.total_kills_for_boss >= 10:
                    self.start_boss_phase()
        else:
            if is_boss:
                self.end_boss_phase()
