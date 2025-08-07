try:
    num = int(input('정수를 입력하세요:'))
except ValueError:
    print('유효한 정수가 아닙니다.')
else:
    print(f"입력하신 정수는{num} 입니다.")

print(num)