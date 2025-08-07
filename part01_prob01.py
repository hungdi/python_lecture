# part01_prob01.py
def safe_divider():
    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
        
        result = num1 / num2
        print(f"결과: {num1} / {num2} = {result}")
        
    except ValueError:
        print("오류: 유효한 숫자를 입력해야 합니다.")
    except ZeroDivisionError:
        print("오류: 어떤 숫자도 0으로 나눌 수 없습니다.")

# 함수 실행
safe_divider()