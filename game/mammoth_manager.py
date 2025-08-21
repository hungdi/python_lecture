import time
from PyQt5.QtCore import Qt
from .mammoth import Mammoth
from .event_bus import EventBus
from .event import MonsterKilledEvent

class MammothManager:
    def __init__(self, background, game_bus: EventBus):
        self.background = background
        self.game_bus = game_bus
        self.max_count = 10
        self.cooldown = 3
        self.last_spawn_time = 0
        self.spawn_normals = True
        self.mammoths = []
        

    def emit_new_deaths(self):
        for m in self.mammoths:
            if m.is_dead and not m.death_emitted:
                m.death_emitted = True
                #self.bus.emit('MONSTER_KILLED', {'monster_id':m.id, 'kind':m.kind, 'is_boss':m.is_boss})
                self.game_bus.emit(MonsterKilledEvent(m.id, m.kind, m.is_boss))

    def spawn_mam(self):
        if self.spawn_normals == False:
            return
        
        now = time.time()
        if len(self.mammoths) >= self.max_count:
            return
        if now - self.last_spawn_time < self.cooldown:
            return
        
        m = Mammoth(self.background)
        self.mammoths.append(m)
        self.last_spawn_time = now

    def update(self, char_x, char_y):
        self.spawn_mam()

        alive = []
        for m in list(self.mammoths):
            m.dir(char_x,char_y)
            m.move(self.background)
            if not m.is_dead:
                alive.append(m)
        
        self.emit_new_deaths()
        
        self.mammoths = [m for m in self.mammoths if not m.is_dead]

        if len(self.mammoths) < self.max_count:
            self.spawn_mam()

    def despawn_normals(self):
        self.mammoths = [m for m in self.mammoths if m.is_boss]

    def spawn_boss(self):
        mult = 2
        m = Mammoth(self.background, is_boss = True)
        m.max_hp = m.max_hp * mult
        m.hp = m.max_hp
        m.power = m.power * mult
        m.set_scale(mult)
        self.mammoths.append(m)

    def check_collision_character(self, char):
        now = time.time()

        for mam in self.mammoths:
            if mam.is_dead:
                continue

            if mam.rect().intersects(char.rect()):
                if now - mam.last_attack_time >= mam.attack_cd:
                    mam.last_attack_time = now
                    char.take_damage(mam.power)

    def check_collision_axe(self, axe):
        now = time.time()
    
        for m in self.mammoths:
            if now >= m.slow_until:
                m.frame_speed_mult = 1.0

        if axe.state == 'ready':
            return
        
        axe_rect = axe.rect()

        for mam in self.mammoths:
            if mam.is_dead:
                continue

            if not mam.rect().intersects(axe_rect):
                continue

            if axe.state == 'rotate':
                last = mam.last_rotate.get(axe.id,0)
                if now - last >= axe.rotate_tick:
                    mam.last_rotate[axe.id] = now
                    mam.take_damage(axe.rotate_power)
                    mam.frame_speed_mult = 0.5
                    mam.slow_until = now + 0.5
                    if mam.is_dead:
                        continue

            elif axe.state in ('throw', 'return'):
                key = (axe.id, axe.state, axe.cycle_id)
                if key not in mam.hit_once:
                    mam.hit_once.add(key)
                    if axe.state == 'throw':
                        mam.take_damage(axe.throw_power)
                    else:
                        mam.take_damage(axe.return_power)
                    mam.frame_speed_mult = 0.5
                    mam.slow_until = now + 0.5
                    
                    if mam.is_dead:
                        continue


    def draw(self, painter):
        for m in self.mammoths:
            m.draw(painter)
    
