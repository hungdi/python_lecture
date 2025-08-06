from PyQt5.QtCore import Qt
class InputHandler:
    def __init__(self):
        self.move_left = False
        self.move_right = False

    def handle_key_press(self, key):
        if key == Qt.Key_Left:
            self.move_left = True
        elif key == Qt.Key_Right:
            self.move_right = True

    def handle_key_release(self, key):
        if key == Qt.Key_Left:
            self.move_left = False
        elif key == Qt.Key_Right:
            self.move_right = False
