class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name}이(가) {self.sound} 소리를 냅니다.")

a1 = Animal("호랑이", "어흥")
a1.make_sound()

a2 = Animal("참새", "짹짹")
a2.make_sound()
