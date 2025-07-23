from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Type

class Resource:
    """자원 기본 클래스"""
    def __init__(self):
        self.amount = 0
    
    def give(self, amount=1):
        """자원 지급"""
        self.amount += amount
    
    def take(self, amount=1):
        """자원 회수"""
        if self.amount >= amount:
            self.amount -= amount
            return True
        return False
    
    def has(self):
        """자원 보유 여부"""
        return self.amount > 0
    
    @property
    def display_name(self):
        """표시 이름"""
        return "자원"

class Food(Resource):
    """식량 클래스"""
    @property
    def display_name(self):
        return "식량"
        
    def use(self, user):
        """식량 사용"""
        if not self.has():
            return False
            
        # 체력이 이미 최대치이면 사용하지 않음
        if user.health >= user.job.basic_hp:
            return False
            
        # 식량 소비
        self.take()
        
        # 직업별 회복량 적용
        heal_amount = user.job.food_heal
        user.health = min(user.health + heal_amount, user.job.basic_hp)
        return True

class Antidote(Resource):
    """해독제 클래스"""
    @property
    def display_name(self):
        return "해독제"
        
    def use(self, user):
        """해독제 사용"""
        if not self.has():
            return False
            
        # 해독제 소비
        self.take()
        
        # 감염 치료
        user.status.infected = False
        user.status.count = 0
        return True
