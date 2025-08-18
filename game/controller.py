from PyQt5.QtCore import Qt

class CharacterManager:
    def __init__(self, character):
        self.character = character
        self.directions = []

    def key_press(self,key):
        if key in (Qt.Key_Left, Qt.Key_Right, Qt.Key_Down, Qt.Key_Up):
            if key not in self.directions:
                self.directions.append(key)

            last = self.directions[-1]
            if last == Qt.Key_Left:
                self.character.facing = 'left'
                self.character.direction = 'left'
            elif last == Qt.Key_Right:
                self.character.facing = 'right'
                self.character.direction = 'right'
            elif last == Qt.Key_Down:
                self.character.facing = 'down'
                self.character.direction = 'down'
            elif last == Qt.Key_Up:
                self.character.facing = 'up'
                self.character.direction = 'up'

    def key_release(self,key):
        if key in self.directions:
            self.directions.remove(key)

        if self.directions:
            last = self.directions[-1]
            if last == Qt.Key_Left:
                self.character.facing = 'left'
                self.character.direction = 'left'
            elif last == Qt.Key_Right:
                self.character.facing = 'right'
                self.character.direction = 'right'
            elif last == Qt.Key_Down:
                self.character.facing = 'down'
                self.character.direction = 'down'
            elif last == Qt.Key_Up:
                self.character.facing = 'up'
                self.character.direction = 'up'
        
        else:
            self.character.direction = None