import random
from config import INFECTION_PROB

class SurvivalSimulator:
    def __init__(self, test_mode=False):
        self.test_mode = test_mode

    def run_day(self, user):
        self.consume_energy(user)

        if not self.is_alive(user):
            self.handle_death(user)
            return

        self.try_get_food(user)
        self.try_use_food(user)  # 식량 사용을 별도로 처리
        self.try_get_antidote(user)
        self.update_infection_status(user)

    def consume_energy(self, user):
        """에너지 소모"""
        user.health -= user.job.consume_hp
        if user.health <= 0:
            self.handle_death(user)

    def is_alive(self, user):
        """생존 여부 확인"""
        return user.health > 0

    def handle_death(self, user):
        """사망 처리"""
        user.health = 0
        user.alive = False

    def try_get_food(self, user):
        """식량 획득 시도"""
        if self._random() < user.job.get_food:
            user.food.give()
            if not self.test_mode:
                print(f"{user.user_name}이(가) 식량을 얻었습니다.")
    
    def try_use_food(self, user):
        """식량 사용 시도"""
        if user.food.use(user) and not self.test_mode:
            print(f"{user.user_name}이(가) 식량을 사용하여 체력을 회복했습니다.")

    def try_get_antidote(self, user):
        """해독제 획득 시도"""
        if self._random() < user.job.get_antidote:
            user.antidote.give()

    def update_infection_status(self, user):
        """감염 상태 업데이트"""
        if user.status.infected:
            self._handle_infected_user(user)
        else:
            self._check_new_infection(user)
    
    def _handle_infected_user(self, user):
        """감염된 유저 처리"""
        if not user.job.handle_infection(user):
            self._progress_infection(user)
    
    def _progress_infection(self, user):
        """감염 진행"""
        user.status.count += 1
        
        # 직업별 최대 감염 일수 도달 시 사망
        if user.status.count >= user.job.max_infection_days:
            self._handle_infection_death(user)
            if not self.test_mode:
                print(f"{user.user_name}이(가) {user.job.max_infection_days}일 연속 감염으로 사망했습니다.")
    
    def _handle_infection_death(self, user):
        """감염 사망 처리"""
        self.handle_death(user)
    
    def _check_new_infection(self, user):
        """새로운 감염 체크"""
        if self._random() < INFECTION_PROB:
            user.status.infected = True
            user.status.count = 1
            if not self.test_mode:
                print(f"{user.user_name}이(가) 감염되었습니다.")

    def _random(self):
        """랜덤 값 생성"""
        return random.random()
