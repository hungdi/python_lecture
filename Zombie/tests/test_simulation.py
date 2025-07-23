import unittest
from simulator import SurvivalSimulator
from user import User
from job import Civilian, Police, Thief

class TestSimulation(unittest.TestCase):
    """시뮬레이션 로직 테스트"""

    def setUp(self):
        """
        테스트를 위한 기본 객체 초기화
        - 시뮬레이터 인스턴스
        - 각 직업군별 유저 (시민, 경찰, 강도)
        """
        self.simulator = SurvivalSimulator()
        self.civilian = User("시민", Civilian(), health=100)
        self.police = User("경찰", Police(), health=100)
        self.thief = User("강도", Thief(), health=60)

    def test_energy_consumption(self):
        """
        에너지 소모 테스트
        Input:
        - 시민 (소모량 10)
        - 경찰 (소모량 10)
        - 강도 (소모량 20)
        Expected:
        - 각 직업별 소모량만큼 체력 감소
        """
        self.simulator.consume_energy(self.civilian)
        self.simulator.consume_energy(self.police)
        self.simulator.consume_energy(self.thief)
        
        self.assertEqual(self.civilian.health, 90)  # 100 - 10
        self.assertEqual(self.police.health, 90)    # 100 - 10
        self.assertEqual(self.thief.health, 40)     # 60 - 20

    def test_death_on_zero_health(self):
        """
        체력 0 도달 시 사망 처리 테스트
        Input:
        - 체력 5인 시민
        - 소모량 10
        Expected:
        - 체력 0으로 설정
        - 생존 상태 False로 변경
        """
        self.civilian.health = 5
        self.simulator.consume_energy(self.civilian)
        
        self.assertEqual(self.civilian.health, 0)
        self.assertFalse(self.civilian.alive)

    def test_infection_progression(self):
        """
        감염 진행 테스트
        Input:
        - 감염된 시민
        - 감염 카운트 2
        Expected:
        - 감염 카운트 3으로 증가
        - 사망 처리 (체력 0, 생존 False)
        """
        self.civilian.status.infected = True
        self.civilian.status.count = 2
        
        self.simulator.update_infection_status(self.civilian)
        
        self.assertEqual(self.civilian.status.count, 3)
        self.assertEqual(self.civilian.health, 0)
        self.assertFalse(self.civilian.alive)

    def test_infection_cure(self):
        """
        해독제를 통한 감염 치료 테스트
        Input:
        - 감염된 시민
        - 감염 카운트 1
        - 해독제 1개 보유
        Expected:
        - 감염 상태 False
        - 감염 카운트 0
        - 해독제 소비
        """
        self.civilian.status.infected = True
        self.civilian.status.count = 1
        self.civilian.antidote.give()
        
        self.simulator.update_infection_status(self.civilian)
        
        self.assertFalse(self.civilian.status.infected)
        self.assertEqual(self.civilian.status.count, 0)
        self.assertEqual(self.civilian.antidote.amount, 0)

    def test_multiple_day_simulation(self):
        """
        여러 날짜 시뮬레이션 테스트
        Input:
        - 시민 (체력 100)
        - 3일 연속 시뮬레이션
        Expected:
        - 매일 에너지 소모
        - 체력이 감소하지만 0 이하로는 떨어지지 않음
        - 생존 상태는 체력에 따라 결정
        """
        for _ in range(3):
            self.simulator.consume_energy(self.civilian)
        
        self.assertEqual(self.civilian.health, 70)  # 100 - (10 * 3)
        self.assertTrue(self.civilian.alive)
        
        # 추가로 7일 더 진행
        for _ in range(7):
            self.simulator.consume_energy(self.civilian)
        
        self.assertEqual(self.civilian.health, 0)  # 완전 소진
        self.assertFalse(self.civilian.alive)

if __name__ == '__main__':
    unittest.main() 