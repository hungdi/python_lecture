import random
import unittest
from unittest.mock import patch
# 상위 디렉토리를 파이썬 경로에 추가
import sys
import os
# 이 파일의 절대경로 기준으로 상위 디렉토리(zombie)를 sys.path에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from job import Civilian, Police, Thief
from user import User
from interaction import InteractionManager
from config import ROBBERY_FOOD_PROB, POLICE_ARREST_PROB


class TestRobberySystem(unittest.TestCase):
    """강도/경찰 시스템 테스트"""
    
    def setUp(self):
        self.robber = User("강도", Thief(), health=60)
        self.civilian = User("시민", Civilian(), health=100)
        self.police = User("경찰", Police(), health=100)
        
        # 자원 지급
        self.civilian.food.give(2)
        self.civilian.antidote.give(2)
        
        # 테스트용 유저 목록
        self.users = [self.robber, self.civilian, self.police]
        # 테스트 모드로 InteractionManager 초기화
        self.interaction = InteractionManager(self.users, test_mode=True)
    
    def test_rob_food_from_civilian(self):
        """시민으로부터 식량 강탈 테스트"""
        with patch('random.random', return_value=ROBBERY_FOOD_PROB - 0.1):
            self.interaction.perform_robbery(self.robber)
            
            # 강도는 식량을 얻고, 시민은 식량을 잃음
            self.assertEqual(self.robber.food.amount, 1)
            self.assertEqual(self.civilian.food.amount, 1)
            # 해독제는 변화 없음
            self.assertEqual(self.robber.antidote.amount, 0)
            self.assertEqual(self.civilian.antidote.amount, 2)
    
    def test_rob_antidote_from_civilian(self):
        """시민으로부터 해독제 강탈 테스트"""
        with patch('random.random', return_value=ROBBERY_FOOD_PROB + 0.1):
            self.interaction.perform_robbery(self.robber)
            
            # 강도는 해독제를 얻고, 시민은 해독제를 잃음
            self.assertEqual(self.robber.antidote.amount, 1)
            self.assertEqual(self.civilian.antidote.amount, 1)
            # 식량은 변화 없음
            self.assertEqual(self.robber.food.amount, 0)
            self.assertEqual(self.civilian.food.amount, 2)
    
    def test_police_arrest_success(self):
        """경찰의 강도 체포 성공 테스트"""
        # 테스트 모드 비활성화로 경찰과의 조우 활성화
        self.interaction.test_mode = False
        
        # 강도에게 자원 지급
        self.robber.food.give()
        self.robber.antidote.give()
        
        with patch('random.random', return_value=POLICE_ARREST_PROB - 0.1):
            self.interaction.perform_robbery(self.robber)
            
            # 강도 사망 및 자원 압수
            self.assertFalse(self.robber.status.alive)
            self.assertEqual(self.robber.health, 0)
            self.assertEqual(self.robber.food.amount, 0)
            self.assertEqual(self.robber.antidote.amount, 0)
            
            # 경찰이 자원 획득
            self.assertEqual(self.police.food.amount, 1)
            self.assertEqual(self.police.antidote.amount, 1)
    
    def test_police_arrest_failure(self):
        """경찰의 강도 체포 실패 테스트"""
        # 테스트 모드 비활성화로 경찰과의 조우 활성화
        self.interaction.test_mode = False
        
        with patch('random.random') as mock_random:
            # 첫 번째 호출: 체포 실패
            # 두 번째 호출: 식량 강탈
            mock_random.side_effect = [POLICE_ARREST_PROB + 0.1, ROBBERY_FOOD_PROB - 0.1]
            
            self.interaction.perform_robbery(self.robber)
            
            # 강도 생존 및 식량 강탈 성공
            self.assertTrue(self.robber.status.alive)
            self.assertEqual(self.robber.food.amount, 1)
            self.assertEqual(self.civilian.food.amount, 1)
    
    def test_dead_robber_cannot_rob(self):
        """사망한 강도는 강탈 불가 테스트"""
        self.robber.status.alive = False
        self.interaction.perform_robbery(self.robber)
        
        # 시민의 자원 변화 없음
        self.assertEqual(self.civilian.food.amount, 2)
        self.assertEqual(self.civilian.antidote.amount, 2)
    
    def test_rob_empty_victim(self):
        """자원이 없는 시민 강탈 시도 테스트"""
        empty_civilian = User("빈털터리", Civilian(), health=100)
        self.users.append(empty_civilian)
        
        with patch('random.random', return_value=ROBBERY_FOOD_PROB - 0.1):
            self.interaction.perform_robbery(self.robber)
            
            # 강도가 아무것도 얻지 못함
            self.assertEqual(self.robber.food.amount, 0)
            self.assertEqual(self.robber.antidote.amount, 0)

if __name__ == '__main__':
    unittest.main() 