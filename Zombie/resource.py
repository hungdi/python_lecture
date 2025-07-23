class Resource:
    def __init__(self, food=0, antidote=0, health=100):
        self.food = food
        self.antidote = antidote
        self.health = health

    def has(self, item):
        return getattr(self, item, 0) > 0

    def give(self, item, amount=1):
        setattr(self, item, getattr(self, item, 0) + amount)

    def take(self, item, amount=1):
        current = getattr(self, item, 0)
        setattr(self, item, max(0, current - amount))

    def summary(self):
        return f"HP: {self.health}, 식량: {self.food}, 해독제: {self.antidote}"
