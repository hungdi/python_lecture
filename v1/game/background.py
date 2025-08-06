from PyQt5.QtGui import QPixmap, QPainter

class Background:
    def __init__(self, image: QPixmap, window_width: int):
        self.image = image
        self.offset = 0
        self.window_width = window_width

    def scroll(self, dx):
        max_scroll = self.image.width() - self.window_width
        self.offset = max(0, min(self.offset + dx, max_scroll))

    def draw(self, painter: QPainter, height: int):
        painter.drawPixmap(
            0, 0,
            self.image.copy(self.offset, 0, self.window_width, height)
        )
