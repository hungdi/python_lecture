import unittest
from mymath import add  # add 함수가 들어있는 모듈

class TestAdd(unittest.TestCase):
    def test_add_basic(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)


class TestEqual(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(add(2, 3), 5)


class TestNotEqual(unittest.TestCase):
    def test_not_equal(self):
        self.assertNotEqual(add(2, 3), 10)

if __name__ == "__main__":
    unittest.main()