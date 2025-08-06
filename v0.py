import sys
sys.path.append("D:/python3.9/Lib/site-packages")
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QTimer

class GameWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2D 횡스크롤 게임")
        self.setFixedSize(800, 480)  # 게임 화면 크기

        # 이미지 로딩
        self.background = QPixmap("background.png")
        self.character = QPixmap("character.png")

        # 초기 위치
        self.char_x = 100
        self.char_y = self.height() - self.character.height()
        self.bg_offset = 0

        # 이동 상태
        self.move_left = False
        self.move_right = False

        # 타이머 설정
        self.timer = QTimer()
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(16)  # 약 60 FPS

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.move_left = True
        elif event.key() == Qt.Key_Right:
            self.move_right = True

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.move_left = False
        elif event.key() == Qt.Key_Right:
            self.move_right = False

    def game_loop(self):
        speed = 5
        max_bg_scroll = self.background.width() - self.width()

        # 캐릭터 이동과 배경 스크롤
        if self.move_right:
            if self.char_x < self.width() // 2:
                self.char_x += speed
            elif self.bg_offset < max_bg_scroll:
                self.bg_offset += speed
            else:
                if self.char_x < self.width() - self.character.width():
                    self.char_x += speed

        if self.move_left:
            if self.char_x > self.width() // 2:
                self.char_x -= speed
            elif self.bg_offset > 0:
                self.bg_offset -= speed
            else:
                if self.char_x > 0:
                    self.char_x -= speed

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        # 배경 그리기
        painter.drawPixmap(0, 0, self.background.copy(self.bg_offset, 0, self.width(), self.height()))

        # 캐릭터 그리기
        painter.drawPixmap(self.char_x, self.char_y, self.character)

def main():
    app = QApplication(sys.argv)
    game = GameWidget()
    game.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
