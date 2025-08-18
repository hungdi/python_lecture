import random
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect

class Potion:
    def __init__(self):
        self.po = QPixmap("assets/potion.png")
        self.x = self.y = 0
        self.amount = 50
        self.taken = False

    def spawn(self, background):
        left, top, right, bottom = background.play_rect()
        self.x = random.randint(left, right - self.width())
        self.y = random.randint(top, bottom - self.height())

    def draw(self, painter):
        if not self.taken:
            painter.drawPixmap(int(self.x), int(self.y), self.po)


    def rect(self):
        return QRect(int(self.x), int(self.y) , self.width(), self.height())

    def width(self):
        return self.po.width()
    
    def height(self):
        return self.po.height()