# 1. 문자형

# 작은 따옴표 속에 큰 따옴표 넣기
print('"파이썬은 재밌습니다"라고 말했습니다')

# 큰 따옴표 속에 작은 따옴표 넣기
print("'파이썬은 재미있습니다'라고 생각했어요")

# 이스케이프 문자를 이용해서 ('\') 출력하기
print("\"파이썬은 재미있어요\"라고 말했습니다")
print('\'파이썬은 재미있어요\'라고 생각했습니다')
print('\\\'파이썬은 재미있어요\\\'라고 생각했습니다')

# 여러 줄의 문자열 만들기
print("안녕하세요. \n재미있는 파이썬, \n공부가 제일 쉬웠어요 \n")

# 여러줄 문자열 기능 
print("""
안녕하세요
파이썬 정말 재미있습니다.
파이썬 공부가 제일 쉽습니다.
""")

# 문자열 인덱싱
print("Hello"[-4])
# print("Hello"[-6])
s = "Hello"
print(s[-5] == s[0])

# 문자열 슬라이싱
print(s[1:4]) # 마지막 숫자를 포함하지 않음, start <= x < end
print(s[1:]) # 1~4
print(s[:3]) # 0~2
print(s[-4:]) # 1~4

# 문자열 길이 구하기
print(len(s))

# 결과예측해보기
print("#연습문제")
print("\\\\\\\\")
print("-" * 8)

# 2. 숫자형
print(0.52273e2)
print(0.52273e-2)

print("3 * 5 =", 3*5)
print("3 / 5 =", 3/5)
print("5 / 7 =", 5/7)
print("8 / 3 =", 8/3)
print("8 // 3 =", 8//3)
print("5 % 2=", 5%2)
print("5 ** 2=", 5**2)

# 3. Boolean type
if "1":
    print("\"1\"은 True")
print(bool(1))
print(bool(0))
print(bool([]))


print(str(1))
print(str(0))
print(str(1) + str(0))
print(int(1) + int(0))

print(int(3.14))
print(float(1))
print(str(12345)+str(67890))

print(bool(12345))
#github test