from .event import BossEndedEvent, BossSpawnedEvent, MonsterKilledEvent

class BossRules:
    def __init__(self, game_bus, monster_bus, mammoth_manager):
        self.game_bus = game_bus
        self.monster_bus = monster_bus
        self.mam = mammoth_manager
        self.total_kills_for_boss = 0
        self.boss_active = False

        monster_bus.on(MonsterKilledEvent, self.on_killed)

    def start_boss_phase(self):
        self.boss_active = True
        self.mam.spawn_normals = False
        self.mam.despawn_normals()
        self.mam.spawn_boss()
        self.game_bus.emit(BossSpawnedEvent)

    def end_boss_phase(self):
        self.boss_active = False
        self.mam.spawn_normals = True
        self.total_kills_for_boss = 0
        self.game_bus.emit(BossEndedEvent)

    def on_killed(self, monsterKilledEvent: MonsterKilledEvent):
        is_boss = monsterKilledEvent.is_boss

        credit = 5 if is_boss else 1
        # 사용되지 않는 emit구문
        # self.bus.emit('KILL_CREDIT', {'amount': credit, 'source': 'boss' if is_boss else 'normal'})

        if not self.boss_active:
            if not is_boss:
                self.total_kills_for_boss += 1
                if self.total_kills_for_boss >= 10:
                    self.start_boss_phase()
        else:
            if is_boss:
                self.end_boss_phase()
