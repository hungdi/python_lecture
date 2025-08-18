import time
from PyQt5.QtCore import Qt
from .axe import Axe
from .event_bus import EventBus

class AxeManager:
    def __init__(self, character, bus):
        self.character = character
        self.cooldown = 0.2
        self.last_throw_time = 0
        self.axes = {1:Axe(self.character,axe_id=1), 2:Axe(self.character,axe_id=2)}
        self.bus = bus
        self.bus.on('LEVEL_UP', self.on_increase_axe)
        
    def on_increase_axe(self, dict):
        cur_level = dict.get('level', 0)
        num = cur_level - len(self.axes)
        if num > 0:
            for idx in range(cur_level, cur_level + num):
                self.axes[idx] = Axe(self.character, axe_id=idx) 

    def key_press(self,key):
        if key != Qt.Key_A:
            return

        now = time.time()

        if now - self.last_throw_time < self.cooldown:
            return
        
        ready_axes = [ax for ax in self.axes.values() if ax.state == 'ready']
        if not ready_axes:
            return
        
        ready_axes.sort(key = lambda a: a.id)
        axe = ready_axes[0]

        axe.throw()
        self.last_throw_time = now

    def update(self):
        for axe in self.axes.values():
            axe.update()


    def draw(self, painter):
        for axe in self.axes.values():
            axe.draw(painter)