from PyQt5.QtGui import QPixmap

class Character:
    def __init__(self, image: QPixmap, ground_y: int):
        self.image = image
        self.x = 100
        self.y = ground_y
        self.ground_y = ground_y

        self.is_jumping = False
        self.jump_velocity = 0
        self.gravity = 1.5

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
