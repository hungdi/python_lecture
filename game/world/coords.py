import random
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def screen(self, bg_camera_x):
        #if random.random() > 0.01:
        #    print(f"Coorinate::screen -> self.x[{self.x}] bg_camera_x[{bg_camera_x}]")
        #print(f"Coorinate::screen -> self.x[{self.x}] bg_camera_x[{bg_camera_x}]")
        return self.x - bg_camera_x, self.y
    
    def world(self):
        return self.x, self.y