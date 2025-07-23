from abc import ABC, abstractmethod
import random
from config import JobStats, InfectionDays, CHEF_CURE_PROB

class Job:
    """직업 기본 클래스"""
    def __init__(self, job_name, stats):
        self.job_name = job_name
        self.basic_hp = stats["hp"]
        self.consume_hp = stats["consume"]
        self.get_food = stats["food_prob"]
        self.food_heal = stats["food_heal"]
        self.get_antidote = stats["antidote_prob"]
        self.max_infection_days = InfectionDays["DEFAULT"]
    
    def handle_infection(self, user):
        """감염 처리 - 해독제 사용 시도"""
        if user.antidote.use(user):
            return True
        return False

class Civilian(Job):
    """시민 직업"""
    def __init__(self):
        super().__init__("시민", JobStats["BASIC"])

class Police(Job):
    """경찰 직업"""
    def __init__(self):
        super().__init__("경찰", JobStats["BASIC"])

class Doctor(Job):
    """의사 직업"""
    def __init__(self):
        super().__init__("의사", JobStats["DOCTOR"])
        self.max_infection_days = InfectionDays["DOCTOR"]

class Chef(Job):
    """요리사 직업"""
    def __init__(self):
        super().__init__("요리사", JobStats["BASIC"])
    
    def handle_infection(self, user):
        """감염 처리 - 해독제 우선, 없으면 식량으로 치료 시도"""
        if super().handle_infection(user):
            return True
            
        # 식량으로 치료 시도
        if user.food.has():
            user.food.take()
            if random.random() < CHEF_CURE_PROB:
                user.status.infected = False
                user.status.count = 0
                return True
        return False

class Soldier(Job):
    """군인 직업"""
    def __init__(self):
        super().__init__("군인", JobStats["SOLDIER"])

class Thief(Job):
    """강도 직업"""
    def __init__(self):
        super().__init__("강도", JobStats["THIEF"])