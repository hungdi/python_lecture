#exercise/exercise01.py
import unittest
from simulator import SurvivalSimulator
from user import User
from job import Civilian, Police, Doctor, Thief

class TestSimulation(unittest.TestCase):
    """시뮬레이션 테스트"""

    def setUp(self):
        """테스트 객체 초기화"""
        self.civilian = Civilian(100)
        self.police = Police(100)
        self.thief = Thief(100)
        self.doctor = Doctor(100)
        self.users = [User("시민1", self.civilian),
                      User("경찰1", self.police),
                      User("강도1", self.thief), 
                      User("의사1", self.doctor)]
        self.simulator = SurvivalSimulator(self.users, test_mode=True)
        

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
        self.setUp()
        self.simulator.simulate_day()
        self.assertEqual(self.civilian.get_hp(), 90)
        self.assertEqual(self.police.get_hp(), 90)
        self.assertEqual(self.thief.get_hp(), 80)


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
        self.setUp()
        for _ in range(10):
            self.simulator.simulate_day()
        
        self.assertFalse(self.civilian.is_alive())
        self.assertEqual(self.civilian.get_hp(), 0)



if __name__ == '__main__':
    unittest.main() 