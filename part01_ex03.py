try:
    num = int(input("숫자를 입력하세요: "))
    result = 10 / num
    print(f"결과: {result}")
except ValueError:
    print("유효한 숫자가 아닙니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

print("abc")