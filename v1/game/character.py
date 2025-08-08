from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from game.bullet import Bullet
from game.image_load_error import ImageLoadError
import os
#from game.pixmap_manager import crop_transparent_area

class Character:
    def __init__(self, image: QPixmap, ground_y: int):
        #self.image = image
        self.init_position(ground_y)
        self.init_pixmap(image)

        self.is_jumping = False
        self.jump_velocity = 0
        self.gravity = 1.5
        self.is_shooting = False

        self.shoot_timer = QTimer()
        self.shoot_timer.setSingleShot(True)
        self.shoot_timer.timeout.connect(self.end_shooting)
    def init_position(self, ground_y):
        self.x = 100
        self.y = ground_y
        self.ground_y = ground_y
    
    def init_pixmap(self, image):
        self.original_image = image
        self.shooting_image = QPixmap("assets/character_shoot.png")
        try:
            if self.shooting_image is None or self.shooting_image.isNull:
                raise ImageLoadError
            print("shooting image load success", self.shooting_image.size())
        except ImageLoadError as e:
            print(e.args)
        except Exception as e:
            print(e.args)
        self.image = self.original_image

    
    def start_jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_velocity = -20

    def update(self):
        if self.is_jumping:
            self.y += self.jump_velocity
            self.jump_velocity += self.gravity

            if self.y >= self.ground_y:
                self.y = self.ground_y
                self.is_jumping = False
                self.jump_velocity = 0

        # 이미지 상태 업데이트
        self.image = self.shooting_image if self.is_shooting else self.original_image

    def shoot(self):
        self.is_shooting = True
        self.shoot_timer.start(200)  # 0.2초 후 복귀
        return Bullet(self.x + self.image.width(), int(self.y + self.image.height() / 2))

    def end_shooting(self):
        self.is_shooting = False