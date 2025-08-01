import unittest
from mymath import add  # add 함수가 들어있는 모듈

class TestFalse(unittest.TestCase):
    def test_is_false(self):
        self.assertFalse(add(2,3) == 2)

unittest.main()