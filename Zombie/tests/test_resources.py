import unittest
from resource import Food, Antidote
from user import User
from job import Civilian

class TestFood(unittest.TestCase):
    """식량 자원 테스트"""

    def setUp(self):
        """
        테스트를 위한 기본 객체 초기화
        - 시민 직업군 사용 (기본 체력 100)
        """
        self.user = User("테스트", Civilian(), health=50)

    def test_food_use_normal(self):
        """
        일반적인 식량 사용을 테스트
        Input:
        - 식량 1개
        - 현재 체력 50
        Expected:
        - 체력 65로 회복 (50 + 15)
        - 식량 0개 남음
        - 사용 결과 True 반환
        """
        food = Food(amount=1)
        result = food.use(self.user)
        
        self.assertTrue(result)
        self.assertEqual(self.user.health, 65)
        self.assertEqual(food.amount, 0)
    
    def test_food_use_empty(self):
        """
        빈 식량 사용 시도를 테스트
        Input:
        - 식량 0개
        - 현재 체력 50
        Expected:
        - 체력 변화 없음
        - 식량 0개 유지
        - 사용 결과 False 반환
        """
        food = Food(amount=0)
        result = food.use(self.user)
        
        self.assertFalse(result)
        self.assertEqual(self.user.health, 50)
        self.assertEqual(food.amount, 0)

    def test_food_use_max_health(self):
        """
        최대 체력 근처에서 식량 사용을 테스트
        Input:
        - 식량 1개
        - 현재 체력 95 (최대 체력 100)
        Expected:
        - 체력 100으로 회복 (최대치)
        - 식량 0개 남음
        - 사용 결과 True 반환
        """
        self.user.health = 95
        food = Food(amount=1)
        result = food.use(self.user)
        
        self.assertTrue(result)
        self.assertEqual(self.user.health, 100)
        self.assertEqual(food.amount, 0)

class TestAntidote(unittest.TestCase):
    """해독제 자원 테스트"""

    def setUp(self):
        """
        테스트를 위한 기본 객체 초기화
        - 시민 직업군 사용
        - 감염 상태로 시작
        """
        self.user = User("테스트", Civilian())
        self.user.status.infected = True
        self.user.status.count = 2

    def test_antidote_use_normal(self):
        """
        일반적인 해독제 사용을 테스트
        Input:
        - 해독제 1개
        - 감염 상태 True
        - 감염 카운트 2
        Expected:
        - 감염 상태 False로 변경
        - 감염 카운트 0으로 초기화
        - 해독제 0개 남음
        - 사용 결과 True 반환
        """
        antidote = Antidote(amount=1)
        result = antidote.use(self.user)
        
        self.assertTrue(result)
        self.assertFalse(self.user.status.infected)
        self.assertEqual(self.user.status.count, 0)
        self.assertEqual(antidote.amount, 0)

    def test_antidote_use_empty(self):
        """
        빈 해독제 사용 시도를 테스트
        Input:
        - 해독제 0개
        - 감염 상태 True
        - 감염 카운트 2
        Expected:
        - 감염 상태 유지
        - 감염 카운트 유지
        - 해독제 0개 유지
        - 사용 결과 False 반환
        """
        antidote = Antidote(amount=0)
        result = antidote.use(self.user)
        
        self.assertFalse(result)
        self.assertTrue(self.user.status.infected)
        self.assertEqual(self.user.status.count, 2)
        self.assertEqual(antidote.amount, 0)

if __name__ == '__main__':
    unittest.main() 