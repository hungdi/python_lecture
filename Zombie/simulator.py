import random

class SurvivalSimulator:
    def run_day(self, user):
        self.consume_energy(user)

        if not self.is_alive(user):
            self.handle_death(user)
            return

        self.try_get_food(user)
        self.try_get_antidote(user)
        self.update_infection_status(user)

    def consume_energy(self, user):
        user.resource.health -= user.job.consume_hp

    def is_alive(self, user):
        return user.resource.health > 0

    def handle_death(self, user):
        user.resource.health = 0
        user.alive = False

    def try_get_food(self, user):
        if random.random() < user.job.get_food:
            user.resource.give("food")
            user.resource.health = min(user.resource.health + user.job.get_health, user.job.basic_hp)

    def try_get_antidote(self, user):
        if random.random() < user.job.get_antidote:
            user.resource.give("antidote")

    def update_infection_status(self, user):
        infection_prob = 0.1
        if random.random() < infection_prob:
            user.status.infected = True
            user.status.count += 1
        else:
            user.status.infected = False
            user.status.count = 0
