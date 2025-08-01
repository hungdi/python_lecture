import unittest

class TestRaise(unittest.TestCase):
    def test_raise(self):
        # 내부함수(또는 중첩함수)
        # 테스트 할 떄만 쓰는 함수로 바깥에 노출할 필요가 없어서, 캡슐화를 목적으로 함
        # 외부 함수의 변수에 접근할 수 있기 때문에 클로저로도 사용됨 (추후배울개념)
        def divide(x, y): 
            return x/y
        
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

unittest.main()

