import unittest
from unittest.mock import patch
import random
from job import Civilian, Police, Doctor, Chef, Thief
from user import User, Status
from config import JobStats, InfectionDays, CHEF_CURE_PROB

class TestJobStats(unittest.TestCase):
    """직업별 기본 스탯 테스트"""
    
    def test_civilian_stats(self):
        """시민 기본 스탯 검증"""
        civilian = Civilian()
        self.assertEqual(civilian.basic_hp, JobStats["BASIC"]["hp"])
        self.assertEqual(civilian.consume_hp, JobStats["BASIC"]["consume"])
        self.assertEqual(civilian.get_food, JobStats["BASIC"]["food_prob"])
        self.assertEqual(civilian.get_antidote, JobStats["BASIC"]["antidote_prob"])
    
    def test_doctor_stats(self):
        """의사 기본 스탯 검증"""
        doctor = Doctor()
        self.assertEqual(doctor.basic_hp, JobStats["DOCTOR"]["hp"])
        self.assertEqual(doctor.get_antidote, JobStats["DOCTOR"]["antidote_prob"])
        self.assertEqual(doctor.max_infection_days, InfectionDays["DOCTOR"])
    
    def test_thief_stats(self):
        """강도 기본 스탯 검증"""
        thief = Thief()
        self.assertEqual(thief.basic_hp, JobStats["THIEF"]["hp"])
        self.assertEqual(thief.consume_hp, JobStats["THIEF"]["consume"])
        self.assertEqual(thief.get_food, JobStats["THIEF"]["food_prob"])

class TestInfectionHandling(unittest.TestCase):
    """감염 처리 관련 테스트"""
    
    def setUp(self):
        self.civilian = User("시민", Civilian(), health=100)
        self.doctor = User("의사", Doctor(), health=80)
        self.chef = User("요리사", Chef(), health=100)
    
    def test_infection_days_limit(self):
        """직업별 감염 지속 일수 검증"""
        self.assertEqual(self.civilian.job.max_infection_days, InfectionDays["DEFAULT"])
        self.assertEqual(self.doctor.job.max_infection_days, InfectionDays["DOCTOR"])
        self.assertEqual(self.chef.job.max_infection_days, InfectionDays["DEFAULT"])
    
    def test_chef_cure_with_food_success(self):
        """요리사의 식량으로 감염 치료 성공 케이스"""
        self.chef.status.infected = True
        self.chef.food.give()
        
        with patch('random.random', return_value=CHEF_CURE_PROB - 0.1):
            result = self.chef.job.handle_infection(self.chef)
            self.assertTrue(result)
            self.assertFalse(self.chef.status.infected)
            self.assertEqual(self.chef.status.count, 0)
            self.assertEqual(self.chef.food.amount, 0)
    
    def test_chef_cure_with_food_failure(self):
        """요리사의 식량으로 감염 치료 실패 케이스"""
        self.chef.status.infected = True
        self.chef.food.give()
        
        with patch('random.random', return_value=CHEF_CURE_PROB + 0.1):
            result = self.chef.job.handle_infection(self.chef)
            self.assertFalse(result)
            self.assertTrue(self.chef.status.infected)
            self.assertEqual(self.chef.food.amount, 0)
    
    def test_chef_cure_without_food(self):
        """요리사가 식량 없이 치료 시도"""
        self.chef.status.infected = True
        result = self.chef.job.handle_infection(self.chef)
        self.assertFalse(result)
        self.assertTrue(self.chef.status.infected)
    
    def test_antidote_priority_over_food(self):
        """해독제가 있을 경우 식량 치료보다 우선 사용"""
        self.chef.status.infected = True
        self.chef.food.give()
        self.chef.antidote.give()
        
        result = self.chef.job.handle_infection(self.chef)
        self.assertTrue(result)
        self.assertFalse(self.chef.status.infected)
        self.assertEqual(self.chef.antidote.amount, 0)
        self.assertEqual(self.chef.food.amount, 1)  # 식량은 소비되지 않음

if __name__ == '__main__':
    unittest.main() 