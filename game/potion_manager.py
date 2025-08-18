import time
from .potion import Potion

class PotionManager:
    def __init__(self, background):
        self.background = background
        self.potions = []
        self.max_count = 3
        self.cooldown = 30
        self.last_spawn = 0

    def spawn_potion(self):
        now = time.time()
        if len(self.potions) < self.max_count and (now-self.last_spawn) >= self.cooldown:
            p = Potion()
            p.spawn(self.background)
            self.potions.append(p)
            self.last_spawn = now

    def update(self, character):
        self.spawn_potion()
        not_taken = []
        char_rect = character.rect()
        
        for p in self.potions:
            
            if (not p.taken) and p.rect().intersects(char_rect):
                character.heal(p.amount)
                p.taken = True

            if not p.taken:
                not_taken.append(p)

        self.potions = not_taken

    def draw(self, painter):
        for p in self.potions:
            p.draw(painter)