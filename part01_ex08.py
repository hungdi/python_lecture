def get_positive_number(num):
    if num <= 0: # 함수는 양수만 받기로 정의했는데, 음수가 들어온 경우 강제 예외 발생
        raise ValueError("입력값은 양수여야 합니다.")
    return num

try:
    get_positive_number(-5)
except ValueError as e:
    print(f"오류: {e}")