import unittest
from job import Civilian, Police, Doctor, Thief
from user import User, Status

class TestCivilian(unittest.TestCase):
    """시민 직업군 테스트"""
    
    def setUp(self):
        """
        테스트를 위한 시민 객체 초기화
        - 기본 체력: 100
        - 기본 소모: 10
        - 식량 획득 확률: 0.3
        - 체력 회복량: 15
        - 해독제 획득 확률: 0.1
        """
        self.job = Civilian()
        self.user = User("시민", self.job, health=100)

    def test_civilian_basic_stats(self):
        """
        시민의 기본 스탯을 검증
        """
        self.assertEqual(self.job.basic_hp, 100)
        self.assertEqual(self.job.consume_hp, 10)
        self.assertEqual(self.job.get_food, 0.3)
        self.assertEqual(self.job.get_health, 15)
        self.assertEqual(self.job.get_antidote, 0.1)

class TestPolice(unittest.TestCase):
    """경찰 직업군 테스트"""
    
    def setUp(self):
        """
        테스트를 위한 경찰 객체 초기화
        - 기본 체력: 100
        - 기본 소모: 10
        - 식량 획득 확률: 0.3
        - 체력 회복량: 15
        - 해독제 획득 확률: 0.1
        """
        self.job = Police()
        self.user = User("경찰", self.job, health=100)

    def test_police_basic_stats(self):
        """
        경찰의 기본 스탯을 검증
        """
        self.assertEqual(self.job.basic_hp, 100)
        self.assertEqual(self.job.consume_hp, 10)
        self.assertEqual(self.job.get_food, 0.3)
        self.assertEqual(self.job.get_health, 15)
        self.assertEqual(self.job.get_antidote, 0.1)

class TestDoctor(unittest.TestCase):
    """의사 직업군 테스트"""
    
    def setUp(self):
        """
        테스트를 위한 의사 객체 초기화
        - 기본 체력: 80 (낮은 체력)
        - 기본 소모: 10
        - 식량 획득 확률: 0.3
        - 체력 회복량: 15
        - 해독제 획득 확률: 0.3 (높은 해독제 획득)
        """
        self.job = Doctor()
        self.user = User("의사", self.job, health=80)

    def test_doctor_basic_stats(self):
        """
        의사의 기본 스탯을 검증
        - 특히 높은 해독제 획득 확률 검증
        """
        self.assertEqual(self.job.basic_hp, 80)
        self.assertEqual(self.job.consume_hp, 10)
        self.assertEqual(self.job.get_food, 0.3)
        self.assertEqual(self.job.get_health, 15)
        self.assertEqual(self.job.get_antidote, 0.3)

class TestThief(unittest.TestCase):
    """강도 직업군 테스트"""
    
    def setUp(self):
        """
        테스트를 위한 강도 객체 초기화
        - 기본 체력: 60 (매우 낮은 체력)
        - 기본 소모: 20 (높은 소모량)
        - 식량 획득 확률: 0.1 (낮은 획득)
        - 체력 회복량: 15
        - 해독제 획득 확률: 0.05 (매우 낮은 획득)
        """
        self.job = Thief()
        self.user = User("강도", self.job, health=60)

    def test_thief_basic_stats(self):
        """
        강도의 기본 스탯을 검증
        - 낮은 기본 체력
        - 높은 체력 소모량
        - 낮은 자원 획득 확률
        """
        self.assertEqual(self.job.basic_hp, 60)
        self.assertEqual(self.job.consume_hp, 20)
        self.assertEqual(self.job.get_food, 0.1)
        self.assertEqual(self.job.get_health, 15)
        self.assertEqual(self.job.get_antidote, 0.05)

if __name__ == '__main__':
    unittest.main() 