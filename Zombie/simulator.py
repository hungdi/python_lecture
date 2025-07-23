import random

class SurvivalSimulator:
    def __init__(self, test_mode=False):
        self.test_mode = test_mode  # 테스트 모드에서는 출력하지 않음

    def run_day(self, user):
        self.consume_energy(user)

        if not self.is_alive(user):
            self.handle_death(user)
            return

        self.try_get_food(user)
        self.try_get_antidote(user)
        self.update_infection_status(user)

    def consume_energy(self, user):
        user.health -= user.job.consume_hp
        if user.health <= 0:
            self.handle_death(user)

    def is_alive(self, user):
        return user.health > 0

    def handle_death(self, user):
        user.health = 0
        user.alive = False

    def try_get_food(self, user):
        if self._random() < user.job.get_food:
            user.food.give()
            if not self.test_mode:
                print(f"{user.user_name}이(가) 식량을 얻어 체력을 회복했습니다.")

    def try_get_antidote(self, user):
        if self._random() < user.job.get_antidote:
            user.antidote.give()

    def update_infection_status(self, user):
        if user.antidote.has():
            if user.antidote.use(user):
                if not self.test_mode:
                    print(f"{user.user_name}이(가) 해독제를 사용하여 감염을 치료했습니다.")
            return

        infection_prob = 0.1
        if self._random() < infection_prob or user.status.infected:
            user.status.infected = True
            user.status.count += 1
            if user.status.count >= 3:
                self.handle_death(user)
                if not self.test_mode:
                    print(f"{user.user_name}이(가) 감염으로 사망했습니다.")
        else:
            user.status.infected = False
            user.status.count = 0

    def _random(self):
        """랜덤 값을 생성하는 메서드. 테스트를 위해 오버라이드 가능"""
        return random.random()
