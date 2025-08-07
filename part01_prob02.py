# part01_prob02.py
class OutOfRangeError(Exception):
    """1부터 100 사이가 아닌 값을 입력했을 때 발생하는 사용자 정의 예외"""
    pass

def get_number_in_range(num):
    if not 1 <= num <= 100:
        raise OutOfRangeError("입력값이 범위를 벗어났습니다. (1~100 사이)")
    return num

# 예외 처리를 포함한 함수 호출
try:
    user_input = 150
    result = get_number_in_range(user_input)
    print(f"입력하신 숫자는 {result}입니다.")
except OutOfRangeError as e:
    print(f"처리된 오류: {e}")

# 정상 작동하는 경우
try:
    user_input = 50
    result = get_number_in_range(user_input)
    print(f"입력하신 숫자는 {result}입니다.")
except OutOfRangeError as e:
    print(f"처리된 오류: {e}")