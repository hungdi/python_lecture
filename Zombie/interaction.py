import random

class InteractionManager:
    def __init__(self, users):
        self.users = users

    def perform_robbery(self, robber):
        if not self.can_rob(robber):
            return

        victim = self.choose_victim(robber)
        if not victim:
            return

        print(f"{robber.user_name}이(가) {victim.user_name}에게 강탈 시도!")

        if self.is_police(victim):
            self.rob_police(robber, victim)
        else:
            self.rob_civilian_all(robber, victim)

    def can_rob(self, user):
        return user.alive and user.job.job_name == "강도"

    def choose_victim(self, robber):
        candidates = [u for u in self.users if u.alive and u != robber]
        return random.choice(candidates) if candidates else None

    def is_police(self, user):
        return user.job.job_name == "경찰"

    def rob_police(self, robber, police):
        self.transfer_all_resources(police, robber)
        robber.resource.health = 0
        robber.alive = False
        print(f"{robber.user_name}이(가) 경찰 {police.user_name}에게서 자원을 강탈했지만 제압당해 사망했습니다.")

    def rob_civilian_all(self, robber, victim):
        stolen = self.transfer_all_resources(victim, robber)
        if stolen:
            print(f"{robber.user_name}이(가) {victim.user_name}에게서 {', '.join(stolen)} 1개씩을 강탈했습니다.")
        else:
            print(f"{victim.user_name}에게서 뺏을 자원이 없습니다.")

    def transfer_all_resources(self, from_user, to_user):
        items = {"food": "식량", "antidote": "해독제"}
        stolen = []
        for attr, name in items.items():
            if from_user.resource.has(attr):
                from_user.resource.take(attr)
                to_user.resource.give(attr)
                stolen.append(name)
        return stolen
