import unittest
from resource import Food, Antidote
from user import User
from job import Civilian

class TestFood(unittest.TestCase):
    """식량 자원 테스트"""
    
    def test_food_use_normal(self):
        """일반적인 식량 사용을 테스트"""
        food = Food()
        food.give()  # amount=1
        user = User("시민", Civilian(), health=50)
        
        result = food.use(user)
        
        self.assertTrue(result)
        self.assertEqual(food.amount, 0)
        self.assertEqual(user.health, 65)  # 50 + 15
    
    def test_food_use_empty(self):
        """빈 식량 사용 시도를 테스트"""
        food = Food()  # amount=0
        user = User("시민", Civilian(), health=50)
        
        result = food.use(user)
        
        self.assertFalse(result)
        self.assertEqual(food.amount, 0)
        self.assertEqual(user.health, 50)
    
    def test_food_use_max_health(self):
        """최대 체력 근처에서 식량 사용을 테스트"""
        food = Food()
        food.give()  # amount=1
        user = User("시민", Civilian(), health=95)
        
        result = food.use(user)
        
        self.assertTrue(result)
        self.assertEqual(food.amount, 0)
        self.assertEqual(user.health, 100)  # 최대 체력

class TestAntidote(unittest.TestCase):
    """해독제 자원 테스트"""
    
    def test_antidote_use_normal(self):
        """일반적인 해독제 사용을 테스트"""
        antidote = Antidote()
        antidote.give()  # amount=1
        user = User("시민", Civilian(), health=100)
        user.status.infected = True
        user.status.count = 2
        
        result = antidote.use(user)
        
        self.assertTrue(result)
        self.assertEqual(antidote.amount, 0)
        self.assertFalse(user.status.infected)
        self.assertEqual(user.status.count, 0)
    
    def test_antidote_use_empty(self):
        """빈 해독제 사용 시도를 테스트"""
        antidote = Antidote()  # amount=0
        user = User("시민", Civilian(), health=100)
        user.status.infected = True
        user.status.count = 2
        
        result = antidote.use(user)
        
        self.assertFalse(result)
        self.assertEqual(antidote.amount, 0)
        self.assertTrue(user.status.infected)
        self.assertEqual(user.status.count, 2)

if __name__ == '__main__':
    unittest.main() 