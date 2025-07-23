from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Type

class Resource(ABC):
    def __init__(self, amount=0):
        self.amount = amount

    def has(self):
        return self.amount > 0

    def give(self, amount=1):
        self.amount += amount

    def take(self, amount=1):
        if self.amount >= amount:
            self.amount -= amount
            return True
        return False

    @abstractmethod
    def use(self, user):
        pass

    @property
    @abstractmethod
    def display_name(self) -> str:
        pass

class Food(Resource):
    @property
    def display_name(self) -> str:
        return "식량"

    def use(self, user):
        if self.has():
            if self.take():  # 성공적으로 소비했을 때만 효과 적용
                user.health = min(user.health + 15, user.job.basic_hp)
                return True
        return False

class Antidote(Resource):
    @property
    def display_name(self) -> str:
        return "해독제"

    def use(self, user):
        if self.has():
            if self.take():  # 성공적으로 소비했을 때만 효과 적용
                user.status.infected = False
                user.status.count = 0
                return True
        return False
