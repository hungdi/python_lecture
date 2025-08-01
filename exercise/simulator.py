

class SurvivalSimulator:
    def __init__(self, users, test_mode=True):
        self.users = users
        self.test_mode = test_mode
    
    def simulate_day(self):
        for user in self.users:
            user.job.consume_energe()

            if not user.job.is_alive():
                continue

            # TODO: 추가로 시뮬레이팅 할게 있다면 이쪽에 작성
            




