# 연습문제1

n = int(input("정수를 입력하세요:"))

for x in range(2,5):
	if n % x == 0:
		print(f"{x}로 나누어 떨어집니다.")
	else:
		print(f"{x}로 나누어 떨어지지 않습니다.")


	


# pass 키워드
number = input("정수 입력:")
number = int(number)
if number > 0:
	# 미구현인 경우
	pass
else:
	print("pass 후에 출력될까?")
	# 미구현인 경우
	pass

