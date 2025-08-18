from PyQt5.QtGui import QPixmap,QTransform,QColor,QFont
from PyQt5.QtCore import QRect, Qt

class Character:
    def __init__(self):
        self.char_front = QPixmap("assets/babarian_front.png")
        self.char_side = QPixmap("assets/babarian_side.png")
        self.char_back = QPixmap("assets/babarian_back.png")
        self.x = 250
        self.y = 250
        self._last_char = self.char_front
        self.init_status()
        self.pixmap_dir()
    
    def pixmap_dir(self):
        self.char_d = self.char_front
        self.char_r = self.char_side
        self.char_l = self.char_side.transformed(QTransform().scale(-1,1))
        self.char_u = self.char_back

    def init_status(self):
        self.level = 1
        self.speed = 5
        self.hp = 100
        self.max_hp = 100
        self.is_dead = False
        self.facing = None
        self.direction = None

    def power_multi(self):
        return 1.0 + 0.10 * self.level

    def move(self, background):
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        elif self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        
        left, top, right, bottom = background.play_rect()
        self.x = max(left, min(self.x, right - self.width()))
        self.y = max(top, min(self.y, bottom - self.height()))

    def _draw_hp_bar(self, painter, x, y, w, h=6, pad=1):
        painter.fillRect(QRect(int(x), int(y), int(w), h), QColor(60,60,60))
        ratio = 0 if self.max_hp <= 0 else max(0.0, min(1.0, self.hp / self.max_hp))
        fill_w = max(0, int(w * ratio))
        color = QColor(0,200,0) if ratio > 0.5 else (QColor(220,180,0) if ratio > 0.3 else QColor(220,0,0))
        painter.fillRect(QRect(int(x+pad), int(y+pad), max(0, fill_w-2*pad), max(1, h-2*pad)), color)
                
    def draw(self,painter):
        pix = self._last_char
        
        if self.facing == "down":
            pix = self.char_d
        elif self.facing == "right":
            pix = self.char_r
        elif self.facing == "left":
            pix = self.char_l
        elif self.facing == "up":
            pix = self.char_u

        painter.drawPixmap(self.x, self.y, pix)
        self._draw_hp_bar(painter, self.x, self.y + self.height() + 4, self.width())

        painter.setFont(QFont("Arial", 10, QFont.Bold))
        painter.setPen(Qt.yellow)  # 노란색 글씨
        text = f"Lv.{self.level}"
        text_x = self.x + self.width() // 4
        text_y = self.y - 5   # 살짝 위로 띄우기
        painter.drawText(text_x, text_y, text)

        self._last_char = pix

    def take_damage(self, power):
        self.hp -= power
        if self.hp <= 0:
            self.hp = 0
            self.is_dead = True

    def heal(self,amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def center(self):
        cx = self.x + self.width()//2
        cy = self.y + self.height()//2
        return cx, cy
    
    def rect(self):
        return QRect(self.x, self.y, self.width(), self.height())

    def width(self):
        return self.char_front.width()
    
    def height(self):
        return self.char_front.height()