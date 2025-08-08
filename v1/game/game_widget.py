from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QPixmap
from game.character import Character
from game.background import Background
from game.input_handler import InputHandler

class GameWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2D 객체지향 횡스크롤 게임")
        self.setFixedSize(800, 480)

        self.bg = Background(QPixmap("assets/background.png"), self.width())
        self.character = Character(QPixmap("assets/character.png"), self.height() - 48)
        self.input = InputHandler()

        self.timer = QTimer()
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(16)
        self.setFocusPolicy(Qt.StrongFocus)

        self.bullets = []

    def keyPressEvent(self, event):
        self.input.handle_key_press(event.key())
        if event.key() == Qt.Key_Space:
            self.character.start_jump()
        elif event.key() == Qt.Key_Z:
            bullet = self.character.shoot()
            self.bullets.append(bullet)
        
        #print("Pressed:", event.key())  # ← 추가

    def keyReleaseEvent(self, event):
        self.input.handle_key_release(event.key())

    def game_loop(self):
        speed = 5

        if self.input.move_right:
            if self.character.x < self.width() // 2:
                self.character.x += speed
            else:
                self.bg.scroll(speed)

        elif self.input.move_left:
            if self.character.x > self.width() // 2:
                self.character.x -= speed
            else:
                self.bg.scroll(-speed)

        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.x > self.width():
                self.bullets.remove(bullet)

        self.character.update()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.bg.draw(painter, self.height())
        painter.drawPixmap(self.character.x, int(self.character.y), self.character.image)
        for bullet in self.bullets:
            bullet.draw(painter)