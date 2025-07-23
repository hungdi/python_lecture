from resource import Food, Antidote

class Status:
    def __init__(self, infected=False, count=0):
        self.infected = infected
        self.count = count

class User:
    def __init__(self, user_name, job, health=100, status=None):
        self.user_name = user_name
        self.job = job
        self.health = health
        self.status = status or Status()
        self.food = Food()
        self.antidote = Antidote()
        self.alive = True

    def summary(self):
        resources = [
            f"{resource.display_name}: {resource.amount}"
            for resource in [self.food, self.antidote]
        ]
        return f"HP: {self.health}, {', '.join(resources)}"
