class Job:
    def __init__(self, hp, alive = True, decreasing_hp = 10):
        self.hp = hp
        self.alive = alive
        self.decreasing_hp = decreasing_hp
        pass
    
    def is_alive(self):
        if self.hp <= 0:
            self.alive = False
            return False
        
        return True
    
    def consume_energe(self):
        self.hp -= self.decreasing_hp


    def get_hp(self):
        return self.hp
    

class Civilian(Job):
    def __init__(self, hp=100):
        super().__init__(hp, True, 10)



class Police(Job):
    def __init__(self, hp=100):
        super().__init__(100, True, 10)
        

class Doctor(Job):
    def __init__(self, hp=100):
        super().__init__(100, True, 10)


class Thief(Job):
    def __init__(self, hp=100):
        super().__init__(100, True, 20)