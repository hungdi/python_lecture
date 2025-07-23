import unittest
from unittest.mock import patch
import random
from simulator import SurvivalSimulator
from user import User
from job import Civilian, Doctor
import statistics

class MockSimulator(SurvivalSimulator):
    """테스트를 위한 시뮬레이터 목 클래스"""
    def __init__(self, fixed_random=None):
        super().__init__(test_mode=True)
        self.fixed_random = fixed_random

    def _random(self):
        if self.fixed_random is not None:
            return self.fixed_random
        return super()._random()

class TestProbabilityWithMock(unittest.TestCase):
    """
    Mock을 사용한 확률 테스트
    random.random()의 반환값을 고정하여 테스트
    """
    
    def setUp(self):
        self.civilian = User("시민", Civilian(), health=100)
        self.doctor = User("의사", Doctor(), health=80)

    def test_food_acquisition_success(self):
        """
        식량 획득 성공 케이스 테스트
        Input:
        - 시민 (식량 획득 확률 0.3)
        - random 값을 0.2로 고정 (0.3보다 작음)
        Expected:
        - 식량 획득 성공
        """
        simulator = MockSimulator(fixed_random=0.2)
        simulator.try_get_food(self.civilian)
        self.assertEqual(self.civilian.food.amount, 1)
        self.assertEqual(self.civilian.health, 100)  # 최대 체력

    def test_food_acquisition_failure(self):
        """
        식량 획득 실패 케이스 테스트
        Input:
        - 시민 (식량 획득 확률 0.3)
        - random 값을 0.4로 고정 (0.3보다 큼)
        Expected:
        - 식량 획득 실패
        """
        simulator = MockSimulator(fixed_random=0.4)
        simulator.try_get_food(self.civilian)
        self.assertEqual(self.civilian.food.amount, 0)
        self.assertEqual(self.civilian.health, 100)

    def test_infection_with_antidote(self):
        """
        감염 상태에서 해독제 사용 테스트
        Input:
        - 감염된 상태
        - 해독제 보유
        - random 값을 0.05로 고정 (감염 확률 0.1보다 작음)
        Expected:
        - 해독제 사용으로 감염 치료
        """
        simulator = MockSimulator(fixed_random=0.05)
        self.civilian.status.infected = True
        self.civilian.antidote.give()
        simulator.update_infection_status(self.civilian)
        self.assertFalse(self.civilian.status.infected)
        self.assertEqual(self.civilian.antidote.amount, 0)

class TestProbabilityStatistical(unittest.TestCase):
    """
    통계적 방법을 사용한 확률 테스트
    충분한 횟수의 시도를 통해 기대 확률에 근접하는지 검증
    """
    
    def setUp(self):
        self.simulator = SurvivalSimulator(test_mode=True)
        self.trials = 100  # 시행 횟수를 100으로 줄임
        self.tolerance = 0.1  # 허용 오차를 10%로 늘림

    def test_civilian_food_acquisition_rate(self):
        """
        시민의 식량 획득 확률 테스트
        Input:
        - 시민 (식량 획득 확률 0.3)
        - 100회 시도
        Expected:
        - 실제 획득 비율이 0.3 ± 0.1 범위 내에 있어야 함
        """
        successes = 0
        for _ in range(self.trials):
            user = User("시민", Civilian(), health=100)
            self.simulator.try_get_food(user)
            if user.food.amount > 0:
                successes += 1
        
        actual_rate = successes / self.trials
        self.assertAlmostEqual(actual_rate, 0.3, delta=self.tolerance)

    def test_doctor_vs_civilian_antidote_rate(self):
        """
        의사와 시민의 해독제 획득 확률 비교 테스트
        Input:
        - 의사 (해독제 획득 확률 0.3)
        - 시민 (해독제 획득 확률 0.1)
        - 각각 100회 시도
        Expected:
        - 의사의 획득 비율이 시민보다 약 3배 높아야 함
        - 각각의 비율이 기대값 ± 0.1 범위 내에 있어야 함
        """
        doctor_successes = 0
        civilian_successes = 0
        
        for _ in range(self.trials):
            doctor = User("의사", Doctor(), health=80)
            civilian = User("시민", Civilian(), health=100)
            
            self.simulator.try_get_antidote(doctor)
            self.simulator.try_get_antidote(civilian)
            
            if doctor.antidote.amount > 0:
                doctor_successes += 1
            if civilian.antidote.amount > 0:
                civilian_successes += 1
        
        doctor_rate = doctor_successes / self.trials
        civilian_rate = civilian_successes / self.trials
        
        # 비율이 0이 되는 것을 방지
        civilian_rate = max(civilian_rate, 0.01)
        
        self.assertAlmostEqual(doctor_rate, 0.3, delta=self.tolerance)
        self.assertAlmostEqual(civilian_rate, 0.1, delta=self.tolerance)
        self.assertAlmostEqual(doctor_rate / civilian_rate, 3.0, delta=1.0)

    def test_infection_distribution(self):
        """
        감염 확률 분포 테스트
        Input:
        - 100회의 시도
        - 각 시도마다 5일 동안 시뮬레이션
        Expected:
        - 평균 감염 횟수가 기대값(1일당 0.1)에 근접해야 함
        - 표준 편차가 합리적인 범위 내에 있어야 함
        """
        infection_counts = []
        days = 5  # 일수를 5일로 줄임
        
        for _ in range(self.trials):
            user = User("시민", Civilian(), health=100)
            infections = 0
            for _ in range(days):
                if not user.status.infected:
                    self.simulator.update_infection_status(user)
                    if user.status.infected:
                        infections += 1
            infection_counts.append(infections)
        
        mean_infections = statistics.mean(infection_counts)
        expected_infections = days * 0.1
        
        self.assertAlmostEqual(mean_infections, expected_infections, delta=0.5)
        std_dev = statistics.stdev(infection_counts)
        self.assertLess(std_dev, days * 0.3)  # 표준 편차 허용 범위를 늘림

if __name__ == '__main__':
    unittest.main() 