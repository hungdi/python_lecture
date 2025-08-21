import random
from PyQt5.QtGui import QPixmap,QTransform, QColor
from PyQt5.QtCore import QRect, Qt
from .background import Background

class Mammoth:
    id_seq = 0

    def __init__(self,background:Background, is_boss = False):
        self.mam_front = QPixmap("assets/mammoth_front.png")
        self.mam_side = QPixmap("assets/mammoth_side.png")
        self.mam_back = QPixmap("assets/mammoth_back.png")
        self.origin_front = self.mam_front
        self.origin_side = self.mam_side
        self.origin_back = self.mam_back
        left, top, right, bottom = background.play_rect()
        print(f"left[{left}], right[{right}], mam_front.width()[{self.mam_front.width()}]")
        self.x = random.randint(left, right - self.mam_front.width())
        print(f"top[{top}], bottom[{bottom}], mam_front.height()[{self.mam_front.height()}]")
        self.y = random.randint(top, bottom - self.mam_front.height())
    
        self.id = Mammoth.id_seq; Mammoth.id_seq += 1
        self.kind = 'mammoth'
        self.is_boss = is_boss
        self.is_dead = False
        self.death_emitted = False
        self.init_status()
        self.pixmap_dir()

    
    def pixmap_dir(self):
        self.mam_d = self.mam_front
        self.mam_r = self.mam_side.transformed(QTransform().scale(-1,1))
        self.mam_l = self.mam_side
        self.mam_u = self.mam_back

    def init_status(self):
        self.speed = 1
        self.hp = 10
        self.max_hp = 10
        self.power = 20
        self.last_attack_time = 0
        self.attack_cd = 1
        self.is_dead = False
        self.facing = None
        self.direction = 'right'
        self.hit_once = set()
        self.last_rotate = {}
        self.rotate_cd = 0.06
        self.frame_speed_mult = 1.0
        self.slow_until = 0

    def dir(self, char_cx, char_cy):
        cx = self.x + self.width()//2
        cy = self.y + self.height()//2

        dx = cx - char_cx
        dy = cy - char_cy

        if abs(dx) >= abs(dy):
            if dx >= 0:
                self.direction = 'left'
            elif dx < 0:
                self.direction = 'right'

        if abs(dx) < abs(dy):
            if dy >= 0:
                self.direction = 'up'
            elif dy < 0:
                self.direction = 'down'

    def move(self, background:Background):
        sp = self.speed * self.frame_speed_mult

        if self.direction == "up":
            self.y -= sp
        elif self.direction == "down":
            self.y += sp
        elif self.direction == "right":
            self.x += sp
        elif self.direction == "left":
            self.x -= sp
        
        left, top, right, bottom = background.play_rect()
        self.x = max(left, min(self.x, right - self.width()))
        self.y = max(top, min(self.y, bottom - self.height()))

    def take_damage(self,power):
        if self.is_dead:
            return
        self.hp -= power
        if self.hp <= 0:
            self.is_dead = True

    def _draw_hp_bar(self, painter, x, y, w, h=6, pad=1):
        painter.fillRect(QRect(int(x), int(y), int(w), h), QColor(60,60,60))
        ratio = 0 if self.max_hp <= 0 else max(0.0, min(1.0, self.hp / self.max_hp))
        fill_w = max(0, int(w * ratio))
        color = QColor(0,200,0) if ratio > 0.5 else (QColor(220,180,0) if ratio > 0.3 else QColor(220,0,0))
        painter.fillRect(QRect(int(x+pad), int(y+pad), max(0, fill_w-2*pad), max(1, h-2*pad)), color)

    def set_scale(self, factor: float):
        # 원본 기준으로 리스케일
        w = max(1, int(self.origin_front.width()  * factor))
        h = max(1, int(self.origin_front.height() * factor))
        self.mam_front = self.origin_front.scaled(w, h, Qt.KeepAspectRatio, Qt.FastTransformation)

        w = max(1, int(self.origin_side.width()  * factor))
        h = max(1, int(self.origin_side.height() * factor))
        self.mam_side  = self.origin_side.scaled(w, h, Qt.KeepAspectRatio, Qt.FastTransformation)

        w = max(1, int(self.origin_back.width()  * factor))
        h = max(1, int(self.origin_back.height() * factor))
        self.mam_back  = self.origin_back.scaled(w, h, Qt.KeepAspectRatio, Qt.FastTransformation)

        # 방향별 스프라이트 다시 설정(우측은 좌우반전)
        self.pixmap_dir()
            
    def draw(self,painter):
        if self.direction == "down":
            pix = self.mam_d
        elif self.direction == "right":
            pix = self.mam_r
        elif self.direction == "left":
            pix = self.mam_l
        elif self.direction == "up":
            pix = self.mam_u

        painter.drawPixmap(int(self.x), int(self.y), pix)
        self._draw_hp_bar(painter, self.x, self.y + self.height() + 4, self.width())

    def rect(self):
        return QRect(int(self.x), int(self.y), self.width(), self.height())

    def width(self):
        return self.mam_front.width()
    
    def height(self):
        return self.mam_front.height()