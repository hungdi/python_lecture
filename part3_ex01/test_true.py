import unittest
from mymath import add  # add 함수가 들어있는 모듈

class TestTrue(unittest.TestCase):
    def test_is_true(self):
        self.assertTrue(add(2, 3) > 4)

unittest.main()