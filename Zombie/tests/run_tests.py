import unittest
import sys
import os

# 상위 디렉토리를 파이썬 경로에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 테스트 모듈 import
from tests.test_jobs import TestJobStats, TestInfectionHandling
from tests.test_resources import TestFood, TestAntidote
from tests.test_simulation import TestSimulation
from tests.test_interaction import TestRobberySystem
from tests.test_probability import TestProbabilityWithMock, TestProbabilityStatistical

def run_all_tests():
    # 테스트 스위트 생성
    suite = unittest.TestSuite()
    
    # 직업 관련 테스트
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestJobStats))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestInfectionHandling))
    
    # 자원 테스트
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFood))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAntidote))
    
    # 시뮬레이션 테스트
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSimulation))
    
    # 강도/경찰 시스템 테스트
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRobberySystem))
    
    # 확률 테스트
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestProbabilityWithMock))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestProbabilityStatistical))
    
    # 테스트 실행
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    run_all_tests() 