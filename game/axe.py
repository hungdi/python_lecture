import time
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QRect
from .character import Character

class Axe:
    def __init__(self,character:Character, axe_id):
        self.axe = QPixmap("assets/axe.png")
        self.character = character
        self.id = axe_id
        self.cycle_id = 0
        self.direction = None
        self.init_status()
        self.axe_power()
        self.pixmap_dir()
    
    def set_dir(self):
        if self.direction == 'right':
            self.x = self.character.x + self.character.width()
            self.y = self.character.y + self.character.height()//2
            self.vx = 1
            self.vy = 0

        elif self.direction == 'left':
            self.x = self.character.x
            self.y = self.character.y + self.character.height()//2
            self.vx = -1
            self.vy = 0

        elif self.direction == 'up':
            self.x = self.character.x + self.character.width()//2
            self.y = self.character.y
            self.vx = 0
            self.vy = -1
        
        elif self.direction == 'down':
            self.x = self.character.x + self.character.width()//2
            self.y = self.character.y + self.character.height()
            self.vx = 0
            self.vy = 1

    def pixmap_dir(self):
        self.start_axe_d = self.axe
        self.start_axe_r = self.axe.transformed(QTransform().rotate(-90))
        self.start_axe_l = self.axe.transformed(QTransform().rotate(90))
        self.start_axe_u = self.axe.transformed(QTransform().rotate(180))

    def init_status(self):
        self.speed = 20
        self.return_speed = 0
        self.max_return_speed = 20
        self.acc_speed = 1
        self.angle = 0
        self.rotate_speed = 25
        self.rotate_tick = 0.12
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.state = 'ready'
        self.rotate_time = None
        self.catch_radius = 10

    def axe_power(self):
        lv = self.character.level
        mult = 1 + 0.1 * lv
        self.throw_power = 10 * mult
        self.rotate_power = 1 * mult
        self.return_power = 10 * mult

    def throw(self):
        self.direction = self.character.facing
        self.set_dir()

        self.speed = 20
        self.return_speed = 0
        self.angle = 0
        self.cycle_id += 1
        self.rotate_time = None
        self.state = 'throw'

    def update(self):
        if self.state != 'ready':
            self.angle = (self.angle + self.rotate_speed) % 360

        if self.state == 'ready':
            return

        if self.state == 'throw':
            self.x += self.vx * self.speed
            self.y += self.vy * self.speed
            self.speed -= self.acc_speed
            if self.speed <= 0:
                self.speed = 0
                self.state = 'rotate'
                self.rotate_time = time.time() + 0.5
        
        elif self.state == 'rotate':
            if time.time() >= self.rotate_time:
                self.state = 'return'

        elif self.state == 'return':
            char_cx, char_cy = self.character.center()
            dx = char_cx - self.x
            dy = char_cy - self.y
            dist = (dx**2 + dy**2) ** 0.5
            
            if dist > 0:
                self.vx = dx / dist
                self.vy = dy / dist

            self.return_speed = min(self.return_speed + self.acc_speed, self.max_return_speed)
            self.x += self.vx * self.return_speed
            self.y += self.vy * self.return_speed

            if dist < self.catch_radius :
                self.state = 'ready'
                self.return_speed = 0
    
    def draw(self, painter):
        
        if self.state == 'ready':
            return
        rotated = self.axe.transformed(QTransform().rotate(self.angle), mode=1)
        w, h = rotated.width(), rotated.height()
        painter.drawPixmap(int(self.x-w/2),int(self.y-h/2), rotated)

    def rect(self):
        return QRect(int(self.x - self.width()//2), int(self.y - self.height()//2) , self.width(), self.height())

    def width(self):
        return self.axe.width()
    
    def height(self):
        return self.axe.height()