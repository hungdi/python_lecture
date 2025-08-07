from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.image = QPixmap("assets/bullet.png")  # 미리 준비해둔 총알 이미지

    def update(self):
        self.x += self.speed

    def draw(self, painter):
        painter.drawPixmap(self.x, self.y, self.image)
        painter.setBrush(Qt.red)
        painter.drawRect(self.x, self.y, 10, 5)
