import unittest
from resource import Food, Antidote
from user import User, Status
from job import Civilian, Police, Thief
from simulator import SurvivalSimulator

class TestResource(unittest.TestCase):
    def test_food_use(self):
        """
        식량 사용 시 다음 사항들을 테스트:
        1. 체력이 정상적으로 회복되는지
        2. 식량이 소비되는지
        3. 사용 결과가 True로 반환되는지
        """
        # Given
        food = Food(amount=1)
        user = User("테스트", Civilian(), health=50)
        
        # When
        result = food.use(user)
        
        # Then
        self.assertTrue(result)
        self.assertEqual(user.health, 65)  # 50 + 15
        self.assertEqual(food.amount, 0)
    
    def test_food_use_when_empty(self):
        """
        식량이 없을 때 사용 시도하는 경우를 테스트:
        1. 체력이 변화하지 않는지
        2. 사용 결과가 False로 반환되는지
        3. 식량 수량이 그대로 유지되는지
        """
        # Given
        food = Food(amount=0)
        user = User("테스트", Civilian(), health=50)
        
        # When
        result = food.use(user)
        
        # Then
        self.assertFalse(result)
        self.assertEqual(user.health, 50)
        self.assertEqual(food.amount, 0)

    def test_food_use_max_health(self):
        """
        체력이 거의 최대일 때 식량 사용을 테스트:
        1. 체력이 최대치를 초과하지 않는지
        2. 식량이 정상적으로 소비되는지
        3. 사용 결과가 True로 반환되는지
        """
        # Given
        food = Food(amount=1)
        user = User("테스트", Civilian(), health=95)  # Civilian의 max_hp는 100
        
        # When
        result = food.use(user)
        
        # Then
        self.assertTrue(result)
        self.assertEqual(user.health, 100)  # 최대 체력을 넘지 않아야 함
        self.assertEqual(food.amount, 0)

    def test_antidote_use(self):
        """
        해독제 사용 시 다음 사항들을 테스트:
        1. 감염 상태가 치료되는지
        2. 감염 카운트가 초기화되는지
        3. 해독제가 소비되는지
        4. 사용 결과가 True로 반환되는지
        """
        # Given
        antidote = Antidote(amount=1)
        user = User("테스트", Civilian())
        user.status.infected = True
        user.status.count = 2
        
        # When
        result = antidote.use(user)
        
        # Then
        self.assertTrue(result)
        self.assertFalse(user.status.infected)
        self.assertEqual(user.status.count, 0)
        self.assertEqual(antidote.amount, 0)

class TestUser(unittest.TestCase):
    def test_initial_state(self):
        """
        User 객체 생성 시 초기 상태를 테스트:
        1. 체력이 정상적으로 설정되는지
        2. 생존 상태가 True인지
        3. 식량과 해독제가 0으로 초기화되는지
        4. 감염 상태와 카운트가 초기화되는지
        """
        # Given
        user = User("테스트", Civilian(), health=100)
        
        # Then
        self.assertEqual(user.health, 100)
        self.assertTrue(user.alive)
        self.assertEqual(user.food.amount, 0)
        self.assertEqual(user.antidote.amount, 0)
        self.assertFalse(user.status.infected)
        self.assertEqual(user.status.count, 0)

    def test_summary_format(self):
        """
        User의 상태 요약 문자열 포맷을 테스트:
        1. 체력, 식량, 해독제 정보가 모두 포함되는지
        2. 포맷이 정확한지 ("HP: X, 식량: Y, 해독제: Z" 형식)
        """
        # Given
        user = User("테스트", Civilian(), health=80)
        user.food.give(2)
        user.antidote.give(1)
        
        # When
        summary = user.summary()
        
        # Then
        self.assertEqual(summary, "HP: 80, 식량: 2, 해독제: 1")

class TestSimulator(unittest.TestCase):
    def setUp(self):
        """
        각 테스트 실행 전에 필요한 객체들을 초기화:
        1. 시뮬레이터 인스턴스
        2. 시민, 경찰, 강도 유저 객체
        """
        self.simulator = SurvivalSimulator()
        self.civilian = User("시민", Civilian(), health=100)
        self.police = User("경찰", Police(), health=100)
        self.thief = User("강도", Thief(), health=60)

    def test_consume_energy(self):
        """
        에너지 소모 기능을 테스트:
        1. 체력이 직업별 소모량만큼 정확히 감소하는지
        """
        # When
        self.simulator.consume_energy(self.civilian)
        
        # Then
        self.assertEqual(self.civilian.health, 90)  # 100 - 10(consume_hp)

    def test_death_on_zero_health(self):
        """
        체력이 0 이하가 될 때 사망 처리를 테스트:
        1. 체력이 정확히 0으로 설정되는지
        2. 생존 상태가 False로 변경되는지
        """
        # Given
        self.civilian.health = 5
        
        # When
        self.simulator.consume_energy(self.civilian)
        
        # Then
        self.assertEqual(self.civilian.health, 0)
        self.assertFalse(self.civilian.alive)

    def test_infection_death(self):
        """
        감염으로 인한 사망을 테스트:
        1. 감염 카운트가 3이 되면 사망하는지
        2. 사망 시 체력이 0이 되는지
        3. 생존 상태가 False로 변경되는지
        """
        # Given
        self.civilian.status.infected = True
        self.civilian.status.count = 2  # 2에서 시작해서 update_infection_status에서 3이 됨
        
        # When
        self.simulator.update_infection_status(self.civilian)  # 랜덤 확률 무시하고 강제로 감염 상태 업데이트
        
        # Then
        self.assertEqual(self.civilian.status.count, 3)
        self.assertEqual(self.civilian.health, 0)
        self.assertFalse(self.civilian.alive)

    def test_infection_cure(self):
        """
        해독제를 사용한 감염 치료를 테스트:
        1. 감염 상태가 False로 변경되는지
        2. 감염 카운트가 0으로 초기화되는지
        """
        # Given
        self.civilian.status.infected = True
        self.civilian.status.count = 1
        self.civilian.antidote.give()
        
        # When
        self.simulator.update_infection_status(self.civilian)
        
        # Then
        self.assertFalse(self.civilian.status.infected)
        self.assertEqual(self.civilian.status.count, 0)

if __name__ == '__main__':
    unittest.main() 