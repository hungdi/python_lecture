#part2_ex10.py
class Parent:
    def __init__(self):
        print("[Parent] __init__ 호출")

    def __del__(self):
        print("[Parent] __del__ 호출")


class Child(Parent):
    def __init__(self):
        print("[Child] __init__ 시작")
        #super().__init__()  # 부모 초기화 명시적으로 호출
        print("[Child] __init__ 끝")

    def __del__(self):
        print("[Child] __del__ 호출")
        #super().__del__()  # 부모 소멸자도 명시적으로 호출 가능 (필수는 아님)


# 테스트
print("== 인스턴스 생성 ==")
obj = Child()

print("== 인스턴스 삭제 ==")
# del obj  # __del__ 호출됨
