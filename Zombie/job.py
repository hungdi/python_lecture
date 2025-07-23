class Job:
    def __init__(self, job_name, basic_hp, consume_hp, get_food, get_health, get_antidote):
        self.job_name = job_name
        self.basic_hp = basic_hp
        self.consume_hp = consume_hp
        self.get_food = get_food
        self.get_health = get_health
        self.get_antidote = get_antidote

class Civilian(Job):
    def __init__(self):
        super().__init__("시민", 100, 10, 0.3, 15, 0.1)

class Police(Job):
    def __init__(self):
        super().__init__("경찰", 100, 10, 0.3, 15, 0.1)

class Chef(Job):
    def __init__(self):
        super().__init__("요리사", 100, 10, 0.3, 15, 0.1)

class Military(Job):
    def __init__(self):
        super().__init__("군인", 120, 15, 0.5, 20, 0.1)

class Doctor(Job):
    def __init__(self):
        super().__init__("의사", 80, 10, 0.3, 15, 0.3)

class Thief(Job):
    def __init__(self):
        super().__init__("강도", 60, 20, 0.1, 15, 0.05)