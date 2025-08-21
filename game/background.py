from PyQt5.QtGui import QPixmap
from . import config
from .event import ChangeMapEvent

class Background:
    def __init__(self, game_bus):
        self.game_bus = game_bus
        self.bg = QPixmap("assets/background.png")
        self.wall_width = 200
        self.origin_x = 0
        self.origin_y = 0
        self.game_bus.on(ChangeMapEvent, self._change_background)

    def _change_background(self, changeMapEvent: ChangeMapEvent):
        #level = dict.get('level', 0)
        level = changeMapEvent.level
        if level > config.FIRST_CHANGE_MAP_LEVEL:
            self.bg = QPixmap("assets/background_lava.png")
    
    def play_rect(self):
        w = self.wall_width
        return(w,w,self.width()-w,self.height()-w)

    def draw(self, painter):
        painter.drawPixmap(0, 0, self.bg)

    def height(self):
        return self.bg.height()

    def width(self):
        return self.bg.width()
