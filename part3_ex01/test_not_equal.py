import unittest
from mymath import add  # add 함수가 들어있는 모듈

class TestNotEqual(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(add(2, 3), 10)

unittest.main()