from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from game.bullet import Bullet
import os
from game.pixmap_manager import crop_transparent_area

class Character:
    def __init__(self, image: QPixmap, ground_y: int):
        self.image = image
        self.x = 100
        self.y = ground_y
        self.ground_y = ground_y

        self.is_jumping = False
        self.jump_velocity = 0
        self.gravity = 1.5
        self.original_image = image
        # 현재 파일 기준 절대경로 설정
        #pixmap = QPixmap("assets/character_shoot.png")
        #print("✅ isNull:", pixmap.isNull())  # True면 문제 있음
        #target_size = self.original_image.size()
        #preprocessed_image = crop_transparent_area(pixmap)
        #self.shooting_image = preprocessed_image
        self.shooting_image = QPixmap("assets/character_shoot.png")
        if self.shooting_image.isNull():
            print("❌ shooting 이미지 로드 실패")
        else:
            print("✅ shooting 이미지 로드 성공:", self.shooting_image.size())
        self.image = self.original_image
        self.is_shooting = False
        self.shoot_timer = QTimer()
        self.shoot_timer.setSingleShot(True)
        self.shoot_timer.timeout.connect(self.end_shooting)

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