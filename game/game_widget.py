import time
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QFont
from game.entities.character import Character
from game.world.background import Background
from game.system.controller import CharacterManager
from game.entities.knife import Knife
from game.system.goblin_manager import GoblinManager
from game.system.score_manager import ScoreManager
from game.events.event_bus import EventBus

class GameWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('2D 횡스크롤 게임')
        self.setFixedSize(800,480)

        self.bus = EventBus()

        self.background = Background()
        self.character = Character(100, self.background)
        self.controller = CharacterManager(self.character)
        self.goblin_manager = GoblinManager(self.background, self.character, self.bus)
        
        self.score_manager = ScoreManager(self.bus)
        self.timer = QTimer()
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(16)

        self.knives = []

    def keyPressEvent(self, event):
        self.controller.key_press(event.key())
        if event.key() == Qt.Key_Space:
            self.character.start_jump()

        if event.key() == Qt.Key_A:
            new_knife = Knife(self.character)
            self.knives.append(new_knife)

    def keyReleaseEvent(self, event):
        self.controller.key_release(event.key())

    def check_collision(self):
        self.knives = self.goblin_manager.intersects_knife(self.knives)
        self.goblin_manager.intersects_char()

    def game_loop(self):
        scr_x, scr_y = self.character.pos.screen(self.background.offset)
        if self.character.is_dead == False:
            speed = self.character.speed
            max_scroll = self.background.max_scroll(self.width())

            if self.controller.move_right:
                self.character.direction = "right"
                if scr_x < self.width() // 2:
                    #print(f"scr_x[{scr_x}], self.width()[{self.width()}]")
                    self.character.move_right()
                elif scr_x == self.width() // 2:
                    self.character.move_right()
                    self.background.scroll_right(speed,self.width())
                elif self.background.offset < max_scroll:
                    self.background.scroll_right(speed,self.width())
                else:
                    if scr_x < self.width() - self.character.width():
                        self.character.move_right()

            if self.controller.move_left:
                self.character.direction = "left"
                if scr_x > self.width() // 2:
                    self.character.move_left()
                elif scr_x == self.width() // 2:
                    self.character.move_left()
                    self.background.scroll_left(speed)
                elif self.background.offset > 0:
                    self.background.scroll_left(speed)
                else:
                    if scr_x > 0:
                        self.character.move_left()

            self.character.update_jump()

            for knife in self.knives:
                knife.move()

            for goblin in self.goblin_manager.goblins:
                char_abs_x = self.character.pos.x
                goblin.move(char_abs_x)

            self.check_collision()

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.character.is_dead == False:
            self.background.draw(painter, self.width(), self.height())
            self.character.draw(painter,self.background.offset)

            for knife in self.knives:
                knife.draw(painter, self.background.offset)

            for goblin in self.goblin_manager.goblins:
                goblin.draw(painter, self.background.offset)

            painter.setPen(Qt.white)
            painter.setFont(QFont('Arial', 16, QFont.Bold))
            painter.drawText(12, 28, f"Score: {self.score_manager.score}")

        else:
            painter.setBrush(Qt.black)
            painter.setPen(Qt.NoPen)
            painter.drawRect(self.rect())

            painter.setPen(Qt.white)
            painter.setFont(QFont('Arial', 40, QFont.Bold))

            painter.drawText(self.rect(), Qt.AlignCenter, f"점수:{self.score_manager.score}")
            # painter.drawText(self.rect(), Qt.AlignCenter, "GAME OVER")
            