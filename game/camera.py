class Camera:
    def __init__(self, camera_w, camera_h, world_w, world_h):
        self.w = camera_w
        self.h = camera_h
        self.world_w = world_w
        self.world_h = world_h
        self.x = 0
        self.y = 0

    def center_on(self, tar_cx, tar_cy):
        self.x = tar_cx - self.w // 2
        self.y = tar_cy - self.h // 2
        self.clamp()

    def clamp(self):
        self.x = max(0, min(self.x, self.world_w - self.w))
        self.y = max(0, min(self.y, self.world_h - self.h))