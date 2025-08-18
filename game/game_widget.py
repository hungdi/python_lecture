from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QFont, QColor
from .character import Character
from .background import Background
from .controller import CharacterManager
from .camera import Camera
from .axe_controller import AxeManager
from .mammoth import Mammoth
from .mammoth_manager import MammothManager
from .potion_manager import PotionManager
from .event_bus import EventBus
from .stats import KillCounter
from .progression import Progression
from .boss_rules import BossRules

class GameWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Babarian Game')
        self.setFixedSize(1000,1000)

        self.bus = EventBus()
        self.background = Background(self.bus)
        self.character = Character()
        self.controller = CharacterManager(self.character)
        self.axe_controller = AxeManager(self.character, self.bus)
        self.mammoth = Mammoth(self.background)
        self.mammoth_controller = MammothManager(self.background,self.bus)
        self.kill_counter = KillCounter(self.bus)
        self.progression = Progression(self.bus, self.character, self.axe_controller)
        self.boss_rules = BossRules(self.bus, self.mammoth_controller)
        self.potion_controller = PotionManager(self.background)
        self.camera = Camera(self.width(), self.height(), self.background.width(), self.background.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(16)

        self.bus.on('MONSTER_KILLED', lambda d: print('[KILLED]', d))
        self.bus.on('BOSS_SPAWNED',  lambda _: print('[BOSS] spawned'))
        self.bus.on('BOSS_ENDED',    lambda _: print('[BOSS] ended'))


    def keyPressEvent(self, event):
        self.controller.key_press(event.key())
        self.axe_controller.key_press(event.key())


    def keyReleaseEvent(self, event):
        self.controller.key_release(event.key())

    def game_loop(self):
        if self.character.is_dead == False:
            if self.character.direction != None:
                self.character.move(self.background)
            elif self.character.direction == None:
                pass
            cx, cy = self.character.center()
            self.axe_controller.update()

            self.mammoth_controller.check_collision_character(self.character)

            for axe in self.axe_controller.axes.values():
                if axe.state != 'ready':
                    self.mammoth_controller.check_collision_axe(axe)

            self.potion_controller.update(self.character)
            self.mammoth_controller.update(cx,cy)
            self.camera.center_on(cx,cy)
        
        self.update()
        

    def paintEvent(self, _):
        painter = QPainter(self)
        painter.setClipRect(0, 0, self.camera.w, self.camera.h)
        painter.translate(-self.camera.x, -self.camera.y)
        self.background.draw(painter)
        self.character.draw(painter)
        self.axe_controller.draw(painter)
        self.mammoth_controller.draw(painter)
        self.potion_controller.draw(painter)

        #AI코드 그대로 
        if self.character.is_dead == False:
            painter.resetTransform()  # 화면 좌표 (0,0)~(width,height)
            painter.setRenderHint(QPainter.TextAntialiasing, True)
            painter.setFont(QFont("Arial", 14, QFont.Bold))

            text = f"KILLS: {getattr(self.kill_counter, 'total_kills', 0)}"
            fm = painter.fontMetrics()
            tw = fm.horizontalAdvance(text)
            th = fm.height()
            pad = 6
            margin = 10

            # 오른쪽 위 위치 계산
            x = self.width() - tw - pad*2 - margin
            y = margin + th //2

            # 반투명 배경 박스
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(0, 0, 0, 120))
            painter.drawRoundedRect(x - pad, y - th - pad, tw + pad*2, th + pad*2, 6, 6)

            # 텍스트
            painter.setPen(QColor(255, 255, 0))
            painter.drawText(x, y, text)

        else:
            painter.resetTransform()
            painter.setBrush(Qt.black)
            painter.setPen(Qt.NoPen)
            painter.drawRect(self.rect())

            painter.setPen(Qt.white)
            painter.setFont(QFont('Arial', 40, QFont.Bold))
            painter.drawText(self.rect(), Qt.AlignCenter, "GAME OVER")