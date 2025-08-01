import unittest


class TestIsNot(unittest.TestCase):
    def test_is_not_same_object(self):
        a = [1, 2]
        b = [1, 2]
        self.assertIsNot(a, b) 
        # 두 객체는 같지 않음
        # 그러므로 테스트는 성공


unittest.main()