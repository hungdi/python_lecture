from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QRect
# alpha 추출용 함수
from PyQt5.QtGui import qAlpha

def crop_transparent_area(pixmap: QPixmap) -> QPixmap:
    image = pixmap.toImage().convertToFormat(QImage.Format_ARGB32)
    width = image.width()
    height = image.height()

    min_x, min_y = width, height
    max_x, max_y = 0, 0

    for y in range(height):
        for x in range(width):
            alpha = qAlpha(image.pixel(x, y))
            if alpha > 0:
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)

    if min_x > max_x or min_y > max_y:
        return QPixmap()  # 모두 투명이면 빈 픽스맵

    rect = QRect(min_x, min_y, max_x - min_x + 1, max_y - min_y + 1)
    return pixmap.copy(rect)
