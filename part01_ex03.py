#part1_ex03.py
import random

# 공통 부모
class Job:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    def daily_routine(self):
        print(f"[{self.name}] 오늘의 시작 (HP: {self.hp})")
        self.consume_hp()
        self.get_resources()
        self.heal_if_possible()
        self.steal_if_possible()
        print(f"[{self.name}] 오늘의 종료 (HP: {self.hp})\n")

    def heal_if_possible(self): pass
    def steal_if_possible(self): pass

# 역할 1: HP 감소
class HPManager:
    def consume_hp(self):
        self.hp -= self.hp_decay()
        if self.hp <= 0:
            print(f"{self.name} 사망")
            self.hp = 0
        else:
            print(f"{self.name} 체력 감소 -{self.hp_decay()} → {self.hp}")

    def hp_decay(self):
        raise NotImplementedError


# 역할 2: 자원 수집
class ResourceHunter:
    def get_resources(self):
        resources = self.generate_resources()
        print(f"{self.name} 자원 획득: {resources}")

    def generate_resources(self):
        raise NotImplementedError


# 역할 3: 자가 치유
class SelfHealer:
    def heal_if_possible(self):
        if random.random() < self.heal_chance():
            amount = self.heal_amount()
            self.hp += amount
            print(f"{self.name} 체력 회복 +{amount} → {self.hp}")
        else:
            print(f"{self.name} 체력 회복 실패")

    def heal_chance(self):
        return 0.2

    def heal_amount(self):
        return 5


# 역할 4: 도둑질
class ThiefSkill:
    def steal_if_possible(self):
        if random.random() < self.steal_chance():
            print(f"{self.name} 도둑질 성공! 다른 유저 자원 탈취")
        else:
            print(f"{self.name} 도둑질 실패")

    def steal_chance(self):
        return 0.5


# =========================
# 직업별 구현
# =========================

class Doctor(Job, HPManager, ResourceHunter, SelfHealer):
    def __init__(self):
        super().__init__("Doctor", hp=100)

    def hp_decay(self):
        return 2

    def generate_resources(self):
        return {"food": 1, "antidote": random.choice([1, 2])}


class Civilian(Job, HPManager, ResourceHunter):
    def __init__(self):
        super().__init__("Civilian", hp=120)

    def hp_decay(self):
        return 1

    def generate_resources(self):
        return {"food": random.choice([1, 2]), "antidote": 0}


class Thief(Job, HPManager, ResourceHunter, ThiefSkill):
    def __init__(self):
        super().__init__("Thief", hp=90)

    def hp_decay(self):
        return 3

    def generate_resources(self):
        return {"food": 1, "antidote": random.choice([0, 1])}


# =========================
# 시뮬레이션
# =========================

if __name__ == "__main__":
    party = [Doctor(), Civilian(), Thief()]
    for member in party:
        member.daily_routine()